#!/usr/bin/python
"""
We see what the response time is for answers to questions.

This is the Reducer.
"""

import sys
import csv
from datetime import datetime

def reducer():
    """
    MapReduce Reducer.
    """
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = \
        csv.writer(
            sys.stdout, delimiter='\t', quotechar='"',
            quoting=csv.QUOTE_MINIMAL)
    question_added_at = None
    min_minutes_diff = None
    current_id = None
    # Example date: 2012-02-22 21:36:17.077627+00
    prefix_len = len('2012-02-22 21:36:17')
    date_format = '%Y-%m-%d %H:%M:%S'
    for line in reader:
        if len(line) == 4:
            the_id = line[0]
            if current_id is None or the_id != current_id:
                if not current_id is None:
                    write_record(current_id, min_minutes_diff, writer)
                current_id = the_id

            node_type = line[2]
            added_at = line[3]
            if node_type == "question":
                question_added_at = \
                    datetime.strptime(added_at[:prefix_len], date_format)
            else:
                answer_added_at = \
                    datetime.strptime(added_at[:prefix_len], date_format)
                if not question_added_at is None:
                    delta = answer_added_at - question_added_at
                    minutes_diff = delta.seconds / 60
                    if min_minutes_diff is None or \
                        minutes_diff < min_minutes_diff:
                        min_minutes_diff = minutes_diff
    write_record(current_id, min_minutes_diff, writer)

def write_record(the_id, minutes_diff, writer):
    """
    Outputs
        Question Node ID |	Response Time (in minutes)
    """
    if minutes_diff is None:
        writer.writerow([the_id, "NA"])
    else:
        writer.writerow([the_id, minutes_diff])

if __name__ == "__main__":
    reducer()
