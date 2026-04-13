{
    'name': 'Real Estate Portal',
    'version': '1.0',
    'summary': 'Portal for Real Estate Management',
    'description': """
        Real Estate Portal Module
        =========================
        This module provides portal access for:
        - Clients to view their properties
        - Owners to manage their real estate
        - Real estate dashboard in portal
    """,
    'author': 'Mahmoud Shaker',
    'category': 'Real Estate',
    'license': 'LGPL-3',
    'depends': [
        'portal',
        'website',
        'app_one',
    ],
    'data': [

        'views/portal_menu.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            # 'real_estate_portal/static/src/css/style.css',
        ],
    },
    'installable': True,
    'application': False,
}