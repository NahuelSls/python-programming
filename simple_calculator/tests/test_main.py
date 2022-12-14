
from simple_calculator.main import SimpleCalculator
import pytest

def test_add_two_numbers():
    calculator = SimpleCalculator()

    result = calculator.add(10, 5)

    assert result == 15

def test_add_three_numbers():
    calculator = SimpleCalculator()

    result = calculator.add(4, 5, 6)

    assert result == 15

def test_add_many_numbers():
    numbers = range(100)

    calculator = SimpleCalculator()

    result = calculator.add(*numbers)

    assert result == 4950

def test_subtract_two_numbers():
    calculator = SimpleCalculator()

    result = calculator.sub(10, 3)

    assert result == 7

def test_subtract_two_numbers():
    numbers = range(5)
    calculator = SimpleCalculator()

    result = calculator.sub(*numbers)

    assert result == -10

def test_mul_two_numbers():
    calculator = SimpleCalculator()

    result = calculator.mul(6, 4)

    assert result == 24

def test_mul_many_numbers():
    numbers = range(1, 10)

    calculator = SimpleCalculator()

    result = calculator.mul(*numbers)

    assert result == 362880

def test_div_two_numbers():
    calculator = SimpleCalculator()

    result = calculator.div(13, 2)

    assert result == 6.5

def test_div_by_zero_returns_inf():
    calculator = SimpleCalculator()

    result = calculator.div(5, 0)

    assert result == float('inf')

def test_mul_by_zero_raises_exception():
    calculator = SimpleCalculator()

    with pytest.raises(ValueError):
        calculator.mul(3, 0)

def test_avg_correct_average():
    calculator = SimpleCalculator()

    result = calculator.avg([2, 5, 12, 98])

    assert result == 29.25

def test_avg_removes_upper_outliners():
    calculator = SimpleCalculator()

    result = calculator.avg([2, 5, 12, 98], ut = 90)

    assert result == pytest.approx(6.333333333)

def test_avg_removes_lower_outliners():
    calculator = SimpleCalculator()

    result = calculator.avg([2, 5, 12, 98], lt = 10)

    assert result == 55

def test_avg_upper_not_included():
    calculator = SimpleCalculator()

    result = calculator.avg([2, 5, 12, 98], ut = 12)

    assert result == pytest.approx(6.33333)

def test_avg_lower_not_included():
    calculator = SimpleCalculator()

    result = calculator.avg([2, 5, 12, 98], lt = 5)

    assert result == pytest.approx(38.333333)

def test_avg_empty_list():
    calculator = SimpleCalculator()

    result = calculator.avg([])

    assert result == 0 #commit




