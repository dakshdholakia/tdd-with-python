from src.string_calculator.string_calculator import add
import pytest

def test_string_input():
    assert add("") == 0


def test_string_input_four():
    assert add("4") == 4

def test_string_input_add():
    assert add("1,2") == 3

def test_string_input_add_arb():
    assert add("1,2,3,4,5,6,7,8,9") == 45

def test_newline_diff_sep():
    assert add("1\n2,3") == 6

def test_custom_sep():
    assert add("//;\n1;2") == 3

def test_neg_num():
    with pytest.raises(Exception) as exc:
        add("1,-2,-3")
    assert str(exc.value)