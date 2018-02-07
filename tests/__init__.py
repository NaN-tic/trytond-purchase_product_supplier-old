# This file is part purchase_product_supplier module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
try:
    from trytond.modules.purchase_product_supplier.tests.test_purchase_product_supplier import suite
except ImportError:
    from .test_purchase_product_supplier import suite

__all__ = ['suite']
