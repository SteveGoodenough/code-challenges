import pytest
from code_challenge_1.challenge_1 import format_time

def test_one_second():
    t = format_time(1)
    assert t == "1 second"


def test_two_seconds():
    t = format_time(2)
    assert t == "2 seconds"


def test_ten_seconds():
    t = format_time(10)
    assert t == "10 seconds"


def test_one_minute():
    t = format_time(60)
    assert t == "1 minute"


def test_one_min_two_secs():
    t = format_time(62)
    assert t == "1 minute and 2 seconds"


def test_one_hour():
    t = format_time(3600)
    assert t == "1 hour"


def test_one_day():
    t = format_time(86400)
    assert t == "1 day"


def test_two_days():
    t = format_time(86400*2)
    assert t == "2 days"


def test_one_year():
    t = format_time(31536000)
    assert t == "1 year"


def test_hour_min_sec():
    t = format_time(3662)
    assert t == "1 hour, 1 minute and 2 seconds"
