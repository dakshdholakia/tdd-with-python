from src.stack_kata.stack_kata import Stack


def test_push():
    l1 = []             # arrange
    st = Stack(l1)      # arrange
    pu = st.push(4)     # act
    assert pu[0] == 4

def test_pop():
    l1 = [4]          # arrange
    st = Stack(l1)    # arrange
    po = st.pop()
    assert len(po) == 0
    assert len(l1) == 0


def test_empty():
    l1 = []          # arrange
    st = Stack(l1)    # arrange
    em = st.is_empty()
    assert em == True


def test_is_not_empty():
    l1 = [4]          # arrange
    st = Stack(l1)    # arrange
    em = st.is_empty()
    assert em == False

def test_size():
    l1 = [4,3,2,1]
    st = Stack(l1)
    si = st.list_size()
    assert si == 4

def test_peek():
    l1 = [2, 4]
    st = Stack(l1)
    pe = st.peek()
    assert pe == 2