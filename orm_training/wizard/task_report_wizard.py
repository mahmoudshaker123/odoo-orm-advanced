from odoo import fields , models,api
from odoo.exceptions import ValidationError

class TaskReportWizard(models.TransientModel):
    _name = 'task.report.wizard'
    _description = 'Task Report Wizard'

    date_from = fields.Date(string="From Date" , required=True)
    date_to = fields.Date(string="To Date" , required=True)
    priority = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ], string="Priority")

    def action_show_tasks(self):
        if self.date_from > self.date_to:
            raise ValidationError("From Date must be before To Date")

        domain=[
            ('start_date','>=',self.date_from),
            ('end_date','>=',self.date_to)
        ]

        if self.priority:
            domain.append(('priority', '=', self.priority))

        tasks = self.env['orm.task'].search(domain)

        return {
            'type': 'ir.actions.act_window',
            'name': 'Filtered Tasks',
            'res_model': 'orm.task',
            'view_mode': 'list,form',
            'domain': [('id', 'in', tasks.ids)],
        }



