# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'STIMCO Employees',
    'version': '1.1',
    'category': 'Human Resources/Employees',
    'sequence': 95,
    'summary': 'Centralize employee information',
    'website': 'https://www.nexources.com',
    'images': [
    ],
    'depends': [
        'hr',
    ],
    'data': [
        'views/hr_employee.xml'
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
