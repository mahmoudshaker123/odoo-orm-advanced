from odoo.addons.portal.controllers.portal import CustomerPortal , pager
from odoo.http import request
from odoo import http

class RealEstatePortal(CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        rtn = super(RealEstatePortal ,self)._prepare_home_portal_values(counters)
        print('inside _prepare_home_portal_values method >>>>>>>>>>>>>>>',rtn)
        rtn['real_estate_counts'] = request.env['property'].search_count([])
        print('val>>>>>>>>>>>>>>>>>>>>>',rtn)
        return rtn

    @http.route(['/my/realestate', '/my/realestate/page/<int:page>'], type='http', auth="user", website=True)
    def RealEstateListView(self, page=1, sortby=None, search=None, search_in='all',groupby='none', **kw):
        real_estate_obj = request.env['property']

        searchbar_groupby = {
            'none': {'label': 'No Group'},
            'owner': {'label': 'Owner'},
        }

        if not groupby:
            groupby = 'none'



        searchbar_inputs = {
            'all': {'label': 'Search in All', 'input': 'all'},
            'name': {'label': 'Name', 'input': 'name'},
            'owner': {'label': 'Owner', 'input': 'owner'},
            'ref': {'label': 'Reference', 'input': 'ref'},
        }
        domain = []

        if search:
            if search_in == 'name':
                domain += [('name', 'ilike', search)]
            elif search_in == 'owner':
                domain += [('owner_id.name', 'ilike', search)]
            elif search_in == 'ref':
                domain += [('ref', 'ilike', search)]
            else:
                domain += ['|', '|',
                           ('name', 'ilike', search),
                           ('owner_id.name', 'ilike', search),
                           ('ref', 'ilike', search)]

        searchbar_sortings = {
            'name': {'label': 'Name', 'order': 'name asc'},
            'price': {'label': 'Selling Price', 'order': 'selling_price desc'},
            'ref': {'label': 'Reference', 'order': 'ref asc'},
        }

        if not sortby:
            sortby = 'name'

        order = searchbar_sortings[sortby]['order']

        step = 5
        total = real_estate_obj.search_count(domain)

        pager_data  = pager(
            url='/my/realestate',
            total=total,
            page=page,
            step=step,
            url_args={
                'sortby': sortby,
                'search': search,
                'search_in': search_in,
                'groupby': groupby,
            }
        )

        records = real_estate_obj.search(
            domain,
            order=order,
            limit=step,
            offset=pager_data['offset']
        )

        grouped_data = {}

        if groupby == 'owner':
            for rec in records:
                key = rec.owner_id.name or "No Owner"

                if key not in grouped_data:
                    grouped_data[key] = []

                grouped_data[key].append(rec)

        else:
            grouped_data = {'All': records}


        values = {
            'grouped_data': grouped_data,
            'groupby': groupby,
            'searchbar_groupby': searchbar_groupby,
            'page_name': 'real_estate_list_view',
            'pager': pager_data,
            'searchbar_sortings': searchbar_sortings,
            'sortby': sortby,
            'searchbar_inputs': searchbar_inputs,
            'search_in': search_in,
            'search': search,
        }

        return request.render("real_estate_portal.real_estate_list_view_portal", values)





    @http.route(['/my/realestate/<model("property"):property_id>'], type='http', website=True, auth="user")
    def RealEstateFormView(self, property_id, **kw):
        real_estate_obj = request.env['property']
        properties = real_estate_obj.search([])
        ids = properties.ids
        current_index = ids.index(property_id.id)
        prev_id = ids[current_index - 1] if current_index > 0 else False
        next_id = ids[current_index + 1] if current_index < len(ids) - 1 else False

        values = {
            'property': property_id,
            'page_name': 'real_estate_form_view',
            'prev_id': prev_id,
            'next_id': next_id,
        }

        return request.render("real_estate_portal.real_estate_form_view_portal", values)

    @http.route('/my/realestate/<model("property"):property_id>/report', auth="user", type="http", website=True)
    def property_report(self, property_id, **kw):

        # if property_id.owner_id != request.env.user.partner_id:
        #     return request.redirect('/my')

        return self._show_report(
            model=property_id,
            report_type='pdf',
            report_ref='app_one.property_report_template',
            download=True
        )

    @http.route('/my/realestate/create', type='http', auth="user", website=True)
    def create_property_form(self, **kw):

        owners = request.env['owner'].sudo().search([])

        values = {
            'page_name': 'real_estate_create',
            'owners': owners,
        }

        return request.render("real_estate_portal.create_property_form", values)

    @http.route('/my/realestate/create/submit', type='http', auth="user", website=True, methods=['POST'])
    def create_property_submit(self, **post):

        owner_id = int(post.get('owner_id')) if post.get('owner_id') else False

        name = post.get('name')

        existing = request.env['property'].sudo().search([
            ('name', '=', name)
        ], limit=1)

        if existing:
            owners = request.env['owner'].sudo().search([])

            return request.render("real_estate_portal.create_property_form", {
                'error': '⚠️ الاسم ده مستخدم قبل كدا',
                'owners': owners,
                'values': post,
            })

        request.env['property'].sudo().create({
            'name': post.get('name'),
            'selling_price': float(post.get('selling_price') or 0),
            'owner_id': owner_id,
            'date_availability': post.get('date_availability'),
            'description': post.get('description'),
            'postcode': post.get('postcode'),
        })

        return request.redirect('/my/realestate')

