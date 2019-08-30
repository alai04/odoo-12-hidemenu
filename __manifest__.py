# -*- coding: utf-8 -*-
{
    'name': "Hidemenu",

    'summary': "Hide Discuss, Calendar and Contacts for users",

    'description': """
        对一般用户隐藏"讨论"、"日历"和"联系人"菜单，菜单只对 group_hide_menus 组中的成员可见。
    """,

    'author': "Albert Lai",
    'website': "http://www.alai04.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['mail', 'calendar', 'contacts'],

    # always loaded
    'data': [
        'security/hidemenus.xml',
        'views/res_config_settings_view.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}