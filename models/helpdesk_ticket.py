from odoo import fields, models, api


class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    ticket_number = fields.Char(string="Ticket Number", required=True, readonly=True, default='New', edit=False)

    @api.model
    def create(self, vals):
        if vals.get('ticket_number', 'New') == 'New':
            vals['ticket_number'] = self.env['ir.sequence'].next_by_code('helpdesk.ticket.number') or 'New'
        return super(HelpdeskTicket, self).create(vals)

    def name_get(self):
        names = []
        for ticket in self:
            names.append((ticket.id, "[{0}] - {1}".format(ticket.ticket_number, ticket.name)))
        return names

    def name_search(self, name='', args=None, operator='ilike', limit=100):
        args = list(args or [])
        domain = ['|', ('name', 'ilike', name), ('ticket_number', 'ilike', name)]
        return super(HelpdeskTicket, self).search(args=args + domain, limit=limit).get_name()

    @api.model
    def init_hook(self):
        ticket_number = 1
        for rec in self.search([], order='id asc'):
            rec.ticket_number = ticket_number
            ticket_number += 1
        self.env["ir.sequence"].search([('code', '=', 'helpdesk.ticket.number')]).write({'number_next': ticket_number})
