from working import convert
import pytest

def test_valids():
    assert convert("8:30 PM to 7:30 AM") == "20:30 to 07:30"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"

def test_invalid_inputs():
    with pytest.raises(ValueError):
        convert("09:00 to 21:00")
        convert("9AM to 5PM")
        convert("9 A.M. to 5 A.M.")

def test_bad_inputs():
    with pytest.raises(ValueError):
        convert("9:15 AM 5:15 PM")
        convert("9 AM - 5 PM")

def test_out_of_range_time():
    with pytest.raises(ValueError):
        convert("09:60 AM to 05:60 PM")
        convert("14:20 AM to 20:30 PM")
        convert("9 AM to 17 PM")