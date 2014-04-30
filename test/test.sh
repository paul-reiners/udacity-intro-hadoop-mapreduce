#!/bin/bash
# init
function pause() {
   read -p "$*"
}

cd /Users/paulreiners/Dropbox/education/Udacity/CS/udacity-intro-hadoop-mapreduce/code/project/map_reduce

cat student_test_posts.csv | python student_times_mapper.py | sort | python student_times_reducer.py > ../../test/student_times_actual.tsv
diff ../../test/student_times_expected.txt ../../test/student_times_actual.tsv
pause 'Press [Enter] key to continue...'

cat student_test_posts.csv | python average_length_mapper.py | sort | python average_length_reducer.py > ../../test/average_length_actual.tsv
diff ../../test/average_length_expected.txt ../../test/average_length_actual.tsv
pause 'Press [Enter] key to continue...'

cat student_test_posts.csv | python popular_tags_mapper.py | sort | python popular_tags_reducer.py > ../../test/popular_tags_actual.tsv
diff ../../test/popular_tags_expected.txt ../../test/popular_tags_actual.tsv
pause 'Press [Enter] key to continue...'

cat student_test_posts.csv | python study_groups_mapper.py | sort | python study_groups_reducer.py > ../../test/study_groups_actual.tsv
diff ../../test/study_groups_expected.txt ../../test/study_groups_actual.tsv
pause 'Press [Enter] key to continue...'

cd /Users/paulreiners/Dropbox/education/Udacity/CS/udacity-intro-hadoop-mapreduce/code/index
cat ../../test/student_test_posts.csv | python mapper.py | sort | python reducer.py
pause 'Press [Enter] key to continue...'

cd /Users/paulreiners/Dropbox/education/Udacity/CS/udacity-intro-hadoop-mapreduce/code/project/map_reduce
cat ../../../test/student_test_posts.csv | python response_time_mapper.py
