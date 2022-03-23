# -*- coding: utf-8 -*-
{
    'name': "helpdesk ticket number",

    'summary': """
        unique identifiers for helpdesk tickets
    """,

    'description': """
        unique identifiers for helpdesk tickets
    """,

    'author': "Sergei Kataev",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Helpdesk',
    'version': '14.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': [
        'helpdesk',
    ],

    # always loaded
    'data': [
        'data/helpdesk_ticket_number.xml',
        'views/helpdesk_ticket_kanban_view.xml',
        'views/helpdesk_ticket_form_view.xml',
        'views/helpdesk_ticket_search_view.xml',
    ],
    'demo': [
    ],
    'post_init_hook': 'helpdesk_post_init_hook',
}
