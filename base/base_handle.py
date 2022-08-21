# 后续需要加上装饰器的东西


import logging
import os.path
# 声明一个黑名单
import allure
def black_wrapper(fun):
    def run(*args, **kwargs):
        # from base.Base import Base
        Base = args[0]
        try:
            # logging.info("开始查找元素：{args[2]}")
            print(args[0])
            print(args[1])
            print(args[2])
            print('1111111111111')
            return fun(*args, **kwargs)
        except Exception as e:
            logging.warning("未找到元素，处理导演 ")
            # 以当前时间命名的 截图
            curtime = Base.get_time()
            tmp_name = curtime + ".png"
            # 当前black_handle.py所在的路径
            logging.info("当前保存图片的路径 >>>" + os.path.dirname(__file__))
            # 找到images 路径 ，拼接图片名称
            tmp_path = os.path.join(os.path.dirname(__file__), "..", "images", tmp_name)
            Base.screenshot(tmp_path)
            allure.attach.file(tmp_path, name="查找截图", attachment_type=allure.attachment_type.PNG)
            raise e

    return run
