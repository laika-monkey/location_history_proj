#!/usr/bin/env python

namelist = {
    'fname' : '/mnt/media/data/google_location_history/location_history.json',
        }

'''
Program to keep me from going insane.

Occasionally get Google Location History.  
Read in JSON
Dump to MySQL db, do not overwrite
Use MySQL to serve website images

For now, do basic stats on data

Start from this end, see if that makes sense for javascript graphing
'''

def plot_accuracy_hist(**kwargs):
    pass

def plot_heat_map(**kwargs):
    pass

def plot_distance_hist(**kwargs):
    ''' plot binned distances travelled, each panel by transport type '''
    pass

def plot_monthly_hist(**kwargs):
    ''' plot distance travelled each month, panel by transport type '''
    pass

def plot_activity_hist(**kwargs):
    ''' plot histogram of activity types '''
    pass

def plot_segments(dtg0, dtg1, plottype='line', **kwargs):
    ''' plot location data as scatter points or line segments for given period '''
    pass

################################################################################
def run_main(fname, **kwargs):
    '''
    timestampMs     str,    milliseconds (epoch time)

    '''
    
    import ijson
    import os
    import sys

    print fname
    with open(fname, 'r') as fh:
        objs = ijson.items(fh, 'locations.item') #activity.activity.item')
##        objs = ijson.items(fh, 'locations.item.activity.item.activity') #activity.activity.item')
        j = 0

        
##        trips_cycling = (o for o in objs if o['type'] == 'ON_BICYCLE')
##        for i, loc in enumerate(trips_cycling):

        for i, loc in enumerate(objs):
            if 'activity' not in loc:
                continue

            for k, activity in enumerate(loc['activity']):
                for activity_option in activity['activity']:
                    if activity_option['type'] == 'ON_BICYCLE':
                        print activity_option

                print 'EPOCH:', activity['timestampMs']
                print 'TIME: ', epoch2dtg(float(activity['timestampMs']))
                print ''
            ''' start here - figure out if a full bike ride is a giant number of activities'''


            j += 1
            if j > 100:
                sys.exit(0)

def epoch2dtg(epoch, fmt_dtg='%Y-%m-%d %H:%M:%S', **kwargs):
    import time
##    retype = type(epoch)
##    return retype([time.strftime(fmt_dtg, time.gmtime(float(e))) for e in epoch])
    return time.strftime(fmt_dtg, time.gmtime(epoch/1000))

if __name__ == "__main__":
    import sys
    run_main(**namelist)
