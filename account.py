#The COPYRIGHT file at the top level of this repository contains the full
#copyright notices and license terms.
from sql import Table
from trytond.model import fields
from trytond.pool import Pool, PoolMeta
from trytond import backend
from trytond.transaction import Transaction

__all__ = ['Account', 'Type']


class Account:
    __metaclass__ = PoolMeta
    __name__ = 'account.account'

    @classmethod
    def __setup__(cls):
        super(Account, cls).__setup__()
        value = ('efective', 'Efective')
        if not value in cls.kind.selection:
            cls.kind.selection.append(value)

    @classmethod
    def __register__(cls, module_name):
        pool = Pool()
        TableHandler = backend.get('TableHandler')
        cursor = Transaction().connection.cursor()
        model_data = Table('ir_model_data')
        model_field = Table('ir_model_field')
        sql_table = cls.__table__()

        # pgc_pymes_176_child
        # pgc_pymes_255_child
        # pgc_pymes_663_child
        # pgc_pymes_763_child
        cursor.execute(*model_data.update(
                columns=[model_data.fs_id],
                values=['pgc_pymes_1765_child'],
                where=((model_data.fs_id == 'pgc_pymes_176_child')
                & (model_data.module == module_name))))
        cursor.execute(*model_data.update(
                columns=[model_data.fs_id],
                values=['pgc_pymes_2550_child'],
                where=((model_data.fs_id == 'pgc_pymes_255_child')
                & (model_data.module == module_name))))
        cursor.execute(*model_data.update(
                columns=[model_data.fs_id],
                values=['pgc_pymes_6630_child'],
                where=((model_data.fs_id == 'pgc_pymes_663_child')
                & (model_data.module == module_name))))
        cursor.execute(*model_data.update(
                columns=[model_data.fs_id],
                values=['pgc_pymes_7630_child'],
                where=((model_data.fs_id == 'pgc_pymes_763_child')
                & (model_data.module == module_name))))

        super(Account, cls).__register__(module_name)


class Type:
    __metaclass__ = PoolMeta
    __name__ = 'account.account.type'

    @classmethod
    def __register__(cls, module_name):
        pool = Pool()
        TableHandler = backend.get('TableHandler')
        cursor = Transaction().connection.cursor()
        model_data = Table('ir_model_data')
        model_field = Table('ir_model_field')
        sql_table = cls.__table__()

        # es_balance_pymes_12380
        # es_balance_pymes_12381
        # es_balance_pymes_12382
        # es_balance_pymes_12390
        # es_balance_pymes_31290
        # es_balance_pymes_32580
        # es_balance_pymes_32581
        # es_balance_pymes_32582
        # es_balance_pymes_32590
        cursor.execute(*model_data.update(
                columns=[model_data.fs_id],
                values=['es_balance_pymes_12310'],
                where=((model_data.fs_id == 'es_balance_pymes_12380')
                & (model_data.module == module_name))))
        cursor.execute(*model_data.update(
                columns=[model_data.fs_id],
                values=['es_balance_pymes_12311'],
                where=((model_data.fs_id == 'es_balance_pymes_12381')
                & (model_data.module == module_name))))
        cursor.execute(*model_data.update(
                columns=[model_data.fs_id],
                values=['es_balance_pymes_12312'],
                where=((model_data.fs_id == 'es_balance_pymes_12382')
                & (model_data.module == module_name))))
        cursor.execute(*model_data.update(
                columns=[model_data.fs_id],
                values=['es_balance_pymes_12330'],
                where=((model_data.fs_id == 'es_balance_pymes_12390')
                & (model_data.module == module_name))))
        cursor.execute(*model_data.update(
                columns=[model_data.fs_id],
                values=['es_balance_pymes_31250'],
                where=((model_data.fs_id == 'es_balance_pymes_31290')
                & (model_data.module == module_name))))
        cursor.execute(*model_data.update(
                columns=[model_data.fs_id],
                values=['es_balance_pymes_32510'],
                where=((model_data.fs_id == 'es_balance_pymes_32580')
                & (model_data.module == module_name))))
        cursor.execute(*model_data.update(
                columns=[model_data.fs_id],
                values=['es_balance_pymes_32511'],
                where=((model_data.fs_id == 'es_balance_pymes_32581')
                & (model_data.module == module_name))))
        cursor.execute(*model_data.update(
                columns=[model_data.fs_id],
                values=['es_balance_pymes_32512'],
                where=((model_data.fs_id == 'es_balance_pymes_32582')
                & (model_data.module == module_name))))
        cursor.execute(*model_data.update(
                columns=[model_data.fs_id],
                values=['es_balance_pymes_32530'],
                where=((model_data.fs_id == 'es_balance_pymes_32590')
                & (model_data.module == module_name))))

        super(Type, cls).__register__(module_name)

