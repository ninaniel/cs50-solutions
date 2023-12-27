from twttr import shorten

def test_shorten_lowers():
    assert shorten("hello, my 1-st name is Nina") == "hll, my 1-st nm s Nn"

def test_shorten_uppers():
    assert shorten("hEllO, mY 1-st nAmE Is NINA") == "hll, mY 1-st nm s NN"
