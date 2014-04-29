#!/bin/bash
# init
function pause(){
   read -p "$*"
}

cd /Users/paulreiners/Dropbox/education/Udacity/CS/udacity-intro-hadoop-mapreduce/code/project

cat student_test_posts.csv | python student_times_mapper.py | sort | python student_times_reducer.py > ../../test/student_times_actual.txt
diff ../../test/student_times_expected.txt ../../test/student_times_actual.txt
pause 'Press [Enter] key to continue...'

cat student_test_posts.csv | python average_length_mapper.py | sort | python average_length_reducer.py > ../../test/average_length_actual.txt
diff ../../test/average_length_expected.txt ../../test/average_length_actual.txt
pause 'Press [Enter] key to continue...'

cat student_test_posts.csv | python popular_tags_mapper.py | sort | python popular_tags_reducer.py > ../../test/popular_tags_actual.txt
diff ../../test/popular_tags_expected.txt ../../test/popular_tags_actual.txt
pause 'Press [Enter] key to continue...'

cat student_test_posts.csv | python study_groups_mapper.py | sort | python study_groups_reducer.py > ../../test/study_groups_actual.txt
diff ../../test/study_groups_expected.txt ../../test/study_groups_actual.txt
