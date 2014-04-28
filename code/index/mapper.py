#!/usr/bin/python
"""
A MapReduce program that creates an index of all words that can be found in the 
body of a forum post and node id they can be found in.
"""

import sys
import csv
import re

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

count = 0
# Skip header.
reader.next()
for line in reader:
    body = line[4]
    node_id = line[0]
    parts = re.split('\s|[.!?:;"()<>[\]#$=\-/,]', body)
    for part in parts:
        if len(part) > 0:
            writer.writerow([part.lower(), 1, node_id])

