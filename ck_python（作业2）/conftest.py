import pytest

@pytest.fixture(scope='module')

def myfixture():
    print("\n用例开始前运行fixture")
    yield
    print("\n用例结束时执行")

    #修改编码方式（使pytest运行可以正常输出中文）
def pytest_collection_modifyitems(session, config, items):
    print(type(items)) #查看items是什么格式

    #items.reverse() #列表反转，用例会倒序执行
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

    #查看pytest_collection_modifyitems 函数的参数
    print("items是: %s" %items)
    print("session是: %s" %session)
    print("config是: %s" %config)