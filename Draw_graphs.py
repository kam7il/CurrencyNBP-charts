import matplotlib.pyplot as plt
from CurrencyNBP_get_data import prize_in_pln

data = prize_in_pln()
x_data = data[0]
y_data = data[1]

fig, ax1 = plt.subplots()
fig.canvas.manager.set_window_title(f"Chart of {data[2][0]}/PLN")  # tytuł okna
ax1.plot(x_data, y_data, color="green", linewidth=3)  # linia właściwości
ax1.tick_params("y", colors="blue")  # parametry skali y
fig.autofmt_xdate()  # auto rotacja daty
ax1.set(title=f"Chart of {data[2][0]}/PLN", xlabel="Date", ylabel="PLN")  # etykiety
ax1.yaxis.grid(True)  # pomocnicze linie y
plt.show()
