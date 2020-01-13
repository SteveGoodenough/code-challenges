from code_challenge_19.challenge_19 import create_reference_id
from code_challenge_19.challenge_19 import decode_reference_id
from code_challenge_19.challenge_19 import move_trolley
from code_challenge_19.challenge_19 import rotate_map
from code_challenge_19.challenge_19 import extract_map
import pytest

# "MToxOkU6MTIzNDU2" 1, 1, E
# "MjoxOkU6MTIzNDU2" 2, 1, E
# "MToyOkU6MTIzNDU2" 1, 2, E
# "NDo0OkU6MTIzNDU2" 4, 4, E
# "NDo4OkU6MTIzNDU2" 4, 8, E

TEST_MAP = \
    "*************************\n" +\
    "*                       *\n" +\
    "* ********** ********** *\n" +\
    "* ********** ********** *\n" +\
    "*                       *\n" +\
    "* ********** ********** *\n" +\
    "* ********** ********** *\n" +\
    "* ********** ********** *\n" +\
    "*                       *\n" +\
    "*************************\n"


@pytest.fixture(autouse=True)
def set_test_map(mocker):
    mocker.patch('code_challenge_19.challenge_19.MAP', TEST_MAP)


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


def test_extract_map(mocker):
    test_map = \
        " **\n" +\
        "* *\n" +\
        "** \n"
    mocker.patch('code_challenge_19.challenge_19.MAP', test_map)
    map = extract_map()
    assert map == [
        [' ', '*', '*'],
        ['*', ' ', '*'],
        ['*', '*', ' '],
    ]


def test_move_trolley_invalid_command():
    with pytest.raises(ValueError, match='Unknown command'):
        view, reference_id = move_trolley('X', "MToxOkU6MTIzNDU2")


def test_move_trolley_initial_call():
    view, reference_id = move_trolley()
    assert reference_id == "MToxOkU6MTIzNDU2"
    assert view == [
        'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'OR',
        'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'OR']


def test_move_trolley_east_from_initial_location():
    view, reference_id = move_trolley('M', "MToxOkU6MTIzNDU2")
    assert reference_id == "MjoxOkU6MTIzNDU2"
    assert view == [
        'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'OR',
        'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'OR']


def test_move_trolley_east_from_middle_row():
    view, reference_id = move_trolley('M', "NDo0OkU6MTIzNDU2")
    assert reference_id == "NTo0OkU6MTIzNDU2"
    assert view == [
        'O', 'O', 'O', 'O', 'O', 'O', 'OLR',
        'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'OLR']


def test_move_trolley_east_from_bottom_row():
    view, reference_id = move_trolley('M', "NDo4OkU6MTIzNDU2")
    assert reference_id == "NTo4OkU6MTIzNDU2"
    assert view == [
        'O', 'O', 'O', 'O', 'O', 'O', 'OL',
        'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'OL']


def test_move_trolley_east_is_blocked_so_move_ignored():
    view, reference_id = move_trolley('M', "MToyOkU6MTIzNDU2")
    assert reference_id == "MToyOkU6MTIzNDU2"
    assert view == []


def test_rotate_E_is_0_degrees(mocker):
    test_map = \
        " ***\n" +\
        "* * \n" +\
        "** *\n" +\
        "*** \n"
    mocker.patch('code_challenge_19.challenge_19.MAP', test_map)
    map = extract_map()
    rotated_map = rotate_map(map, 1, 1, 'E')
    assert rotated_map == [
        [' ', '*', '*', '*'],
        ['*', ' ', '*', ' '],
        ['*', '*', ' ', '*'],
        ['*', '*', '*', ' '],
    ]


def test_rotate_N_is_90_degrees(mocker):
    test_map = \
        " ***\n" +\
        "* * \n" +\
        "** *\n" +\
        "*** \n"
    mocker.patch('code_challenge_19.challenge_19.MAP', test_map)
    map = extract_map()
    rotated_map = rotate_map(map, 1, 1, 'N')
    assert rotated_map == [
        ['*', '*', '*', ' '],
        ['*', '*', ' ', '*'],
        ['*', ' ', '*', '*'],
        [' ', '*', ' ', '*'],
    ]


def test_rotate_W_is_180_degrees(mocker):
    test_map = \
        " ***\n" +\
        "* * \n" +\
        "** *\n" +\
        "*** \n"
    mocker.patch('code_challenge_19.challenge_19.MAP', test_map)
    map = extract_map()
    rotated_map = rotate_map(map, 1, 1, 'W')
    assert rotated_map == [
        [' ', '*', '*', '*'],
        ['*', ' ', '*', '*'],
        [' ', '*', ' ', '*'],
        ['*', '*', '*', ' '],
    ]


def test_rotate_S_is_270_degrees(mocker):
    test_map = \
        " ***\n" +\
        "* * \n" +\
        "** *\n" +\
        "*** \n"
    mocker.patch('code_challenge_19.challenge_19.MAP', test_map)
    map = extract_map()
    rotated_map = rotate_map(map, 1, 1, 'S')
    assert rotated_map == [
        ['*', ' ', '*', ' '],
        ['*', '*', ' ', '*'],
        ['*', ' ', '*', '*'],
        [' ', '*', '*', '*'],
    ]


def test_rotate_using_invalid_orientation_returns_same_map(mocker):
    test_map = \
        " **\n" +\
        "* *\n" +\
        "** \n"
    mocker.patch('code_challenge_19.challenge_19.MAP', test_map)
    map = extract_map()
    rotated_map = rotate_map(map, 1, 1, 'X')
    assert rotated_map == [
        [' ', '*', '*'],
        ['*', ' ', '*'],
        ['*', '*', ' '],
    ]
