# -*- coding: utf-8 -*-

import monetary


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
