# -*- coding: utf-8 -*-

from odoo import models, api, _
from odoo.exceptions import AccessDenied


class ProductProduct(models.Model):
    _inherit = "product.product"

    @api.model
    def create(self, vals):
        """Only user in product_create_write_group can write/create."""
        self.check_create_write_access_right()
        return super(ProductProduct, self).create(vals)

    def write(self, vals):
        """Only user in product_create_write_group can write/create."""
        self.check_create_write_access_right()
        return super(ProductProduct, self).write(vals)

    @api.model
    def check_create_write_access_right(self):
        """Only user in product_create_write_group can write/create."""
        if not self.env.user.has_group("stimco_security.product_create_write_group"):
            raise AccessDenied(
                _("The requested operation cannot be completed due to security restrictions.(Create/Write Product).")
            )
