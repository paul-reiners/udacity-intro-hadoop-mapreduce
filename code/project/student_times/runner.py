"""
Author: Chris Zheng don9z

    Hangzhou, China
    http://blog.zhengdong.me
"""

import sys
def get_mapper_feeds():
    for line in sys.stdin:
        yield line.strip()

def combine_bykeys(stdin):
    current_key = None
    current_values = []

    for line in stdin:
        line = line.strip()
        try:
            key, values = line.split('\t', 1)
            values = values.split('\t')
        except ValueError:
            continue

        if current_key == key:
            current_values.append(values)
        else:
            if current_key:
                yield current_key, current_values
            current_key = key
            current_values = [values]

    if current_key != None and current_key == key:
        yield current_key, current_values

def get_reducer_feeds():
    return combine_bykeys(sys.stdin)

def run_mapper(mapper):
    for feed in get_mapper_feeds():
        for keyvalue in mapper(feed):
            print keyvalue

def run_mapper_with_conf(mapper, conf):
    for feed in get_mapper_feeds():
        for keyvalue in mapper(feed, conf):
            print keyvalue

def run_reducer(reducer):
    for key, values in get_reducer_feeds():
        for keyvalue in reducer(key, values):
            print keyvalue

def run_reducer_with_conf(reducer, conf):
    for key, values in get_reducer_feeds():
        for keyvalue in reducer(key, values, conf):
            print keyvalue

def run_combiner(combiner):
    run_reducer(combiner)

def run_combiner_with_conf(combiner, conf):
    run_reducer_with_conf(combiner, conf)

