from odoo import api, SUPERUSER_ID


def helpdesk_post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    env['helpdesk.ticket'].init_hook()
