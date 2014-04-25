#!/usr/bin/python

import sys
import csv
import runner

def reducer(key, values):
    users = {}
    current_author_id = None
    hour_counts = [0] * 24
    
    author_id = key
    for value in values:
        hour = int(value[0])
        count = int(value[1])
        hour_counts[hour] += count
    max_hours = get_max_hours(hour_counts)
    for max_hour in max_hours:
        yield '%s\t%s' % (author_id, max_hour)

def get_max_hours(hour_counts):
    max_hours = []
    max_hour_count = -1
    for i in range(24):
        if hour_counts[i] > max_hour_count:
            max_hour_count = hour_counts[i]
    for i in range(24):
        if hour_counts[i] == max_hour_count:
            max_hours.append(i)
    
    return max_hours
            
if __name__ == "__main__":
    runner.run_reducer(reducer)

