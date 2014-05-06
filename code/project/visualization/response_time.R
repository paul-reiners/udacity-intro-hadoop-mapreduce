setwd("~/Dropbox/education/Udacity/CS/udacity-intro-hadoop-mapreduce")

response.time <- read.table("results/response_time.tsv", sep="\t")
colnames(response.time) <- c("QuestionID", "ResponseTimeInMinutes")
response.time <- response.time[complete.cases(response.time),]

library(plyr)
frequencies = count(response.time, c("ResponseTimeInMinutes"))

library(ggplot2)
ggplot(frequencies, aes(x=ResponseTimeInMinutes, y=freq)) +
  geom_bar(stat="identity", fill="dark blue") +
  ylab("Response time in minutes from question until first answer") +
  xlab("Minutes")
