import pytest
from calculator import Calculator
from cofig_class import Test_config
import yaml



class TestCalc:
    @pytest.mark.run(order=4)   #��������ִ��˳��
    @pytest.mark.add_demo   #��ӱ�ǩ
    @pytest.mark.parametrize("a, b, expected", Test_config().get_data()[0], ids=Test_config().get_data()[2])
    def test_add(self, a, b, expected, myfixture):
        assert expected == Calculator().add(a, b)

    @pytest.mark.run(order=2)
    @pytest.mark.sub_demo
    @pytest.mark.parametrize("a, b, expected", Test_config().get_data()[1], ids=Test_config().get_data()[2])
    def test_sub(self, a, b, expected, myfixture):
        assert expected == Calculator().sub(a, b)

    @pytest.mark.run(order=3)
    @pytest.mark.mun_demo
    @pytest.mark.parametrize("a, b, expected", Test_config().get_data()[3], ids=Test_config().get_data()[2])
    def test_mun(self, a, b, expected, myfixture):
        assert expected == Calculator().mun(a, b)

    @pytest.mark.run(order=1)
    @pytest.mark.div_demo
    @pytest.mark.parametrize("a, b, expected", Test_config().get_data()[4], ids=Test_config().get_data()[2])
    def test_div(self, a, b, expected, myfixture):
        assert expected == Calculator().div(a, b)