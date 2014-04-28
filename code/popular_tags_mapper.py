#!/usr/bin/python
"""
Top Tags
We are interested seeing what are the top tags used in posts.

Write a mapreduce program that would output Top 10 tags, ordered by the number
of questions they appear in.

For an extra challenge you can think how to get a top 10 list of tags, where
they are ordered by some weighted score by your choice.
"""

import sys
import csv

def mapper(stdin):
    reader = csv.reader(stdin, delimiter='\t')
    # Skip header.
    reader.next()
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:
        if len(line) == 19:
            # "node_type": type of the node, either "question", "answer" or "comment"
            node_type = line[5]
            if node_type == "question":
                tagnamesStr = line[2]
                tagnames = tagnamesStr.split()
                for tagname in tagnames:
                    yield '%s\t%s' % (tagname, "1")
        
if __name__ == "__main__":
    for output in mapper(sys.stdin):
        print output
