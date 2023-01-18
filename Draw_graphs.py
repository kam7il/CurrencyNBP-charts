import matplotlib.pyplot as plt
from CurrencyNBP_get_data import prize_in_pln


data = prize_in_pln()
x = data[0]
y = data[1]


# plt.figure().set_figwidth(15)
# plt.figure().set_figheight(7)
# plt.rcParams['figure.figsize'] = [15, 7]

plt.rcParams['figure.autolayout'] = "True"
plt.figure(f"Chart of {data[2][0]}/PLN")
plt.plot(x, y)  # Narysuj niektóre dane na osiach.
plt.show()
