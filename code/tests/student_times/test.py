#!/usr/bin/python

# Based on:
#   http://blog.zhengdong.me/2012/07/30/streaming-python-unit-testing

import unittest
import project.student_times.mapper
import project.student_times.reducer
from random import shuffle

class StudentTimesMapperTest(unittest.TestCase):
    def test_mapper(self):
        header = '"id"\t"title"\t"tagnames"\t"author_id"\t"body"\t"node_type"\t' \
                      '"parent_id"\t"abs_parent_id"\t"added_at"\t"score"\t"state_string"\t' \
                      '"last_edited_id"\t"last_activity_by_id"\t"last_activity_at"\t' \
                      '"active_revision_id"\t"extra"\t"extra_ref_id"\t"extra_count"\t"marked"'
        # User has only one posting (at 17)
        line1 = '"1"\t"title"\t"tagnames"\t"1"\t"body"\t"node_type"\t"parent_id"\t' \
                     '"abs_parent_id"\t"2014-01-14 17:18:35.613939+00"\t"score"\t"state_string"\t' \
                     '"last_edited_id"\t"last_activity_by_id"\t"last_activity_at"\t' \
                     '"active_revision_id"\t"extra"\t"extra_ref_id"\t"extra_count"\t"marked"'
        mapper_expected1 = '1\t17\t1'
        # User has two postings, both at 08
        line2 = '"2"\t"title"\t"tagnames"\t"2"\t"body"\t"node_type"\t"parent_id"\t' \
                     '"abs_parent_id"\t"2014-01-14 08:18:35.613939+00"\t"score"\t"state_string"\t' \
                     '"last_edited_id"\t"last_activity_by_id"\t"last_activity_at"\t' \
                     '"active_revision_id"\t"extra"\t"extra_ref_id"\t"extra_count"\t"marked"'
        mapper_expected2 = '2\t08\t1'
        line3 = '"3"\t"title"\t"tagnames"\t"2"\t"body"\t"node_type"\t"parent_id"\t' \
                     '"abs_parent_id"\t"2014-01-14 08:19:35.613939+00"\t"score"\t"state_string"\t' \
                     '"last_edited_id"\t"last_activity_by_id"\t"last_activity_at"\t' \
                     '"active_revision_id"\t"extra"\t"extra_ref_id"\t"extra_count"\t"marked"'
        mapper_expected3 = '2\t08\t1'
        
        my_input = [line1, line2, line3]
        shuffle(my_input)
        my_input.insert(0, header)
        expected = [mapper_expected1, mapper_expected2, mapper_expected3]

        result = [] 
        for output in mapper.mapper(my_input):
            result.append(output)
        self.assertTrue(sorted(expected) == sorted(result))

    def test_reducer(self):
        keys = ['1', '2', '3']
        valuess = [[['17', '1']], [['08', '1'], ['08', '1'], ['09', '1']], [['08', '1'], ['09', '1']]]
        expecteds = [['1\t17'], ['2\t08'], ['3\t08', '3\t09']]

        for i in range(len(keys)):
            key = keys[i]
            values = valuess[i]
            result = []
            for output in reducer.reducer(key, values):
                result.append(output)
            self.assertEqual(expecteds[i], result)

if __name__ == '__main__':
    unittest.main()
