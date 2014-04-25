#!/usr/bin/python

# Based on:
#   http://blog.zhengdong.me/2012/07/30/streaming-python-unit-testing

import unittest
import mapper
import reducer

class StudentTimesMapperTest(unittest.TestCase):
    def test_mapper(self):
        input = ['"id"\t"title"\t"tagnames"\t"author_id"\t"body"\t"node_type"\t"parent_id"\t"abs_parent_id"\t"added_at"\t"score"\t"state_string"\t"last_edited_id"\t"last_activity_by_id"\t"last_activity_at"\t"active_revision_id"\t"extra"\t"extra_ref_id"\t"extra_count"\t"marked"',
                 '"1"\t"title"\t"tagnames"\t"1"\t"body"\t"node_type"\t"parent_id"\t"abs_parent_id"\t"2014-01-14 17:18:35.613939+00"\t"score"\t"state_string"\t"last_edited_id"\t"last_activity_by_id"\t"last_activity_at"\t"active_revision_id"\t"extra"\t"extra_ref_id"\t"extra_count"\t"marked"']
        expected = ['1\t17\t1']

        result = [] 
        for output in mapper.mapper(input):
            result.append(output)
        self.assertEqual(expected, result)

    def test_reducer(self):
        key = '1'
        values = [['17', '1']]
        expected = ['1\t17']

        result = []
        for output in reducer.reducer(key, values):
            result.append(output)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
