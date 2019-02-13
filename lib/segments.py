class Segment(object):

    def __init__(self, fields=[], date_range=None, dbname='location.db', data=None, **kwargs):
        '''a this will represent a location history segment '''
        self.fields = fields
        self.date_range = date_range
        self.dbname = dbname
        self.data = data 

    def read(self, fields, **kwargs):
        '''
        Opens database and reads desired fields
        fields      list||str,              select defined fields form sqlite database
        start_time  YYYY-MM-DD HH:mm:ss,    string defining epoch time
        end_time    YYYY-MM-DD HH:mm:ss,    string defining epoch time to end
        '''
        import sqlite3
        import numpy as np
        from dtg import dtg2epoch

        base = ['timestampeMs_key', 'timestampMs', 'latitudeE7', 'longitudeE7']
        with sqlite3.connect(self.dbname) as conn:
            c = conn.cursor()
            if hasattr(fields, '_iter_'):
                fields = ', '.join(base + fields)
            else:
                base.append(fields)
                fields = ', '.join(base)
                
            query = "SELECT {} FROM activity".format(fields)
              
            if self.date_range is not None:
                e0, e1 = dtg2epoch(self.date_range)
                query += " WHERE timestampMs BETWEEN '{:f}' and '{:f}'".format(e0, e1)
                    
            query += ';' #?needed?
            print query
            c.execute(query)
            data = np.array(c.fetchall())
                    
            self.data = data[data[:,1].argsort()]

    def _split_segments(self, **kwargs):
        '''
        create process to find the beginning and end of activities
        Might be as simple as finding STILL for certain periods.  Stop lights
        seems like an issue

        never mind, reinit a bunch of new objects and put data in theM 
        '''
        pass

    def plot_path(self, **kwargs):
        ''' plot current segment '''
        pass

