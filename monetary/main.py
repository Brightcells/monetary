# -*- coding: utf-8 -*-

from __future__ import division

from decimal import Decimal


class Monetary(object):
    def decimal(self, value):
        """
        In [1]: Decimal(3.14)
        Out[1]: Decimal('3.140000000000000124344978758017532527446746826171875')

        In [2]: Decimal(str(3.14))
        Out[2]: Decimal('3.14')
        """
        return Decimal(str(value))

    def mul(self, multiplicand, multiplicator, cast_func=float):
        """
        8 × 3 = 24, 8 is multiplicand, 3 is multiplicator.
        """
        return cast_func(self.decimal(multiplicand) * self.decimal(multiplicator))

    def div(self, dividend, divisor, cast_func=float):
        """
        24 ÷ 8 = 3, 24 is dividend, 8 is divisor.
        """
        return cast_func(self.decimal(dividend) / self.decimal(divisor))

    def cent(self, dollar, rate=100, cast_func=int):
        """
        Exchange Dollar into Cent

        In [1]: 0.07 * 100
        Out[1]: 7.000000000000001

        :param dollar:
        :param rate:
        :return:
        """
        return self.mul(dollar, rate, cast_func=cast_func)

    def dollar(self, cent, rate=100, cast_func=float):
        """
        Exchange Cent into Dollar

        :param cent:
        :param rate:
        :return:
        """
        return self.div(cent, rate, cast_func=cast_func)


_global_instance = Monetary()
decimal = _global_instance.decimal
cent = Fen = dollar2cent = Yuan2Fen = _global_instance.cent
dollar = Yuan = cent2dollar = Fen2Yuan = _global_instance.dollar
mul = _global_instance.mul
div = _global_instance.div
