import json
import os


def load_transactions():
    if not os.path.isfile('operations.json'):
        return []

    with open('operations.json', 'r', encoding='utf-8') as file:
        try:
            transactions = json.load(file)
            if isinstance(transactions, list):
                return transactions
        except json.JSONDecodeError:
            return []

    return []


print(load_transactions())
