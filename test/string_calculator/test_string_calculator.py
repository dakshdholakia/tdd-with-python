from src.string_calculator.string_calculator import add

def test_string_input():
    assert add("") == 0


def test_string_input_four():
    assert add("4") == 4

def test_string_input_add():
    assert add("1,2") == 3