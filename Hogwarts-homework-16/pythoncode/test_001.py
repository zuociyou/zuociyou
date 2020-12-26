import pytest
import yaml
def add_function(a,b):
    return a+b
@pytest.mark.parametrize("a,b,expected",
                         yaml.safe_load(open("./data.yml"))["datas"],
                         ids=yaml.safe_load(open("./data.yml"))["myid"])
def test_add1(a,b,expected):
    assert add_function(a,b) == expected