#!/usr/bin/python

import sys
import csv

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    current_word = None
    word_count = 0
    ids = []
    for line in reader:
        if len(line) == 3:
            word = line[0]
            if current_word is None or word != current_word:
                if not current_word is None:
                    write_record(current_word, word_count, ids, writer)
                current_word = word
                word_count = 0
                ids = []
            count = int(line[1])
            word_count += count
            the_id = int(line[2])
            if not the_id in ids:
                ids.append(the_id)
    write_record(current_word, word_count, ids, writer)

def write_record(word, word_count, ids, writer):
    ids.sort()
    writer.writerow([word, word_count, ids])

if __name__ == "__main__":
    reducer()

