setwd("~/Dropbox/education/Udacity/CS/udacity-intro-hadoop-mapreduce")

student.times <- read.table("results/student_times.tsv", sep="\t")
colnames(student.times) <- c("StudentID", "Hour")

library(plyr)
frequencies = count(student.times, c("Hour"))

library(ggplot2)
ggplot(frequencies, aes(x=Hour, y=freq)) +
  geom_bar(stat="identity", fill="dark blue") +
  ylab("Number of students who most frequently post at this hour") +
  xlab("Hour")
