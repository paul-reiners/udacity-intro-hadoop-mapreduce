setwd("~/Dropbox/education/Udacity/CS/udacity-intro-hadoop-mapreduce")

popular.tags <- read.table("results/popular_tags.tsv", sep="\t")
colnames(popular.tags) <- c("Tag", "Counts")

library(wordcloud)
wordcloud(popular.tags$Tag, popular.tags$Counts)
