from CurrencyNBP_get_data import prize_in_pln
import matplotlib.pyplot as plt

print(prize_in_pln())

fig, ax = plt.subplots()  # Utwórz figurę zawierającą pojedyncze osie.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Narysuj niektóre dane na osiach.
plt.show()