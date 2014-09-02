#This file is part purchase_product_supplier module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.pool import Pool
from .product import *

def register():
    Pool.register(
        ProductSupplier,
        module='purchase_product_supplier', type_='model')
