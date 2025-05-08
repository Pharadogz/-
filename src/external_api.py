import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


def convert_to_rub(transaction: dict) -> float:
    """Конвертирует сумму транзакции в рубли.

    :param transaction: dict, словарь с данными о транзакции
    :return: float, сумма транзакции в рублях
    """
    amount = transaction.get("amount")
    currency = transaction.get("currency")
    API_URL = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"

    if currency == "RUB":
        return float(amount)
    elif currency in ["USD", "EUR"]:
        try:
            response = requests.get(API_URL, headers={"apikey": API_KEY})
            response_data = response.json()
            if response.status_code != 200:
                raise Exception("Ошибка при получении данных с API")

            exchange_rate = response_data["rates"].get("RUB")
            if exchange_rate is not None:
                return float(amount) * exchange_rate
            else:
                raise ValueError("Курс RUB не найден")

        except (requests.RequestException, ValueError) as exc:
            print(f"Ошибка при конвертации валюты: {exc}")
            return 0.0  # или можно выбросить исключение для дальнейшей обработки
    else:
        print("Некорректная валюта")
        return 0.0  # или выбросить исключение
