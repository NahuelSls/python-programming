from simple_calculator.main import SimpleCalculator

def test_add_two_numbers():
    calculator = SimpleCalculator()

    result = calculator.add(10, 5)

    assert result == 15