def dtg2epoch(dtg, fmt_dtg='%Y-%m-%d %H:%M:%S', **kwargs):
    ''' go from fmt_dtg to epoch seconds in gmt '''
    from datetime import datetime as dt
    delta = lambda x: (dt.strptime(x, fmt_dtg) - dt(1970, 1, 1, 0, 0, 0)).total_seconds() * 1000.
    return delta(dtg) if not hasattr(dtg, '__iter__') else [delta(d) for d in dtg]

def epoch2dtg(epoch, fmt_dtg='%Y-%m-%d %H:%M:%S', **kwargs):
    import time
    delta = lambda x: time.strftime(fmt_dtg, time.gmtime(x/1000))
    return delta(epoch) if not hasattr(epoch, '__iter__') else [delta(e) in epoch]
