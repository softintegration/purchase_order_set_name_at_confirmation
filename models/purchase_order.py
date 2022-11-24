# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals.update({'name':'/'})
        return super(PurchaseOrder, self).create(vals)

    def button_confirm(self):
        res = super(PurchaseOrder, self).button_confirm()
        for order in self:
            if order.name == '/':
                self_comp = self.with_company(order.company_id)
                seq_date = None
                if order.date_order:
                    seq_date = fields.Datetime.context_timestamp(self, fields.Datetime.to_datetime(order.date_order))
                order.name = self_comp.env['ir.sequence'].next_by_code('purchase.order',sequence_date=seq_date) or '/'
        return res