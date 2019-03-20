def format_time(seconds):
    slice = {'year': 31536000, 'day': 86400, 'hour': 3600, 'minute': 60, 'second': 1}
    time_string = "none"
    for unit_name, unit_time in slice.items():
        units = int(seconds / unit_time)
        if units:
            seconds -= units * unit_time
            time_string = (time_string if time_string != 'none' else '') + ', {} {}{}'.format(units, unit_name, 's' if units > 1 else '')
    return ' and'.join(time_string.lstrip(', ').rsplit(',', 1))
