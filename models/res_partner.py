# -*- coding: utf-8 -*-
from openerp.osv import fields, osv
from openerp import tools

import logging
_logger = logging.getLogger(__name__)

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
    
    def direct_print_cheque_book(self, cr, uid, ids, context=None):
        try:
            import win32api
            import tempfile
            import os
            pdf = self.pool.get('report').get_pdf(cr, uid, ids, 'mplus_cheque.report_cheque_book', context=context)
            f = tempfile.NamedTemporaryFile(suffix='.pdf', delete=False)
            f.write(pdf)
            f.close()
            win32api.ShellExecute(0, "print", f.name, None,  ".",  0)
            #os.unlink(f.name)  #TO DO: wait print process to finish before printing
        except Exception, ex:
            _logger.info('Could not print: %s', tools.ustr(ex))
        return {
            'type': 'ir.actions.client',
            'tag': 'reload'
        }