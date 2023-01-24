import sys
from datetime import datetime
from requests import get, JSONDecodeError


def prize_in_pln():
    data_all_currency = get("https://api.nbp.pl/api/exchangerates/tables/a/?format=json")
    data_all_currency_json = data_all_currency.json()

    amount_of_currencies = len(data_all_currency_json[0]["rates"])  # ilosc walut
    # print(data_single_currency_json["rates"][0]["mid"]) #  test

    a = True
    while a:
        user_currency_code = input("Jaką walute chcesz sprawdzić? ").upper()
        # user_currency_code = "USD"

        # czy kod waluty istnieje
        for x in range(0, amount_of_currencies):
            if user_currency_code == data_all_currency_json[0]["rates"][x]["code"]:  # warunek sprawdzajacy czy istnieje
                a = False
                break
            elif amount_of_currencies == x and a is True:  # jeśli nie jest
                print("Nie ma takiego kodu waluty")

    user_date_input_start = input("Podaj date początkową (RRRR-MM-DD): ")
    # user_date_input_start = "2022-01-01"
    user_date_input_end = input("Podaj date końcową(RRRR-MM-DD): ")
    # user_date_input_end = "2022-02-28"

    try:
        datetime.fromisoformat(user_date_input_start)
        datetime.fromisoformat(user_date_input_end)
    except ValueError:
        print("Błędny format daty lub data nie poprawna")
        sys.exit()

    data_single_currency_date = get(
        f"https://api.nbp.pl/api/exchangerates/rates/a/{user_currency_code}/{user_date_input_start}/{user_date_input_end}"
        f"/?format=json")

    try:
        data_single_currency_date_json = data_single_currency_date.json()
        # print(data_single_currency_date_json)
    except JSONDecodeError:
        print("Nie ma danych w podanej dacie")
        sys.exit()

    data_for_charts = [[], [], [user_currency_code]]

    len_of_rates = len(data_single_currency_date_json["rates"])

    # print(len(data_single_currency_date_json["rates"]))
    # print(data_single_currency_date_json["rates"][0]["effectiveDate"])
    # print(data_single_currency_date_json["rates"][0]["mid"])

    for x in range(0, len_of_rates):
        data_for_charts[0].append(data_single_currency_date_json["rates"][x]["effectiveDate"])
        data_for_charts[1].append(data_single_currency_date_json["rates"][x]["mid"])

    # print(data_for_charts)

    return data_for_charts
