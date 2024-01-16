# -*- coding: utf-8 -*-
{
    'name': "Aden - Proyectos",

    'summary': "Customized project module for Aden Business School",

    'description': "Customized project module for Aden Business School",

    'author': "Aden Business School",

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
        'views/aden_project_task_views.xml',
        'views/aden_teams_views.xml',
        'views/aden_project_project_views.xml',
        'views/aden_resources_views.xml',
        'views/aden_category_views.xml',
        'views/aden_subcategory_views.xml',
    ],

    'installable': True,

    'application': True,

    'auto_install': False,

    'license': 'LGPL-3',

}
