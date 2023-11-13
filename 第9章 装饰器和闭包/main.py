# 装饰器通常会把一个函数替换成另外一个函数
def deco(func):
    def inner():
        print('running inner()')
    return inner

@deco
def target():
    print(f'running target()')

target()