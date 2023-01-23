import matplotlib.pyplot as plt
from CurrencyNBP_get_data import prize_in_pln


data = prize_in_pln()
x = data[0]
y = data[1]

fig, ax1 = plt.subplots()
fig.tight_layout(pad=4)
ax1.plot(x, y, color="green", linewidth=3)
ax1.tick_params("y", colors="blue")
fig.autofmt_xdate()
ax1.set(title=f"Chart of {data[2][0]}/PLN", xlabel="Date", ylabel="PLN")
plt.show()
