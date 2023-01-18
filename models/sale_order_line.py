# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    prepress_proof_id = fields.Many2one('prepress.proof', string='Prepress proof', readonly=False)
