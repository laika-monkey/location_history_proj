#!/usr/bin/env python

import sys
from odict import odict

namelist = {
            'db_name': '/mnt/media/data/location.db',
            'fname_location':
                '/mnt/media/data/google_location_history/location_history.json',
            'fname_location': sys.argv[1],
            
            'fill_value' : {
                'INT' : -1,
                'REA' : -1.,
                'CHA' : '', },
            
            }

location = odict([
            ('timestampMs', 'CHAR(14)'), 
            ('latitudeE7', 'REAL'),
            ('longitudeE7', 'REAL'),
            ('heading', 'INT'),
            ('accuracy', 'INT',),
            ('altitude', 'INT'),
            ('verticalAccuracy', 'INT')])
activity = odict([
            ('ON_FOOT', 'INT'),
            ('WALKING', 'INT'),
            ('RUNNING', 'INT'),
            ('ON_BICYCLE', 'INT'),
            ('IN_VEHICLE', 'INT'),
            ('IN_ROAD_VEHICLE', 'INT'),
            ('IN_RAIL_VEHICLE', 'INT'),
            ('IN_TWO_WHEEL_VEHICLE', 'INT'),
            ('IN_FOUR_WHEEL_VEHICLE', 'INT'),
            ('IN_TWO_WHEELER_VEHICLE', 'INT'),
            ('IN_FOUR_WHEELER_VEHICLE', 'INT'),
            ('UNKNOWN', 'INT'),
            ('STILL', 'INT'),
            ('EXITING_VEHICLE', 'INT'),
            ('TILTING', 'INT')])

namelist.update({ 'tables' : {'location': location, 'activity': activity} })

#############################################################################_80
#############################################################################_80
#############################################################################_80

def dump_json2sql(tables={}, fill_value={}, 
    fname_location='./location_history.json', **kwargs):
    import ijson

    conn = init_db(tables, **kwargs)
    c = conn.cursor()
   
    #_loop over json records, write to appropriate table
    with open(fname_location, 'r') as fh:

        #_loop over each location instance in google file
        for i, l in enumerate(ijson.items(fh, 'locations.item')):
            if not i % 1000: print 'Processing location record ', i

            row = []
            for ii, (field, var_type) in enumerate(tables['location'].items()):
                row.append(l[field] if field in l else fill_value[var_type[:3]])

            row = ','.join([str(r) for r in row])
            c.execute("INSERT INTO location VALUES ({})".format(row))

            if 'activity' not in l:
                continue

            for ii, a in enumerate(l['activity']):

                row = [l['timestampMs']]
                for iii, (field, var_type) in enumerate(tables['location'].items()):
                    row.append(a[field] if field in a else fill_value[var_type[:3]])

                offset = len(tables['location'].keys())
                row += [fill_value[var_type[:3]]     \
                        for var_type in tables['activity'].itervalues()]
                for iii, activity in enumerate(a['activity']):
                    idx = tables['activity'].keys().index(activity['type']) + offset
                    row[idx] = activity['confidence']

                row = ','.join([str(r) for r in row])
                c.execute('INSERT INTO activity VALUES ({})'.format(row))

        
    conn.commit()
    conn.close()

def init_db(tables, dbtype='sqlite', db_name='default.db', **kwargs):
    ''' build schema for database '''
    import sqlite3
    import os

    '.tables for names of tables, .schema <tbname> for desc'
    print 'Initializing {}'.format(db_name)
    conn = sqlite3.connect(db_name)

    #_initialize location db
    try:
        c = conn.cursor()
        for table, values in tables.items():
            if table == 'activity':
                columns = ['timestampeMs_key']
                columns += [' '.join(pairs) for pairs in tables['location'].items()]
                columns += [' '.join(pairs) for pairs in values.items()]
                columns = ','.join(columns)
            else:
                columns = [' '.join(pairs) for pairs in values.items()]
                columns = ','.join(columns)
            cmd = 'CREATE TABLE {}({})'.format(table, columns)
            c.execute(cmd)
        conn.commit()

    except sqlite3.OperationalError as err:
        print "DB exists, continuing...{}".format(err)

    return conn

if __name__ == '__main__':
    dump_json2sql(**namelist)
