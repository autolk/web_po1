# def pytest_runtest_setup(item):
#     print('11111')

# 修改编码格式
def pytest_collection_modifyitems(session, config, items):
    print(items)
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')