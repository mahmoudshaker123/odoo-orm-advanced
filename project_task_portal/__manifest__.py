{
    'name': 'Project Task Portal',
    'version': '1.0.1',
    'category': 'Project',
    'depends': ['project', 'portal', 'website'],
    'data': [
        'views/portal_templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'project_task_portal/static/src/css/portal.css',
            'project_task_portal/static/src/js/portal.js',
        ],
    },
    'installable': True,
}
