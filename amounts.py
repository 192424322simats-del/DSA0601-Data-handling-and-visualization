import matplotlib.pyplot as plt

categories = [
    "Groceries", "Dairy", "Fruits", "Vegetables", "Bakery",
    "Beverages", "Snacks", "Personal Care", "Household Items", "Frozen Foods"
]

sales = [120, 95, 80, 75, 68, 90, 110, 55, 70, 60]

max_sales = max(sales)
min_sales = min(sales)

highest_category = categories[sales.index(max_sales)]
lowest_category = categories[sales.index(min_sales)]

print("Highest Selling Category:", highest_category, "-", max_sales, "Lakhs")
print("Lowest Selling Category:", lowest_category, "-", min_sales, "Lakhs")

plt.figure(figsize=(12, 6))
bars = plt.bar(categories, sales, color='skyblue', edgecolor='black')

bars[categories.index(highest_category)].set_color('green')
bars[categories.index(lowest_category)].set_color('red')

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 1, yval, ha='center', fontsize=9)

plt.title("Monthly Sales Revenue by Product Category - June 2026", fontsize=14)
plt.xlabel("Product Category", fontsize=12)
plt.ylabel("Sales (₹ Lakhs)", fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
