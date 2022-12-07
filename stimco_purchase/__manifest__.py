# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'STIMCO Purchase',
    'version': '1.2',
    'category': 'Inventory/Purchase',
    'sequence': 35,
    'summary': 'Purchase orders, tenders and agreements',
    'website': 'https://www.nexources.com/',
    'depends': ['purchase'],
    'data': [
        'views/product_supplierinfo_views.xml'
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
