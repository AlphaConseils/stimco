# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'STIMCO Inventory',
    'version': '1.1',
    'summary': 'Manage your stock and logistics activities',
    'website': 'http://www.nexources.com/',
    'depends': ['stock'],
    'category': 'Inventory/Inventory',
    'sequence': 25,
    'data': [
        'report/stock_report_views.xml',
        'report/report_delivery_document.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
