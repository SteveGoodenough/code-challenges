from code_challenge_6.challenge_6 import my_filter
from code_challenge_6.challenge_6 import number_is_less_than_5
from code_challenge_6.challenge_6 import number_is_even
from code_challenge_6.challenge_6 import number_is_odd


def test_filter_less_than_5():
    result = my_filter([3,4,5,6,7,8], number_is_less_than_5)
    assert result == [3, 4]


def test_filter_number_is_odd():
    result = my_filter([3,4,5,6,7,8], number_is_odd)
    assert result == [3, 5, 7]


def test_filter_number_is_even():
    result = my_filter([3,4,5,6,7,8], number_is_even)
    assert result == [4, 6, 8]
