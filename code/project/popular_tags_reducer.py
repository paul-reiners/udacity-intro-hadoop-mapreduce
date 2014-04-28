#!/usr/bin/python

import sys
import csv

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    tag_count = 0
    current_tag = None
    top_10 = []
    for line in reader:
	if len(line) == 2:
            tag = line[0]
            if current_tag is None or tag != current_tag:
                if not current_tag is None:
                    top_10 = add_record(current_tag, tag_count, top_10)
                tag_count = 0
                current_tag = tag
                    
            count = int(line[1])
            tag_count += 1
    top_10 = add_record(current_tag, tag_count, top_10)
    for tag, tag_count in top_10:        
        writer.writerow([tag, tag_count])
        
def add_record(tag, tag_count, top_10):
    if len(top_10) < 10 or tag_count > top_10[9][1]:
        top_10.append([tag, tag_count])
        top_10.sort(key=lambda tup: tup[1], reverse=True)
        top_10 = top_10[:10]
    return top_10
    
if __name__ == "__main__":
    reducer()
