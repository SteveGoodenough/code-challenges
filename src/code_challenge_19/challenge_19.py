import base64

MAP = \
    "**************************\n" +\
    "*                        *\n" +\
    "* ********** *********** *\n" +\
    "* ********** *********** *\n" +\
    "*                        *\n" +\
    "* ********** *********** *\n" +\
    "* ********** *********** *\n" +\
    "* ********** *********** *\n" +\
    "*                        *\n" +\
    "**************************\n"


def move_trolley(command='', reference_id=''):
    map = MAP.split('\n')
    if command != '':
        x, y, orientation, trolley_id = decode_reference_id(reference_id)
        if command == 'M':
            pass
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

    view = generate_view(x, y, orientation)
    return view, create_reference_id(x, y, orientation, trolley_id)


def generate_view(x, y, orientation):
    view = ['O']
    return view


def create_reference_id(x, y, orientation, trolley_id):
    clear_reference_id = f'{x}:{y}:{orientation}:{trolley_id}'
    encoded_bytes = base64.b64encode(clear_reference_id.encode("utf-8"))
    reference_id = str(encoded_bytes, "utf-8")
    return reference_id


def decode_reference_id(reference_id):
    try:
        decoded_bytes = base64.b64decode(reference_id)
        decoded_list = str(decoded_bytes, "utf-8").split(':')
    except UnicodeDecodeError:
        raise ValueError('Invalid reference id')
    if len(decoded_list) != 4:
        raise ValueError('Not enough elements in reference id')
    return int(decoded_list[0]), int(decoded_list[1]), decoded_list[2], decoded_list[3]
