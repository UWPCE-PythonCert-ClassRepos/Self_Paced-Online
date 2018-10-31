from caught_speeding import caught_speeding


def test_1():
    assert caught_speeding(60, False) is 0

def test_2():
    assert caught_speeding(61, False) is 1

def test_3():
    assert caught_speeding(65, False) is 1

def test_4():
    assert caught_speeding(80, False) is 1

def test_5():
    assert caught_speeding(81, False) is 2

def test_5():
    assert caught_speeding(90, False) is 2

def test_6():
    assert caught_speeding(65, True) is 0

def test_7():
    assert caught_speeding(66, True) is 1

def test_8():
    assert caught_speeding(80, True) is 1

def test_9():
    assert caught_speeding(85, True) is 1

def test_10():
    assert caught_speeding(86, True) is 2

def test_11():
    assert caught_speeding(90, True) is 2