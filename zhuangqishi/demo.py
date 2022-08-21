from zhuangqishi.ceshi import logger
# 目前感觉是因为不在同一个文件，所以装饰器中需要返回，还没有真正的弄明白
@logger
def add(x, y):
    # print('{} + {} = {}'.format(x, y, x+y))
    a = x+y
    return a

b = add(10,20)
print(b)
