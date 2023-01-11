# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class AccountMove(models.Model):
    _inherit = 'account.move'

    journal_id = fields.Many2one(required=False, default=False)

    @api.constrains('move_type', 'journal_id')
    def _check_journal_move_type(self):
        """ DELETE JOURNAL CONSTRAINT *** LEAVE ME ALONE. """
        pass

    @api.depends('move_type')
    def _compute_journal_id(self):
        """ DELETE JOURNAL DEFAULT VALUE *** LEAVE ME ALONE. """
        pass

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    @api.onchange('product_id')
    def _sti_onchange_product_id(self):
        if not self.move_id.currency_id.id:
            raise UserError(_('Please set currency first!'))