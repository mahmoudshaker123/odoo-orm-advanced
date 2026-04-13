from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.http import request
from odoo import http

class RealEstatePortal(CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        rtn = super(RealEstatePortal ,self)._prepare_home_portal_values(counters)
        print('inside _prepare_home_portal_values method >>>>>>>>>>>>>>>',rtn)
        rtn['real_estate_counts'] = request.env['property'].search_count([])
        print('val>>>>>>>>>>>>>>>>>>>>>',rtn)
        return rtn

    @http.route(['/my/realestate'] , type='http', auth="user", website=True)
    def RealEstateListView(self,**kw):

        print('Hello you call /my/realestate controller >>>>>> ')
        real_estate_obj = request.env['property']
        real_estate = real_estate_obj.search([])

        return request.render("real_estate_portal.real_estate_list_view",{'real_estate':real_estate})