#!/usr/bin/env python

def run_main(**namelist):
    from lib import Segment
    data = Segment(**namelist)
    data.read('ON_BICYCLE')

if __name__ == '__main__':
    import yaml

    namelist = yaml.load(open('options.yaml', 'r'))
    run_main(**namelist)

