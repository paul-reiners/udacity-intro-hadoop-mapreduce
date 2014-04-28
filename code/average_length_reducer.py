#!/usr/bin/python

import sys
import csv

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    answer_count = 0
    answer_total_length = 0   
    question_body_length = None
    current_id = None
    for line in reader:
	if len(line) == 3:
            the_id = line[0]
            if current_id is None or the_id != current_id:
                if not current_id is None:
                    write_record(current_id, question_body_length, answer_count, answer_total_length, writer)
                answer_count = 0
                answer_total_length = 0   
                question_body_length = None
                current_id = the_id
                    
            node_type = value[1]
            body_length = int(value[2])
            if node_type == "question":
                question_body_length = body_length
            else:
                answer_count += 1
                answer_total_length += body_length
    write_record(current_id, question_body_length, answer_count, answer_total_length, writer)

def write_record(the_id, question_body_length, answer_count, answer_total_length, writer):
    if answer_count == 0:
        writer.writerow([the_id, question_body_length, "NA"])
    else:
        writer.writerow([the_id, question_body_length, float(answer_total_length) / float(answer_count)])
    
if __name__ == "__main__":
    reducer()
