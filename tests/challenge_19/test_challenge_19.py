from code_challenge_19.challenge_19 import move_trolley
from code_challenge_19.challenge_19 import create_reference_id
from code_challenge_19.challenge_19 import decode_reference_id
import pytest


# def test_go():
#     go()
#     assert 1 == 2


def test_encode_reference_id():
    x = 1
    y = 1
    orientation = "E"
    trolley_id = "123456"
    reference_id = create_reference_id(x, y, orientation, trolley_id)
    assert reference_id == "MToxOkU6MTIzNDU2"


def test_decode_reference_id():
    reference_id = "MToxOlM6MTIzNDU2"
    x, y, orientation, trolley_id = decode_reference_id(reference_id)
    assert x == 1
    assert y == 1
    assert orientation == "S"
    assert trolley_id == "123456"


def test_decode_invalid_reference_id_not_encoded_string():
    reference_id = "thiswontwork"
    with pytest.raises(ValueError, match='Invalid reference id'):
        x, y, orientation, trolley_id = decode_reference_id(reference_id)


def test_decode_invalid_reference_id_not_enough_elements():
    reference_id = "MToxOlM="
    with pytest.raises(ValueError, match='Not correct number of elements in reference id'):
        x, y, orientation, trolley_id = decode_reference_id(reference_id)


def test_move_trolley_invalid_command():
    with pytest.raises(ValueError, match='Unknown command'):
        view, referenece_id = move_trolley('X', "MToxOkU6MTIzNDU2")


def test_move_trolley_initial_call():
    view, referenece_id = move_trolley()
    assert referenece_id == "MToxOkU6MTIzNDU2"
    assert view == [
        'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'OR',
        'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'OR']

# "MToxOkU6MTIzNDU2" 1, 1, E
