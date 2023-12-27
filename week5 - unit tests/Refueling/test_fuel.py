from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("3/3") == 100
    assert convert("1/4") == 25
    assert convert("1/5") == 20
    assert convert("2/4") == 50
    assert convert("0/5") == 0
    assert convert("1/70") == 1

def test_gauge():
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(50) == "50%"
    assert gauge(25) == "25%"

def test_zero_div():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_value_er():
    with pytest.raises(ValueError):
        convert("28/7")

def test_value_error_type():
    with pytest.raises(ValueError):
        convert("one/two")
        convert("q/w")
        convert(" ")
        convert("as da")
