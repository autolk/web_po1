# def pytest_runtest_setup(item):
#     print('11111')
import os
import time
import pytest
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 修改编码格式/这个方法针对的是hook_fun.py中的方法
def pytest_collection_modifyitems(session, config, items):
    print(items)
    for item in items:
        print(item.name)
        print(item._nodeid)
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

# pytest 可以直接获取 rootdir 路径
# def get_rootdir(request):
#     # 根目录
#     rootdir = request.config.rootdir
#     return rootdir
#
#
# @pytest.fixture(scope="session", autouse=True)
# def manage_logs(request):
#     """Set log file name same as test name"""
#     now = time.strftime("%Y-%m-%d%H-%M-%S")
#     log_name = 'logs/' + now + '.logs'
#
#     request.config.pluginmanager.get_plugin("logging-plugin") \
#         .set_log_path(os.path.join(get_rootdir(request), log_name))

