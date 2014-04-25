#!/usr/bin/python

import sys
import csv

def reducer():
    users = {}
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    current_id = None 
    answer_count = 0
    answer_total_length = 0
    question_body_length = None

    for line in reader:
	    if len(line) == 4:
                the_id = line[0]
                node_type = line[2]
                body_length = int(line[3])
                if current_id is None or the_id != current_id:
                    if not current_id is None:
                        write_record(current_id, question_body_length, answer_count, answer_total_length, writer)
                    current_id = the_id
                    answer_count = 0
                    answer_total_length = 0   
                    question_body_length = None
                if node_type == "question":
                    question_body_length = body_length
                else:
                    answer_count += 1
                    answer_total_length += body_length
    write_record(current_id, question_body_length, answer_count, answer_total_length, writer)

def write_record(current_id, question_body_length, answer_count, answer_total_length, writer):
    if answer_count == 0:
        newLine = [current_id, question_body_length, "NA"]
    else:
        newLine = [current_id, question_body_length, float(answer_total_length) / float(answer_count)]
    writer.writerow(newLine)
            
if __name__ == "__main__":
    reducer()

