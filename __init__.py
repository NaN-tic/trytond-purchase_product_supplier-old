# This file is part purchase_product_supplier module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from . import product
from . import invoice


def register():
    Pool.register(
        product.ProductSupplier,
        invoice.InvoiceLine,
        module='purchase_product_supplier', type_='model')
