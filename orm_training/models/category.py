from odoo import models, fields

class OrmCategory(models.Model):
    _name = 'orm.category'
    _description = 'Task Category'

    name = fields.Char(required=True)
    description = fields.Text()
