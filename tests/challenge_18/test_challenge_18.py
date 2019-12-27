from code_challenge_18.challenge_18 import Node
from code_challenge_18.challenge_18 import get_description
from code_challenge_18.challenge_18 import add_to_list
from code_challenge_18.challenge_18 import create_integer_list
from code_challenge_18.challenge_18 import reverse_list


def test_get_description_of_a_list():
    test_list = Node("hello", Node("world"))
    assert get_description(test_list) == "hello world None"


def test_add_item_to_list():
    base_list = Node("hello", Node("world"))
    test_list = add_to_list(base_list, "!")
    assert get_description(test_list) == "hello world ! None"


def test_convert_list_of_a_string_to_integer():
    base_list = Node("1")
    test_list = create_integer_list(base_list)
    assert get_description(test_list) == "1 None"
    assert type(test_list.item) == int


def test_convert_list_of_strings_to_integers():
    base_list = Node("1", Node("2"))
    test_list = create_integer_list(base_list)
    assert get_description(test_list) == "1 2 None"


def test_convert_list_of_strings_with_non_numeric_to_integers():
    base_list = Node("1", Node("2", Node("A")))
    test_list = create_integer_list(base_list)
    assert get_description(test_list) == "1 2 0 None"


def test_convert_another_list_of_strings_with_non_numeric_to_integers():
    base_list = Node("1s", Node("2", Node("A")))
    test_list = create_integer_list(base_list)
    assert get_description(test_list) == "0 2 0 None"


def test_reverse_a_list():
    base_list = Node("hello", Node("world", Node("!")))
    test_list = reverse_list(base_list)
    assert get_description(test_list) == "! world hello None"


def test_reverse_the_challenge_example_list():
    base_list = Node("a", Node("b", Node("c", Node("d", Node("e", Node("f"))))))
    test_list = reverse_list(base_list)
    assert get_description(test_list) == "f e d c b a None"
