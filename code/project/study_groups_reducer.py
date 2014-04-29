#!/usr/bin/python
"""
Study Groups
We might want to help students form study groups. But first we want to see if
there are already students on forums that communicate a lot between themselves.

As the first step for this analysis we have been tasked with writing a
mapreduce program that for each forum thread (that is a question node with all
it's answers and comments) would give us a list of students that have posted
there - either asked the question, answered a question or added a comment. If
a student posted to that thread several times, they should be added to that
list several times as well, to indicate intensity of communication.
"""

import sys
import csv

def reducer():
    """ MapReduce Reducer. """
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = \
        csv.writer(
            sys.stdout, delimiter='\t', quotechar='"',
            quoting=csv.QUOTE_MINIMAL)
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
    """
    Write record with format:
        Question Node ID |	Student IDs
    """
    writer.writerow([the_id, user_ids])

if __name__ == "__main__":
    reducer()
