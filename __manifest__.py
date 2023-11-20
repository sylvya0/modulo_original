{
    'name': "basico",
    'summary': """modulo_basico""",
    'description': """
        realizando modulo basico
    """,
    'author': "silvia lazaro",
    'website': "https://zaragoza.salesianos.edu",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Examen',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views.xml',
    ],
}