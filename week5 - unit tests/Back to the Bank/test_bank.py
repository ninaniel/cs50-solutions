from bank import value

def test_hello():
    assert value("hello, nice to meet you!") == 0
    assert value("Hello, nice to meet you!") == 0
    assert value("HELLO, nice to meet you!") == 0

def test_h():
    assert value("happy to meet you!") == 20
    assert value("HAPPY TO MEET YOU") == 20
    assert value("Happy to meet you!") == 20

def test_other():
    assert value("NICE TO MEET YOU") == 100
    assert value("nice to meet you") == 100
