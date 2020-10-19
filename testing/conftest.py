import pytest
from pythoncode.calculator import Calculator
import os


@pytest.fixture(scope='module')
def get_calc():
    calc = Calculator()
    print('计算开始')
    yield calc
    print('计算结束')


def pytest_addoption(parser):
    parser.addoption("--env", action="store",
                     default='test',
                     help="选择不同环境的数据,env,dev,st")


@pytest.fixture(scope='session')
def get_env(request):
    os.environ['pytest_env'] = request.config.getoption("--env")
    print(os.environ['pytest_env'])