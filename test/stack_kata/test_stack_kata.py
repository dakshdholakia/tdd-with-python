from src.stack_kata.stack_kata import Stack


def test_push():
    l1 = []             # arrange
    st = Stack(l1)      # arrange
    p1 = st.push(4)     # act
    assert p1[0] == 4

def test_pop():
    l1 = [4]          # arrange
    st = Stack(l1)    # arrange
    p1 = st.pop()
    assert len(p1) == 0
    assert len(l1) == 0