from odoo import fields, models

class ChangeState(models.TransientModel):
    _name = 'change.state'
    _description = 'Change Property State Wizard'

    property_id = fields.Many2one('property', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('pending', 'Pending'),
    ],
        default='draft',
        required=True,
    )
    reason = fields.Char(required=True)


    def action_confirm(self):
        self.ensure_one()
        if self.property_id.state == 'closed':
            self.property_id.state = self.state
            self.property_id.create_history_record('closed', self.state, self.reason)
