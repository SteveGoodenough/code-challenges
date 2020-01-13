import base64

MAP = \
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
ROTATIONS = {'E': 0, 'N': 1, 'W': 2, 'S': 3}


def move_trolley(command='', reference_id=''):
    map = extract_map()
    if command != '':
        x, y, orientation, trolley_id = decode_reference_id(reference_id)
        if command == 'M':
            if map[y][x+1] == ' ':
                x += 1
        elif command == 'L':
            pass
        elif command == 'R':
            pass
        else:
            raise ValueError('Unknown command')
    else:
        x = 1
        y = 1
        orientation = 'E'
        trolley_id = "123456"

    view = generate_view(map, x, y, orientation)
    return view, create_reference_id(x, y, orientation, trolley_id)


def extract_map():
    return list(list(line) for line in MAP[:-1].split('\n'))


def generate_view(map, x, y, orientation):
    view = []
    for idx, val in enumerate(map[y][x+1::]):
        if val == ' ':
            val = "O"
            if map[y-1][x+idx+1] == ' ':
                val += 'L'
            if map[y+1][x+idx+1] == ' ':
                val += 'R'
            view.append(val)
        else:
            break
    return view


def create_reference_id(x, y, orientation, trolley_id):
    clear_reference_id = f'{x}:{y}:{orientation}:{trolley_id}'
    reference_id = str(base64.b64encode(clear_reference_id.encode("utf-8")), "utf-8")
    return reference_id


def decode_reference_id(reference_id):
    try:
        decoded_list = str(base64.b64decode(reference_id), "utf-8").split(':')
    except UnicodeDecodeError:
        raise ValueError('Invalid reference id')
    if len(decoded_list) != 4:
        raise ValueError('Not correct number of elements in reference id')
    return int(decoded_list[0]), int(decoded_list[1]), decoded_list[2], decoded_list[3]


def rotate_map_and_coordinates(map, x, y, orientation):
    rotated_x = x
    rotated_y = y
    rotated_map = map
    for _ in range(ROTATIONS.get(orientation, 0)):
        rotated_x, rotated_y = rotate_coordinates_90_degrees(rotated_x, rotated_y, len(rotated_map) - 1)
        rotated_map = [list(line) for line in zip(*reversed(rotated_map))]
    return rotated_map, rotated_x, rotated_y


def rotate_coordinates_90_degrees(x, y, width):
    return width - y, x
