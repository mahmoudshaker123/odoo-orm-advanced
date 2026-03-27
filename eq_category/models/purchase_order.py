from odoo import fields, models,api

class PurchaseOrderInherit(models.Model):

    _inherit = 'purchase.order.line'
    _description = 'Equipment Category'

    eq_category_id = fields.Many2one('eq.category', string="Equipment Category")

    @api.onchange('product_id')
    def _onchange_product_eq(self):
        for line in self:
            line.eq_category_id = line.product_id.eq_category_id





