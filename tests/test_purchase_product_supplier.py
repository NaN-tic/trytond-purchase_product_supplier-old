# This file is part of the purchase_product_supplier module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class PurchaseProductSupplierTestCase(ModuleTestCase):
    'Test Purchase Product Supplier module'
    module = 'purchase_product_supplier'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        PurchaseProductSupplierTestCase))
    return suite
