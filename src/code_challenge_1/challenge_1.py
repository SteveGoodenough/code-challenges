def format_time(s):
    t = ""
    t, s = time_slice(s, t, 31536000, 'year')
    t, s = time_slice(s, t, 86400, 'day')
    t, s = time_slice(s, t, 3600, 'hour')
    t, s = time_slice(s, t, 60, 'minute')
    t, s = time_slice(s, t, 1, 'second')
    return rreplace(t.lstrip(", "), ',', ' and', 1) 


def time_slice(secs, t, unit, nam):
    if secs >= unit:
        u = int(secs / unit)
        secs = secs - u * unit
        return t + ', {} {}{}'.format(u ,nam ,'s' if u > 1 else ''), secs
    else: return t, secs


def rreplace(s, old, new, occurrence):
    li = s.rsplit(old, occurrence)
    return new.join(li)

    # if s >= 31536000:
    #     u = int(s / 31536000)
    #     s = s - u * 31536000
    #     t += '{}{} {}{}'.format(' and ' if len(t) else '', u ,'year', 's' if u > 1 else '')
    # if s >= 86400:
    #     u = int(s / 86400)
    #     s = s - u * 86400
    #     t += '{}{} {}{}'.format(' and ' if len(t) else '', u ,'day', 's' if u > 1 else '')
    # if s >= 3600:
    #     u = int(s / 3600)
    #     s = s - u * 3660
    #     t += '{}{} {}{}'.format(' and ' if len(t) else '', u ,'hour', 's' if u > 1 else '')
    # if s >= 60:
    #     u = int(s / 60)
    #     s = s - u * 60
    #     t += '{}{} {}{}'.format(' and ' if len(t) else '', u ,'minute','s' if u > 1 else '')
    # if (s > 0): t += '{}{} {}{}'.format(' and ' if len(t) else '', s, 'second', 's' if s > 1 else '')

