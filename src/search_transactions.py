import re


def search_transactions(transactions: list, search_string: str) -> list:
    """
    Функция для поиска транзакций по заданной строке
    """
    # Компилируем регулярное выражение для поиска
    pattern = re.compile(search_string, re.I)  # Игнорируем регистр

    # Фильтруем транзакции по совпадению с регулярным выражением
    same_transactions = [
        transaction
        for transaction in transactions
        if "description" in transaction and pattern.search(transaction["description"])
    ]

    return same_transactions


# Пример использования
transactions = [
    {"id": 1, "description": "Оплата за услуги", "amount": 100},
    {"id": 2, "description": "Покупка товара", "amount": 200},
    {"id": 3, "description": "Оплата за интернет", "amount": 50},
]

search_string = "оплата"
matched = search_transactions(transactions, search_string)

for transaction in matched:
    print(transaction)