#!/usr/bin/python

from __future__ import print_function
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

def error(*objs):
    print("ERROR: ", *objs, file=sys.stderr)

def write_record(word, word_count, ids, writer):
    try:
        # Sometimes library call will fail.  Perhaps because of too long
        # a list of ids.
        writer.writerow([word, word_count, ids])
    except IOError as e:
        error(e)

if __name__ == "__main__":
    reducer()

