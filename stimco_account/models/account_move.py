# -*- coding: utf-8 -*-

from odoo import models, _
from odoo.exceptions import UserError


class AccountMove(models.Model):
    _inherit = 'account.move'

    def action_ssend_to_draft(self):
        if any(rec.show_reset_to_draft_button is False for rec in self):
            raise UserError(_('One of the invoices is already in draft state.'))
        self.filtered(
            lambda rec: rec.show_reset_to_draft_button).button_draft()