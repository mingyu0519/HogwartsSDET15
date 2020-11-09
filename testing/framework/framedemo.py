import importlib


# 动态导入
def dynamic():
    tmp = 'hello.a'.split(".")
    c = importlib.import_module(tmp[0])
    getattr(c, tmp[1])()


# 保存全局变量
def set_env():
    globals()['a'] = 'globals_a'
    print(globals()['a'])


# 字符串当作python代码执行
def str2cmd():
    print(eval('1+1'))


if __name__ == '__main__':
    dynamic()