# -*- coding: utf-8 -*-
from openerp.osv import fields, osv

class res_partner(osv.osv):
    _inherit = 'res.partner'

    _columns = {
        'bank_acc_number': fields.char('Nomor Rekening'),
        'bank_name': fields.char('Nama Cabang'),
        'bank_cheque_series': fields.char('No Seri Warkat'),
        'number_of_print': fields.integer('Number of print'),
    }
    
    _defaults = {
        'number_of_print': 1,
    }