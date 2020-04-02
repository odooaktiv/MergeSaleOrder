# -*- coding: utf-8 -*-

{
    'name': 'Merge Sale Order',
    'category': 'Sales',
    'summary': 'This module will merge sale order.',
    'version': '10.0.1.0.1',
    'website': 'http://www.aktivsoftware.com',
    'author': 'Aktiv Software',
    'license': 'AGPL-3',
    'description': 'Merge Sale Order',

    'depends': [
        'sale'
    ],

    'data': [
        'wizard/merge_sale_order_wizard_view.xml',
    ],
    'images': ['static/description/banner.jpg'],
    'auto_install': False,
    'installable': True,
    'application': False

}
