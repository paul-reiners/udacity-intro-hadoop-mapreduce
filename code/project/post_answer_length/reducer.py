#!/usr/bin/python

import sys
import csv

def reducer():
    users = {}
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    current_author_id = None
    hour_counts = [0] * 24
    
    for line in reader:
	if len(line) == 3:
            author_id = line[0]
            hour = int(line[1])
            count = int(line[2])
            if current_author_id is None or author_id != current_author_id:
                if not current_author_id is None:
                    write_record(current_author_id, hour_counts, writer)
                hour_counts = [0] * 24
                current_author_id = author_id
            hour_counts[hour] += count
    write_record(current_author_id, hour_counts, writer)

def get_max_hour(hour_counts):
    max_hours = []
    max_hour_count = -1
    for i in range(24):
        if hour_counts[i] > max_hour_count:
            max_hour_count = hour_counts[i]
    for i in range(24):
        if hour_counts[i] == max_hour_count:
            max_hours.append(i)
    
    return max_hours

def write_record(author_id, hour_counts, writer):
    max_hours = get_max_hour(hour_counts)
    for max_hour in max_hours:
        newLine = [author_id, max_hour]
        writer.writerow(newLine)
            
if __name__ == "__main__":
    reducer()
