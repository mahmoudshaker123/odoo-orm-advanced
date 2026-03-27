{
    'name': 'Equipment Category',
    'version': '18.0',
    'summary': '',
    'depends': ['base','stock','purchase',],
    'data': [
        'security/ir.model.access.csv',
        'views/eq_category_views.xml',
        'views/product_template_inherit_views.xml',
        'views/purchase_order_inherit_views.xml',

    ],
    'application': False,
}
