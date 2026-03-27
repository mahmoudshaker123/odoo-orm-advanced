{
    'name': 'ORM Training',
    'version': '18.0',
    'summary': 'Module to practice Odoo ORM methods',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/task_report_wizard_view.xml',

        'views/task_views.xml',
        'views/category_views.xml',
        'views/menus.xml',
    ],
    'application': True,
}
