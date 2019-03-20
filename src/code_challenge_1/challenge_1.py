def format_time(seconds):
    time_part = {'year': 31536000, 'day': 86400, 'hour': 3600, 'minute': 60, 'second': 1}
    time_slice = []
    for unit_name, unit_time in time_part.items():
        units = int(seconds / unit_time)
        if units:
            seconds -= units * unit_time
            time_slice.append('{} {}{}'.format(units, unit_name, 's' if units > 1 else ''))
    time_string = (", ".join(time_slice)) if len(time_slice) else 'none'
    return ' and'.join(time_string.rsplit(',', 1))
