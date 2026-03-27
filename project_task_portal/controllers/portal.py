from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import pager as portal_pager
from odoo.addons.project.controllers.portal import ProjectCustomerPortal


class ProjectTaskPortal(ProjectCustomerPortal):

    def _get_portal_task_domain(self):
        user = request.env.user
        commercial_partner = user.partner_id.commercial_partner_id
        return [
            '|',
            '|',
            ('user_ids', 'in', user.id),
            ('partner_id', 'child_of', commercial_partner.id),
            ('message_partner_ids', 'child_of', commercial_partner.id),
        ]

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)

        if 'task_count' in counters:
            task_count = request.env['project.task'].search_count(
                self._get_portal_task_domain()
            )

            values['task_count'] = task_count

        return values

    @http.route(['/my/tasks', '/my/tasks/page/<int:page>'], type='http', auth="user", website=True)
    def portal_my_tasks(self, page=1, date_begin=None, date_end=None, sortby=None, search=None, search_in='name', groupby=None, **kwargs):
        values = self._prepare_tasks_values(
            page,
            date_begin,
            date_end,
            sortby,
            search,
            search_in,
            groupby,
            domain=self._get_portal_task_domain(),
        )

        pager = portal_pager(**values['pager'])
        grouped_tasks = values['grouped_tasks'](pager['offset'])

        values.update({
            'grouped_tasks': grouped_tasks,
            'pager': pager,
            'page_name': 'task',
            'task_count_total': values['pager']['total'],
        })

        return request.render('project_task_portal.portal_my_tasks', values)
