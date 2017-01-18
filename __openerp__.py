# -*- coding: utf-8 -*-
{
    'name': "Mplus Cheque",
    'summary': """
        Print cheque book
    """,
    'description': """
        Print cheque book
    """,
    'author': "Mplus Software",
    'website': "http://mplus.software",
    'category': 'CRM',
    'version': '1.0',
    'depends': ['report'],
    'data': [
        'data/mplus_cheque_data.xml',
        'views/mplus_cheque_report.xml',
        'views/res_partner_view.xml',
        'views/report_cheque_book.xml',
    ],
}