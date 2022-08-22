

def logger(func):
    def wrapper(*args, **kw):
        print('我准备开始执行：{} 函数了:'.format(func.__name__))

        # 真正执行的是这行
        return func(*args, **kw)

        print('我执行完啦')

        print('hhhhh')

    return wrapper