import pytest
from code_challenge_1.challenge_1 import format_time

def test_one_second():
    t = format_time(1)
    assert t == "1 second"
    
def test_ten_seconds():
    t = format_time(10)
    assert t == "10 seconds"

