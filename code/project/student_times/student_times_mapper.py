#!/usr/bin/python
"""
"""

import sys
import csv

def mapper(stdin):
    reader = csv.reader(stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:
	if len(line) == 19:
		theID = line[0]
		if theID == "id":
			continue
		author_id = line[3]
		added_at = line[8]
		# Sample added_at:
		# 2012-02-25 08:09:06.787181+00
		added_at = added_at.strip()
		hour = int(added_at[11:13])
		newLine = [author_id, hour, 1]

                writer.writerow(newLine)
        
if __name__ == "__main__":
    mapper(sys.stdin)
