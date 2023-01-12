# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'STIMCO Sales',
    'version': '1.2',
    'category': 'Sales/Sales',
    'summary': 'Sales internal machinery',
    'description': """
This module contains all the common features of Sales Management and eCommerce.
    """,
    'depends': [
        'sale',
    ],
    'data': [
        'report/report_saleorder_document.xml',
    ],
    'installable': True,
    'license': 'LGPL-3',
}
