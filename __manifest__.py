# -*- coding: utf-8 -*-
{
    'name': "Hidemenu",

    'summary': "Hide Discuss and Calendar for users",

    'description': """
        对一般用户隐藏"讨论"和"日历"菜单，菜单只对 group_hide_menus 组中的成员可见。
    """,

    'author': "Albert Lai",
    'website': "http://www.alai04.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['mail', 'calendar'],

    # always loaded
    'data': [
        'security/hidemenus.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}