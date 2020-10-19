#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import yaml
import os


# 解析测试数据
def get_test_data():
    # if os.environ['pytest_env'] == 'test':
    #     data_file = './datas/calc_env_test.yml'
    # elif os.environ['pytest_env'] == 'dev':
    #     data_file = './datas/calc_env_dev.yml'
    # elif os.environ['pytest_env'] == 'st':
    #     data_file = './datas/calc_env.yml'
    # else:
    #     data_file = './datas/calc.yml'
    # print(os.environ['pytest_env'])
    data_file = './datas/calc.yml'
    with open(data_file, encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        add_datas = datas['calc']['add']['data']
        add_ids = datas['calc']['add']['ids']
    return [add_datas, add_ids]


class TestCalc:
    @pytest.mark.hogwarts
    @pytest.mark.parametrize('a,b,expect', get_test_data()[0], ids=get_test_data()[1])
    def test_add(self, get_calc, a, b, expect, get_env):
        # print(os.environ['pytest_env'])
        result = get_calc.add(a, b)
        assert result == expect

    @pytest.mark.hogwarts
    def test_add_env(self, get_calc, get_env):
        if os.environ['pytest_env'] == 'test':
            data_file = './datas/calc_env_test.yml'
        elif os.environ['pytest_env'] == 'dev':
            data_file = './datas/calc_env_dev.yml'
        elif os.environ['pytest_env'] == 'st':
            data_file = './datas/calc_env.yml'
        else:
            data_file = './datas/calc.yml'
        with open(data_file, encoding='utf-8') as f:
            datas = yaml.safe_load(f)
            add_datas = datas['calc']['add']['data']
        for data in add_datas:
            result = get_calc.add(data[0], data[1])
            assert result == data[2]


