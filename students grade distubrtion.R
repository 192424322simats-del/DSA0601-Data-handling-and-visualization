grades <- c("A", "B", "C", "D", "E")

students <- c(5, 8, 7, 6, 4)

barplot(students,
        names.arg = grades,
        main = "Student Grade Distribution",
        xlab = "Grades",
        ylab = "Number of Students")

scores <- c(95, 85, 75, 65, 50)

average <- sum(students * scores) / sum(students)

print(paste("Average score of the class =", average))