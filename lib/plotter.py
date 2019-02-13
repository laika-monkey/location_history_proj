#!/usr/bin/env python

namelist = {
    'fname' : '/mnt/media/data/google_location_history/location_history.json',
    'dbname' : '/mnt/media/data/location.db',

    }
'''
Program to keep me from going insane.

Occasionally get Google Location History.  
Read in JSON
Dump to sqlite db, do not overwrite
Use sql to serve website images

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

def plot_segment(**kwargs):
    ''' two panel plot of activity confidence and location '''
    import matplotlib.pyplot as plt

    
def draw_map(grid=[20, 35, -90, 75], corners=[20, 35, -90, 75],
    delta=1, water='blue', fill='#dcbc80', res='f', **kwargs):
    from mpl_toolkits.basemap import Basemap

    m = Basemap(projection='npstere', boundinglat=grid[0], lon_0=0,
            resolution='f')
    m.drawcoastlines(linewidth=0.5)
    m.fillcontinents(color=fill, lake_color=water, zorder=0)
    m.drawstates()
    args = { 'linewidth' : .5, 'dashes' : [4,1], size : 'xx-small' }
    m.drawparallels(np.arange(grid[0], grid[1], 1, labels=[0,0,0,0], **args)
    m.drawmeridians(np.arange(grid[2], grid[3], 1, labels=[1,1,0,0], **args)
    return m

    class Segment:q

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
        j = 0
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
