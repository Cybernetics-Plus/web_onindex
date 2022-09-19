# -*- coding: utf-8 -*-
###################################################################################
#
#    Cybernetics Plus Co., Ltd.
#    Website NoIndex
#
###################################################################################

{
    'name': 'Cybernetics NoIndex',
    'version': '15.0.0.1.1',
    'summary': """ 
            Website NoIndex
            .""",
    'description': """ 
            Website NoIndex
            .""",
    'author': 'Cybernetics Plus Co., Ltd.',
    'website': 'https://www.cybernetics.plus',
    'live_test_url': 'https://www.cybernetics.plus',
    'images': ['static/description/banner.png'],
    'category': 'Website',
    'license': 'AGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
    'contributors': [
        'Developer <dev@cybernetics.plus>',
    ],
    'depends': [
        'web',
    ],
    'data': [
        'views/noindex.xml',
    ],
}