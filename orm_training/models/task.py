from odoo import models, fields, api
from odoo.osv import expression

from odoo.exceptions import ValidationError
from datetime import date ,timedelta


class OrmTask(models.Model):
    _name = 'orm.task'
    _description = 'ORM Task'
    _rec_name = 'title'

    title = fields.Char(required=True)
    description = fields.Text()
    is_done = fields.Boolean(default=False)
    priority = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ], default='medium')

    category_id = fields.Many2one('orm.category', string='Category')
    user_id = fields.Many2one('res.users', default=lambda self: self.env.user)

    start_date = fields.Date()
    end_date = fields.Date()

    days_count = fields.Integer(
        compute="_compute_days_count",
        store=True
    )

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        args = args or []
        # Define your custom search logic here
        domain = expression.OR([
            ('title', operator, name),
            ('priority', operator, name),
            ('category_id', operator, name)
        ])
        # Combine with other existing args if any, and perform the search
        return self.search(expression.AND([domain, args]), limit=limit).name_get()

    @api.model
    def default_get(self, fields_list):
        res = super(OrmTask, self).default_get(fields_list)
        res['description']='Hello From Odoo'
        res['start_date']=date.today()
        res['end_date']=date.today()+ timedelta(days=5)
        print('Fields>>>>>>>>>>>>>>>>>>', fields_list)
        return res


    @api.depends('start_date','end_date')
    def _compute_days_count(self):
        for rec in self:
            if rec.start_date and rec.end_date:
                rec.days_count = (rec.end_date - rec.start_date).days
            else:
                rec.days_count = 0


    def print_name(self):
        for rec in self:
            tasks = self.env['orm.task'].search([])
            high_tasks= tasks.filtered(lambda t:t.priority=='high')
            maths_tasks = tasks.filtered(lambda t:t.category_id.name=='Maths')

            print('Maths >>>>>>>>>>>>>>>>>>>>>>',maths_tasks)





