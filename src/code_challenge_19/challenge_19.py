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


def move_trolley(command='', reference_id=''):
    map = MAP.split('\n')
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


def generate_view(map, x, y, orientation):
    row_above = map[y-1][x+1::]
    row = map[y][x+1::].replace(' ', 'O')
    row_below = map[y+1][x+1::]
    view = []
    for idx, val in enumerate(row):
        if val == 'O':
            if row_above[idx] == ' ':
                val += 'L'
            if row_below[idx] == ' ':
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


def rotate_map():
    map = tuple(tuple(line) for line in MAP[:-1].split('\n'))
    return tuple(zip(*map[::-1]))
