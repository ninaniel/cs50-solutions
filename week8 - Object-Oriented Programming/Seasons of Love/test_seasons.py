from seasons import get_date, minutes_from
import pytest
import datetime


def test_get_date(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "2021-6-4")
    assert get_date() == "2021-06-04"

def test_get_date(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "2021-13-12")
    with pytest.raises(SystemExit):
        get_date()

def test_minutes_from():
    today = datetime.date(2023,12,6)
    assert minutes_from(datetime.date(2022,12,6), today) == "Five hundred twenty-five thousand, six hundred minutes"
    assert minutes_from(datetime.date(2021,12,6), today) == "One million, fifty-one thousand, two hundred minutes"