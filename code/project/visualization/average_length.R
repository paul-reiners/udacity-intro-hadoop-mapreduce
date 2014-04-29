setwd("~/Dropbox/education/Udacity/CS/udacity-intro-hadoop-mapreduce")

average.length <- read.table("results/average_length.tsv", sep="\t")
colnames(average.length) <- c("QuestionNodeID", "QuestionLength", "AverageAnswerLength")

library(ggplot2)
scatterplot <- ggplot(average.length, aes(x = QuestionLength, y = AverageAnswerLength))
answer.question.plot <- scatterplot + geom_point(colour = "blue", size = 1) + ggtitle("Average Answer Length vs. Question Length")

pdf("plots/AverageLength.pdf")

print(answer.question.plot)

dev.off()
