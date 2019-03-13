def format_time(s):
    t = ""
    if s >= 31536000:
        u = int(s / 31536000)
        s = s - u * 31536000
        t += '{}{} {}{}'.format(' and ' if len(t) else '', u ,'year', 's' if u > 1 else '')
    if s >= 86400:
        u = int(s / 86400)
        s = s - u * 86400
        t += '{}{} {}{}'.format(' and ' if len(t) else '', u ,'day', 's' if u > 1 else '')
    if s >= 3600:
        u = int(s / 3600)
        s = s - u * 3660
        t += '{}{} {}{}'.format(' and ' if len(t) else '', u ,'hour', 's' if u > 1 else '')
    if s >= 60:
        u = int(s / 60)
        s = s - u * 60
        t += '{}{} {}{}'.format(' and ' if len(t) else '', u ,'minute','s' if u > 1 else '')
    if (s > 0): t += '{}{} {}{}'.format(' and ' if len(t) else '', s, 'second', 's' if s > 1 else '')
    return t 

