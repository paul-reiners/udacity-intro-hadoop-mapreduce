setwd("~/Dropbox/education/Udacity/CS/udacity-intro-hadoop-mapreduce")

# study.groups <- read.table("test/study_groups_actual.tsv", sep="\t", stringsAsFactors = FALSE)
study.groups <- read.table("results/study_groups.tsv", sep="\t", stringsAsFactors = FALSE)
colnames(study.groups) <- c("QuestionNodeID", "StudentIDs")

# returns string w/o leading or trailing whitespace
# From http://stackoverflow.com/a/2261149/7648
trim <- function (x) gsub("^\\s+|\\s+$", "", x)

file.name <- "results/study_groups_edges.csv"
sink(file.name)
cat('"V1","V2"\n')
for (i in 1:nrow(study.groups)) {
  student.ids <- study.groups[i, ]$StudentIDs
  # Get rid of '[' and ']'.
  student.ids.2 <- substr(student.ids, 2, nchar(student.ids) - 1)
  student.ids.3 <- unlist(strsplit(student.ids.2, "[,]"))
# Not terribly efficient code below.
  j = 1
  while (j < length(student.ids.3)) {
    v1 = trim(student.ids.3[j])
    k = j + 1
      while (k <= length(student.ids.3)) {
        v2 = trim(student.ids.3[k])
        cat(paste(v1, v2, sep = ","))
        cat('\n')
        k = k + 1
      }
    j = j + 1
  }
}
sink()

library(igraph)

edges = read.csv(file.name)
g = graph.data.frame(edges, FALSE)

plot(g, vertex.size=5)
