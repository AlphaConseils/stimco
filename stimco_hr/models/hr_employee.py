# -*- coding: utf-8 -*-

from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    cnaps_number = fields.Char()
    cin_number = fields.Char()
    issue_date = fields.Char()
    issue_place = fields.Char()