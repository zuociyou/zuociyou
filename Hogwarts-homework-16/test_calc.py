
import pytest
from pythoncode.calculator import Calculator
import json

class TestCalc:
    def setup_class(self):
        self.calc = Calculator()
        print("开始计算")

    def teardown_class(self):
        print("结束计算")

    @pytest.mark.parametrize("a,b,expect", [
        (3, 5, 8), (-1, -2, -3), (100, 300, 400)
    ], ids=["int", "minus", "bigint"])
    def test_add(self, a, b, expect):
        assert expect == self.calc.add(a, b)
    @pytest.mark.parametrize("a, b, expect",
                             [(5, 2, 3), (-1, -2, 1), (0, 300, -300)],
                             ids=["zhengshuxiangjian", "fushuxiangjian", "zhengshuhefushujisuan"])
    def test_sub(self, a, b, expect):
        assert expect == self.calc.sub(a, b)

    @pytest.mark.parametrize("a, b, expect", [(3, 5, 15), (-1, -2, 2), (-1, 2, -2)])
    def test_mul(self, a, b, expect):
        assert expect == self.calc.mul(a, b)

    @pytest.mark.parametrize("a, b, expect", [(4, 2, 2), (-2, -2, 1), (2, -2, -1)])
    def test_div(self, a, b, expect):
        assert expect == self.calc.div(a, b)