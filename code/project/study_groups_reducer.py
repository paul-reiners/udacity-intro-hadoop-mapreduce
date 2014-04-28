#!/usr/bin/python

import sys
import csv

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    current_id = None
    user_ids = []
    for line in reader:
	if len(line) == 2:
            the_id = line[0]
            if current_id is None or the_id != current_id:
                if not current_id is None:
                    write_record(current_id, user_ids, writer)
                user_ids = []
                current_id = the_id
                    
            user_id = int(line[1])
            user_ids.append(user_id)
    write_record(current_id, user_ids, writer)

def write_record(the_id, user_ids, writer):
    writer.writerow([the_id, user_ids])
    
if __name__ == "__main__":
    reducer()
