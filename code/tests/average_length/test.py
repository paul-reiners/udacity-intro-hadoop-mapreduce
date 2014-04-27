#!/usr/bin/python

# Based on:
#   http://blog.zhengdong.me/2012/07/30/streaming-python-unit-testing

import unittest
from project.average_length import mapper
from project.average_length import reducer 
from random import shuffle

class StudentTimesMapperTest(unittest.TestCase):
    def test_mapper(self):
        header = '"id"\t"title"\t"tagnames"\t"author_id"\t"body"\t"node_type"\t' \
                      '"parent_id"\t"abs_parent_id"\t"added_at"\t"score"\t"state_string"\t' \
                      '"last_edited_id"\t"last_activity_by_id"\t"last_activity_at"\t' \
                      '"active_revision_id"\t"extra"\t"extra_ref_id"\t"extra_count"\t"marked"'
        # User has question
        line1 = '"1"\t"title"\t"tagnames"\t"1"\t"What is the answer to this question?"\t"question"\t"parent_id"\t' \
                     '"abs_parent_id"\t"2014-01-14 17:18:35.613939+00"\t"score"\t"state_string"\t' \
                     '"last_edited_id"\t"last_activity_by_id"\t"last_activity_at"\t' \
                     '"active_revision_id"\t"extra"\t"extra_ref_id"\t"extra_count"\t"marked"'
        mapper_expected1 = '1\t0\tquestion\t36'
        # User has answer
        line2 = '"2"\t"title"\t"tagnames"\t"2"\t"The answer is 5."\t"answer"\t"1"\t' \
                     '"abs_parent_id"\t"2014-01-14 08:18:35.613939+00"\t"score"\t"state_string"\t' \
                     '"last_edited_id"\t"last_activity_by_id"\t"last_activity_at"\t' \
                     '"active_revision_id"\t"extra"\t"extra_ref_id"\t"extra_count"\t"marked"'
        mapper_expected2 = '1\t1\tanswer\t16'
        # User has comment
        line3 = '"3"\t"title"\t"tagnames"\t"2"\t"body"\t"comment"\t"parent_id"\t' \
                     '"abs_parent_id"\t"2014-01-14 08:19:35.613939+00"\t"score"\t"state_string"\t' \
                     '"last_edited_id"\t"last_activity_by_id"\t"last_activity_at"\t' \
                     '"active_revision_id"\t"extra"\t"extra_ref_id"\t"extra_count"\t"marked"'
        
        my_input = [line1, line2, line3]
        shuffle(my_input)
        my_input.insert(0, header)
        expected = [mapper_expected1, mapper_expected2]

        result = [] 
        for output in mapper.mapper(my_input):
            result.append(output)
        self.assertTrue(sorted(expected) == sorted(result))

    def test_reducer(self):
        keys = ['1', '2', '3']
        valuess = [[['0', 'question', '8'], ['1', 'answer', '15']], [['0', 'question', '3'], ['1', 'answer', '4'], ['1', 'answer', '6']], [['0', 'question', '7']]]
        expecteds = [['1\t8\t15.0'], ['2\t3\t5.0'], ['3\t7\tNA']]

        for i in range(len(keys)):
            key = keys[i]
            values = valuess[i]
            result = []
            for output in reducer.reducer(key, values):
                result.append(output)
            self.assertEqual(expecteds[i], result)

if __name__ == '__main__':
    unittest.main()
