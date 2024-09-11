from src.arithmetics.arithmetics import arithmetics

def test_brackets():
    assert arithmetics('((()()))') == 0

def test_invalid():
    assert arithmetics('())') == "Invalid record error"

def test_exp():
    assert arithmetics('( ( 4 * 5 )  )') == 20

def test_exp2():
    assert arithmetics('3 + ( 2 * 1 )') == "Invalid record error"

# def test_exp3():
#     assert arithmetics('( 1 + ( ( 2 + 3 ) * (4 * 5) ) )') == 101

