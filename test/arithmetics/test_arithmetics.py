from src.arithmetics.arithmetics import arithmetics


def test_brackets():
    assert arithmetics('((()()))') == 0
