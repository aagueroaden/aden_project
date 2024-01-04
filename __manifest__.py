# -*- coding: utf-8 -*-
{
    'name': "aden_project",

    'summary': "Customized project base module to Aden nescesities",

    'description': """
Long description of module's purpose
    """,

    'author': "Agustin Aguero Aden",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'aden',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'aden_project_task_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'installable': True,

    'application': True,

    'auto_install': False,

}
