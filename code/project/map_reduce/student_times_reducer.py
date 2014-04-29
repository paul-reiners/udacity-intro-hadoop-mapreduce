#!/usr/bin/python
"""
Students and Posting Time on Forums

We have a lot of passionate students that bring a lot of value to forums. Forums
also sometimes need a watchful eye on them, to make sure that posts are tagged
in a way that helps to find them, that the tone on forums stays positive, and in
general - they need people who can perform some management tasks - forum
moderators. These are usually chosen from students who already have shown that
they are active and helpful forum participants.

Our students come from all around the world, so we need to know both at what
times of day the activity is the highest, and to know which of the students are
active at that time.

In this exercise your task is to find for each student what is the hour during
which the student has posted the most posts. Output from reducers should be:

    author_id    hour

For example:

    13431511\t13
    54525254141\t21

If there is a tie: there are multiple hours during which a student has posted a
maximum number of posts, please print the student-hour pairs on separate lines.
You can ignore the time-zone offset for all times - for example in the following
line:

    "2012-02-25 08:11:01.623548+00"

- you can ignore the +00 offset.

In order to find the hour posted, please use the date_added field and NOT the
last_activity_at field.
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
    """ Returns the max hour(s). """
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
    """
    Writes record in format.
        Student ID |	Hour
    """
    max_hours = get_max_hour(hour_counts)
    for max_hour in max_hours:
        new_line = [author_id, max_hour]
        writer.writerow(new_line)

if __name__ == "__main__":
    reducer()
