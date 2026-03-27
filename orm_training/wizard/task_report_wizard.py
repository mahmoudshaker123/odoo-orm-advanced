from odoo import fields , models,_ 
from odoo.exceptions import ValidationError ,UserError

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
        
        
    
    def action_close_tasks(self):
        self.ensure_one()

        # Validation
        if self.date_from > self.date_to:
            raise UserError(_("From Date must be before To Date"))

        domain = [
            ('start_date', '>=', self.date_from),
            ('start_date', '<=', self.date_to),
            ('is_done', '=', False),
        ]

        tasks = self.env['orm.task'].search(domain)

        if not tasks:
            raise UserError(_("No tasks found in the selected period."))

        tasks.write({
            'is_done': True,
            'end_date': self.date_to,
        })

        return {'type': 'ir.actions.act_window_close'}