from odoo import fields, models



class EqCategory(models.Model):

    _name = 'eq.category'
    _description = 'Equipment Category'

    name= fields.Char(string="Name" ,required=True)
    reference = fields.Char(string="Reference" , required=True)