# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields
from trytond.pool import Pool, PoolMeta


__all__ = ['InvoiceLine']
__metaclass__ = PoolMeta


class InvoiceLine:
    __name__ = 'account.invoice.line'
    supplier_reference = fields.Function(fields.Char('Supplier Reference'),
        'on_change_with_supplier_reference')

    @fields.depends('origin')
    def on_change_with_supplier_reference(self, name=None):
        PurchaseLine = Pool().get('purchase.line')
        if self.origin and isinstance(self.origin, PurchaseLine().__class__):
            return self.origin.purchase.supplier_reference
