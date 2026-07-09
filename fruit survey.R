fruits <- c("Apple", "Banana", "Mango", "Orange", "Grapes")
votes <- c(25, 18, 30, 12, 8)

survey_data <- data.frame(Fruit = fruits, Votes = votes)

most_preferred <- survey_data$Fruit[which.max(survey_data$Votes)]
least_preferred <- survey_data$Fruit[which.min(survey_data$Votes)]

print(paste("Most preferred fruit:", most_preferred))
print(paste("Least preferred fruit:", least_preferred))

barplot(survey_data$Votes,
        names.arg = survey_data$Fruit,
        col = c("red", "yellow", "orange", "green", "purple"),
        main = "Favourite Fruit Survey",
        xlab = "Fruits",
        ylab = "Votes")