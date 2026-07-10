import matplotlib.pyplot as plt

months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

energy = [420, 450, 490, 530, 560, 600, 580, 590, 610, 630, 590, 540]

plt.figure(figsize=(10, 5))
plt.plot(months, energy, marker='o')

plt.title("Monthly Electricity Generation - 2025")
plt.xlabel("Month")
plt.ylabel("Energy Generated (MWh)")
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
