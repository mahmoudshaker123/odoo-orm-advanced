from odoo import fields,models,api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def default_get(self, fields_list):
        res = super(ResPartner, self).default_get(fields_list)
        res['']
        print('Fields>>>>>>>>>>>>>>>>>>', fields_list)
        return res


