# -*- coding: utf-8 -*-

from __future__ import division

import warnings
from decimal import Decimal


class Monetary(object):
    def keep_ndigits(self, value, ndigits=2):
        return '%.{}f'.format(ndigits) % value

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

    def div(self, dividend, divisor, cast_func=float, ndigits=None):
        """
        24 ÷ 8 = 3, 24 is dividend, 8 is divisor.
        """
        result = cast_func(self.decimal(dividend) / self.decimal(divisor))
        return self.keep_ndigits(result, ndigits=ndigits) if ndigits else result

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

    def dollar(self, cent, rate=100, cast_func=float, ndigits=None):
        """
        Exchange Cent into Dollar

        :param cent:
        :param rate:
        :return:
        """
        return self.div(cent, rate, cast_func=cast_func, ndigits=ndigits)

    def cncurrency(self, value, classical=True, prefix=False):
        """
        classical:  True   圆
                    False  元
        prefix:     True   以'人民币'作为前缀
                    False, 无前缀
        """
        # 浮点数精度提示
        if not isinstance(value, (Decimal, str, int)):
            msg = """
    由于浮点数精度问题，请考虑使用字符串，或者 decimal.Decimal 类。
    因使用浮点数造成误差而带来的可能风险和损失作者概不负责。
            """
            warnings.warn(msg, UserWarning)
        # 转换为 Decimal，并截断多余小数
        if not isinstance(value, Decimal):
            value = Decimal(value).quantize(Decimal('.01'))
        if value == 0:
            return u'零圆整' if classical else u'零元整'
        s = ''
        # 处理前缀
        if prefix:
            s == u'人民币'
        # 处理负数
        if value < 0:
            s += u'负'  # 输出前缀，加负
            value = -value  # 取正数部分，无须过多考虑正负数舍入
        # 转化为字符串
        absv = str(value)
        if len(absv) > 19:
            raise ValueError(u'金额太大了，不知道该怎么表达。')
        istr, dstr = absv.split('.')  # 整数部分、小数部分分别处理
        # 汉字金额字符定义
        digits = [u'零', u'壹', u'贰', u'叁', u'肆', u'伍', u'陆', u'柒', u'捌', u'玖']
        iunits = [u'圆', u'拾', u'佰', u'仟', u'万', u'拾', u'佰', u'仟', u'亿', u'拾', u'佰', u'仟', u'万', u'拾', u'佰', u'仟']
        zeros = [(u'零仟', u'零佰', u'零拾', u'零零零', u'零零', u'零万', u'零亿', u'亿万', u'零圆'), (u'零', u'零', u'零', u'零', u'零', u'万', u'亿', u'亿', u'圆')]
        dunits = [u'角', u'分']
        # 处理整数部分
        if istr != '0':
            for i, x in enumerate(istr):
                s += '%s%s' % (digits[int(x)], iunits[len(istr) - i - 1])
            for z1, z2 in zip(zeros[0], zeros[1]):
                s = s.replace(z1, z2)
            # 整
            if dstr == '00':
                s += u'整'
        # 处理小数部分
        if dstr[0] != '0':
            s += '%s%s' % (digits[int(dstr[0])], dunits[0])
        if dstr[1] != '0':
            s += '%s%s' % (digits[int(dstr[1])], dunits[1])
        # YUAN替换
        if not classical:
            s = s.replace(u'圆', u'元')
        return s


_global_instance = Monetary()
decimal = _global_instance.decimal
cent = Cent = fen = Fen = dollar2cent = Dollar2Cent = yuan2fen = Yuan2Fen = _global_instance.cent
dollar = Dollar = yuan = Yuan = cent2dollar = Cent2Dollar = fen2yuan = Fen2Yuan = _global_instance.dollar
mul = _global_instance.mul
div = _global_instance.div
cncurrency = _global_instance.cncurrency
