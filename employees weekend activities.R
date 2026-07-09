activities <- c("Video games", "Reading", "Cooking", "Painting", "Music Listening")
percentages <- c(20, 35, 20, 10, 25)

most_common <- activities[which.max(percentages)]

print(paste("Most common activity during weekends is:", most_common))

pie(percentages,
    labels = paste(activities, percentages, "%"),
    col = c("lightblue", "lightgreen", "pink", "yellow", "orange"),
    main = "Employees' Weekend Activities")