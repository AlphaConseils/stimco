# -*- coding: utf-8 -*-

from odoo import models, fields

class ProductSupplierinfo(models.Model):
    _inherit = 'product.supplierinfo'

    brand = fields.Char()