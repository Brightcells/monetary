# -*- coding: utf-8 -*-

import monetary
import pytest


class TestMonetaryCommands(object):
    def test_cent(self):
        assert monetary.cent(0.07) == 7

    def test_dollar(self):
        assert monetary.dollar(7) == 0.07
        assert monetary.dollar(314.15926, ndigits=2) == '3.14'

    def test_mul(self):
        assert monetary.mul(1, 0.95) == 0.95
        assert monetary.mul(1, 0.01) == 0.01

    def test_div(self):
        assert monetary.div(10, 2) == 5.0
        assert monetary.div(10, 2.0) == 5.0
        assert monetary.div(10, 2, cast_func=int) == 5
        assert monetary.div(10, 2.0, cast_func=int) == 5

    def test_cncurrency(self):
        assert monetary.cncurrency(0) == u'零圆整'
        assert monetary.cncurrency(10000) == u'壹万圆整'
        assert monetary.cncurrency(100000000) == u'壹亿圆整'
        assert monetary.cncurrency(1000000000000) == u'壹万亿圆整'
        assert monetary.cncurrency(1000000000000000) == u'壹仟万亿圆整'
        assert monetary.cncurrency(1111111111111) == u'壹万壹仟壹佰壹拾壹亿壹仟壹佰壹拾壹万壹仟壹佰壹拾壹圆整'
        assert monetary.cncurrency('0.11') == u'壹角壹分'
        assert monetary.cncurrency('0.01') == u'壹分'
        assert monetary.cncurrency('1.11') == u'壹圆壹角壹分'
        with pytest.raises(ValueError):
            assert monetary.cncurrency(10000000000000000)
