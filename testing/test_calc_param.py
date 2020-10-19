#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import yaml


# 解析测试数据
def get_test_data():
    with open('./datas/calc.yml', encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        add_datas = datas['calc']['add']['data']
        add_ids = datas['calc']['add']['ids']
        div_datas = datas['calc']['div']['data']
        div_ids = datas['calc']['div']['ids']
        sub_datas = datas['calc']['sub']['data']
        sub_ids = datas['calc']['sub']['ids']
        mul_datas = datas['calc']['mul']['data']
        mul_ids = datas['calc']['mul']['ids']
    return [add_datas, add_ids, div_datas, div_ids, sub_datas, sub_ids, mul_datas, mul_ids]


class TestCalc:
    @pytest.mark.parametrize('a,b,expect', get_test_data()[0], ids=get_test_data()[1])
    def test_add(self, get_calc, a, b, expect):
        result = get_calc.add(a, b)
        assert result == expect

    @pytest.mark.parametrize('a, b, expect', get_test_data()[2], ids=get_test_data()[3])
    def test_div(self, get_calc, a, b, expect):
          result = get_calc.div(a, b)
          if type(result) == float:
              assert round(result, 2) == expect
          else:
              assert result == expect

    @pytest.mark.parametrize('a,b,expect', get_test_data()[4], ids=get_test_data()[5])
    def test_sub(self, get_calc, a, b, expect):
        result = get_calc.sub(a, b)
        assert result == expect

    @pytest.mark.parametrize('a, b, expect', get_test_data()[6], ids=get_test_data()[7])
    def test_mul(self, get_calc, a, b, expect):
        result = get_calc.mul(a, b)
        if type(result) == float:
            assert round(result, 2) == expect
        else:
            assert result == expect
