import matplotlib.pyplot as plt

channels = [
    "Social Media", "Television", "Print Media", "Radio",
    "Email Marketing", "Influencer Marketing", "SEO", "Events"
]

budget = [28, 22, 10, 8, 12, 9, 6, 5]

plt.figure(figsize=(8, 8))
plt.pie(budget, labels=channels, autopct='%1.1f%%', startangle=90)
plt.title("Marketing Budget Allocation")
plt.tight_layout()
plt.show()
