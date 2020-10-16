#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from pythoncode.calculator import Calculator


class TestCalc:
    def setup_class(self):
        print("计算开始")
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize('a,b,expect', [
        [1, 1, 2], [100, 1, 101], [0.1, 0.1, 0.2], [-1, -1, -2],
        [1, 0, 1], [0, 1, 1], [-1, 1, 0], [-100, -400, -500], [-500, 1000, 500]
    ], ids=['int_case', 'bignum_case', 'float_case', 'minus_case', 'zero_case',
    	"zero_int_case", "minus_int_case", "minus_bignum_case", "minus_bignum_int_case"
    ])
    def test_add(self, a, b, expect):
        # calc = Calculator()
        result = self.calc.add(a, b)
        assert result == expect

    @pytest.mark.parametrize('a, b, expect',[
	[1, 1, 1], [100, 2, 50], [0.8, 2, 0.4], [1.2, 0.1, 12], [-100, -2, 50], [10000, 100, 100],
	[15, 2, 7.5], [0, 10, 0]
    ], ids=[ 'int_case', 'int_bignum_case', 'float_case', 'float_float_case', 'minus_case', 'bignum_case',
    	'int_folat_case', 'zero_case'
    ])
    def test_div(self, a, b, expect):
          result = self.calc.div(a, b)
          assert result == expect
