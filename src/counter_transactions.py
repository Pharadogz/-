from collections import Counter
from typing import List, Dict


def count_transactions_by_category(
    transactions: List[dict], categories: List[str]
) -> Dict[str, int]:
    """
    Функция для подсчета количества банковских операций по категориям.
    """
    # Создаем счетчик для операций
    category_counter = Counter()
    # Подсчитываем количество операций по категориям
    for transaction in transactions:
        if "description" in transaction:  # Проверяем наличие поля description
            description = transaction["description"]
            # Увеличиваем счетчик для каждой категории
            category_counter[description] += 1
    # Оставляем только те категории, которые указаны в списке categories
    result = {category: category_counter[category] for category in categories}

    return result


# Пример использования
transactions = [
    {"id": 1, "description": "Оплата за услуги", "amount": 100},
    {"id": 2, "description": "Покупка товара", "amount": 2000},
    {"id": 3, "description": "Оплата за интернет", "amount": 350},
    {"id": 4, "description": "Оплата за услуги", "amount": 150},
]

categories = [
    "Оплата за услуги",
    "Покупка товара",
    "Оплата за интернет",
    "Неправильная категория",
]

# Подсчитываем количество транзакций по категориям
transaction_counts = count_transactions_by_category(transactions, categories)

# Вывод результата
print(transaction_counts)