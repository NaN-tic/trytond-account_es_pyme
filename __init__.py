#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
from trytond.pool import Pool
from . import account
from . import currency
from . import tax


def register():
    Pool.register(
        account.Account,
        account.Type,
        account.FiscalYear,
        account.Period,
        currency.Currency,
        tax.Tax,
        tax.TaxTemplate,
        module='account_es_pyme', type_='model')
