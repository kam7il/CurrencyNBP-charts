import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from CurrencyNBP_get_data import prize_in_pln

data = prize_in_pln()
x_data_pd = pd.to_datetime(data[0])
y_data = data[1]

fig, ax1 = plt.subplots()
fig.canvas.manager.set_window_title(f"Chart of {data[2][0]}/PLN")  # tytuł okna
ax1.plot(x_data_pd, y_data, color="green", linewidth=3)  # linia właściwości
ax1.tick_params("y", colors="blue")  # parametry skali y
# fig.autofmt_xdate()  # auto rotacja daty
ax1.set(title=f"Chart of {data[2][0]}/PLN", ylabel="PLN")  # etykiety
ax1.xaxis.grid(True)  # pomocnicze linie x
ax1.yaxis.grid(True)  # pomocnicze linie y

# formatowanie daty
locator = mdates.AutoDateLocator(minticks=3, maxticks=15)  # min max skala
ax1.xaxis.set_major_locator(locator)
ax1.xaxis.set_major_formatter(mdates.ConciseDateFormatter(locator))

plt.show()
