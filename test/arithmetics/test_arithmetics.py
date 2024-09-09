from src.arithmetics.arithmetics import arithmetics


def test_brackets():
    assert arithmetics('((()()))') == 0

def test_invalid():
    assert arithmetics('())') == "Invalid record error"

def test_exp():
    assert arithmetics('( ( 4 * 5 )  )') == 20