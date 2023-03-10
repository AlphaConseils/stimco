# -*- coding: utf-8 -*-

from odoo import models, api, _
from odoo.exceptions import AccessDenied


class ResPartner(models.Model):
    """Only user in contact_create_write_group can write/create."""

    _inherit = "res.partner"

    @api.model
    def create(self, vals):
        self.check_create_write_access_right()
        return super(ResPartner, self).create(vals)

    def write(self, vals):
        self.check_create_write_access_right()
        return super(ResPartner, self).write(vals)

    @api.model
    def check_create_write_access_right(self):
        if not self.env.user.has_group("stimco_security.partner_create_write_group"):
            raise AccessDenied(
                _(
                    "The requested operation cannot be completed due to security restrictions.(Create/Write Contact)."
                )
            )
