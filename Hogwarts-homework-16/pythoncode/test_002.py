import pytest
import yaml
# @pytest.fixture()
def myfixture():
    print("执行myfixture")

class Test_firstFile():
    @pytest.mark.lva
    @pytest.mark.parametrize("a,b,c",yaml.safe_load(open("./data.yml"))["datas"],
                             ids=yaml.safe_load(open("./data.yml"))["myids"])
    def test_one(self,a,b,c):
        print("执行test_one,用例级别1")
        assert a+b==c
    @pytest.mark.lv2
    def test_two(self,myfixture):
        print("执行test_two，用例级别2")
        assert 1==1
    @pytest.mark.lv3
    def test_three(self):
        print("执行test_three，案例级别3")
        assert 1+1==2