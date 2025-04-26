import json
import os
from typing import List, Dict, Union


def load_transactions(file_path: str = 'operations.json') -> List[Dict[str, Union[str, float, dict]]]:
    """
    Загружает транзакции из JSON-файла

    Args:
        file_path: Путь к JSON-файлу (по умолчанию 'operations.json')

    Returns:
        Список транзакций или пустой список при ошибке
    """
    if not os.path.isfile(file_path):
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            transactions = json.load(file)
            return transactions if isinstance(transactions, list) else []
    except (json.JSONDecodeError, UnicodeDecodeError):
        return []


def convert_amount(transaction: dict, currency_rates: dict = None) -> float:
    """
    Конвертирует сумму транзакции в рубли

    Args:
        transaction: Словарь с данными о транзакции
        currency_rates: Словарь курсов валют (по умолчанию базовые курсы)

    Returns:
        Сумма в рублях или 0.0 при ошибке
    """
    # Курсы валют по умолчанию
    default_rates = {
        "USD": 75.0,
        "EUR": 85.0,
        "GBP": 95.0,
        "RUB": 1.0
    }
    rates = currency_rates or default_rates

    try:
        amount = float(transaction['operationAmount']['amount'])
        currency = transaction['operationAmount']['currency']['code'].upper()
        return amount * rates.get(currency, 1.0)
    except (KeyError, ValueError, TypeError):
        return 0.0


def process_transactions(transactions: list) -> list:
    """
    Обрабатывает список транзакций, добавляя конвертированные суммы

    Args:
        transactions: Список транзакций

    Returns:
        Список транзакций с добавленными конвертированными суммами
    """
    processed = []
    for tx in transactions:
        if not isinstance(tx, dict):
            continue

        tx_copy = tx.copy()
        tx_copy['converted_amount'] = convert_amount(tx)
        processed.append(tx_copy)
    return processed


if __name__ == '__main__':
    # Пример использования
    transactions = load_transactions()
    processed_transactions = process_transactions(transactions)

    # Выводим первые 5 транзакций для примера
    for tx in processed_transactions[:5]:
        print(f"{tx.get('description', 'No description')}: "
              f"{tx.get('operationAmount', {}).get('amount')} "
              f"{tx.get('operationAmount', {}).get('currency', {}).get('code')} "
              f"=> {tx.get('converted_amount', 0):.2f} RUB")
