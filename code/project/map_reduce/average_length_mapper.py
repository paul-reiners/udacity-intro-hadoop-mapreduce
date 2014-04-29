#!/usr/bin/python
"""
We are interested to see if there is a correlation between the length of a post
and the length of answers.

Write a mapreduce program that would process the forum_node data and output the
length of the post and the average answer (just answer, not comment) length for
each post. You will have to decide how to write both the mapper and the reducer
to get the required result.
"""

import sys
import csv

def mapper(stdin):
    """
    MapReduce Mapper.  Output is tab-delimited.  Each line gives the question
    ID, 0/1, question/answer, and body length.
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
            body = line[4]
            node_type = line[5]
            if node_type == "question":
                writer.writerow([the_id, "0", "question", len(body)])
            elif node_type == "answer":
                parent_id = line[6]
                writer.writerow([parent_id, "1", "answer", len(body)])

if __name__ == "__main__":
    mapper(sys.stdin)
