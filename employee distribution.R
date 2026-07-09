departments <- c("HR", "Finance", "Marketing", "IT", "Sales")
percentages <- c(15, 20, 25, 25, 15)

total_employees <- 200

marketing_percent <- percentages[departments == "Marketing"]
marketing_employees <- (marketing_percent / 100) * total_employees

print(paste("Employees in Marketing department:", marketing_employees))

pie(percentages,
    labels = paste(departments, percentages, "%"),
    col = c("lightblue", "lightgreen", "pink", "orange", "yellow"),
    main = "Employee Distribution by Department")