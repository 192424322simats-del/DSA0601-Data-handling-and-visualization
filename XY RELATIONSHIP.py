import matplotlib.pyplot as plt

advertising = [5, 8, 10, 12, 15, 18, 20, 22, 25, 28]
sales = [42, 55, 63, 70, 82, 91, 98, 110, 120, 132]

plt.figure(figsize=(8, 5))
plt.scatter(advertising, sales, color='blue', s=80)

plt.title("Advertising Expenditure vs Sales Revenue")
plt.xlabel("Advertising Cost (₹ Lakhs)")
plt.ylabel("Sales Revenue (₹ Lakhs)")
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
=
