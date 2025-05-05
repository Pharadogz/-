import json
import os
import requests
from typing import List, Dict, Union, Optional, Any


def load_transactions(file_path: str = 'operations.json') -> List[Dict[str, Any]]:
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
            return [tx for tx in transactions if isinstance(tx, dict)] if isinstance(transactions, list) else []
    except (json.JSONDecodeError, UnicodeDecodeError):
        return []


def is_valid_transaction(transaction: Dict[str, Any]) -> bool:
    """
    Проверяет, что транзакция имеет правильную структуру

    Args:
        transaction: Словарь с данными транзакции

    Returns:
        True если транзакция валидна, иначе False
    """
    try:
        return all(key in transaction for key in ['operationAmount', 'description']) and \
            all(key in transaction['operationAmount'] for key in ['amount', 'currency']) and \
            'code' in transaction['operationAmount']['currency']
    except (TypeError, KeyError):
        return False


def convert_amount(transaction: Dict[str, Any], api_key: str = "ваш_api_ключ") -> Optional[float]:
    """
    Конвертирует сумму транзакции в рубли через API

    Args:
        transaction: Словарь с данными о транзакции
        api_key: Ключ для API (по умолчанию 'ваш_api_ключ')

    Returns:
        Сумма в рублях или None при ошибке
    """
    if not is_valid_transaction(transaction):
        return None

    try:
        amount = float(transaction["operationAmount"]["amount"])
        currency = transaction["operationAmount"]["currency"]["code"]

        if currency == "RUB":
            return amount

        response = requests.get(
            "https://api.apilayer.com/exchangerates_data/convert",
            params={
                "to": "RUB",
                "from": currency,
                "amount": amount
            },
            headers={"apikey": api_key},
            timeout=10
        )
        response.raise_for_status()
        return response.json().get("result")

    except (KeyError, ValueError, requests.RequestException):
        return None


def process_transactions(transactions: List[Dict[str, Any]], use_api: bool = False) -> List[Dict[str, Any]]:
    """
    Обрабатывает список транзакций, добавляя конвертированные суммы

    Args:
        transactions: Список транзакций
        use_api: Флаг использования реального API (False - тестовые курсы)

    Returns:
        Список транзакций с добавленными конвертированными суммами
    """
    processed = []
    test_rates = {"USD": 75.0, "EUR": 85.0, "GBP": 95.0, "RUB": 1.0}

    for tx in transactions:
        if not is_valid_transaction(tx):
            continue

        tx_copy = tx.copy()
        try:
            if use_api:
                converted = convert_amount(tx_copy)
            else:
                amount = float(tx_copy['operationAmount']['amount'])
                currency = tx_copy['operationAmount']['currency']['code'].upper()
                converted = amount * test_rates.get(currency, 1.0)

            if converted is not None:
                tx_copy['converted_amount'] = converted
                processed.append(tx_copy)
        except (KeyError, ValueError, TypeError):
            continue

    return processed


if __name__ == '__main__':
    # Пример использования
    transactions = load_transactions()

    print(f"Загружено транзакций: {len(transactions)}")
    print(f"Валидных транзакций: {sum(1 for tx in transactions if is_valid_transaction(tx))}")

    # Обработка с тестовыми курсами (без API)
    processed_offline = process_transactions(transactions, use_api=False)
    print(f"\nОбработано транзакций (оффлайн): {len(processed_offline)}")

    # Вывод первых 3 транзакций
    for tx in processed_offline[:3]:
        print(f"\nОписание: {tx.get('description', 'Нет описания')}")
        print(f"Сумма: {tx['operationAmount']['amount']} {tx['operationAmount']['currency']['code']}")
        print(f"Конвертировано: {tx.get('converted_amount', 0):.2f} RUB")
