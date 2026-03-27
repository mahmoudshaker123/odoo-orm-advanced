from odoo import fields, models



class ProductInherit(models.Model):

    _inherit = 'product.template'
    _description = 'Equipment Category'

    eq_category_id = fields.Many2one('eq.category', string="Equipment Category")

