def format_time(seconds):
        time_string = "none"
        seconds, time_string = time_slice(seconds, time_string, 31536000, 'year')
        seconds, time_string = time_slice(seconds, time_string, 86400, 'day')
        seconds, time_string = time_slice(seconds, time_string, 3600, 'hour')
        seconds, time_string = time_slice(seconds, time_string, 60, 'minute')
        seconds, time_string = time_slice(seconds, time_string, 1, 'second')
        return rreplace(time_string.lstrip(", "), ',', ' and', 1)


def time_slice(seconds, time_string, time_unit, unit_name):
    units = int(seconds / time_unit)
    if units:
        seconds = seconds - units * time_unit
        return seconds, (time_string if time_string != 'none' else '') + ', {} {}{}'.format(units, unit_name, 's' if units > 1 else '')
    else:
        return seconds, time_string


def rreplace(string, old, new, occurrence):
    li = string.rsplit(old, occurrence)
    return new.join(li)
