# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    siret = fields.Char(string='SIRET', size=14)
    ape = fields.Char(string='APE')

    @api.model
    def _get_user_currency(self):
        currency_id = self.env.ref('base.XPF')
        return super(ResCompany, self)._get_user_currency()
