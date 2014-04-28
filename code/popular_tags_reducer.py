#!/usr/bin/python

import sys
import csv

def reducer(key, values):
    the_id = key
    answer_count = 0
    answer_total_length = 0   
    question_body_length = None
    for value in values:
        node_type = value[1]
        body_length = int(value[2])
        if node_type == "question":
            question_body_length = body_length
        else:
            answer_count += 1
            answer_total_length += body_length
    if answer_count == 0:
        yield '%s\t%s\t%s' % (the_id, question_body_length, "NA")
    else:
        yield '%s\t%s\t%s' % (the_id, question_body_length, float(answer_total_length) / float(answer_count))
            
if __name__ == "__main__":
    runner.run_reducer(reducer)
