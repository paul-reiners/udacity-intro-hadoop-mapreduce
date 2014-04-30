#!/usr/bin/python
"""
We see what the response time is for answers to questions.

This is the Mapper.
"""

import sys
import csv

def mapper(stdin):
    """
    MapReduce Mapper.  Output is tab-delimited.  Each line gives the question
    ID, 0/1, question/answer, and post time.
    """
    reader = csv.reader(stdin, delimiter='\t')
    # Skip header.
    reader.next()
    writer \
        = csv.writer(
            sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:
        if len(line) == 19:
            the_id = line[0]
            node_type = line[5]
            added_at = line[8]
            if node_type == "question":
                writer.writerow([the_id, "0", "question", added_at])
            elif node_type == "answer":
                parent_id = line[6]
                writer.writerow([parent_id, "1", "answer", added_at])

if __name__ == "__main__":
    mapper(sys.stdin)
