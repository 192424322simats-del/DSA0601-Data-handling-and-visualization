categories <- c("Housing", "Transportation", "Food", "Entertainment")
percentages <- c(40, 20, 30, 10)

highest_category <- categories[which.max(percentages)]

print(paste("Weighted average category of spending is:", highest_category))

pie(percentages,
    labels = paste(categories, percentages, "%"),
    col = c("lightblue", "lightgreen", "pink", "yellow"),
    main = "Household Budget Distribution")