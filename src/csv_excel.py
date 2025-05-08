import csv
import pandas as pd


def read_financial_operations_csv(file_path):
    """Данная функция  считывает финансовые операции из CSV файла"""
    operations = []

    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")

            for row in reader:
                operation = {
                    "id": row.get("id", ""),
                    "state": row.get("state", ""),
                    "date": row.get("date", ""),
                    "amount": row.get("amount", ""),
                    "currency_name": row.get("currency_name", ""),
                    "currency_code": row.get("currency_code", ""),
                    "from": row.get("from", ""),
                    "to": row.get("to", ""),
                    "description": row.get("description", ""),
                }
                operations.append(operation)

    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return []
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return []

    return operations


# Пример использования
file_path = "transactions.csv"
operations = read_financial_operations_csv(file_path)
print(operations)


def read_financial_operations_excel(file_path):
    """Данная функция считывает финансовые операции из Excel файла и возвращает список словарей."""
    try:
        # Считываем данные из Excel файла
        df = pd.read_excel(file_path)
        # Проверяем, что DataFrame не пустой
        if df.empty:
            raise ValueError("Файл пустой или не содержит данные.")

        # Преобразуем DataFrame в список словарей
        transactions = df.to_dict(orient="records")
        return transactions

    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}' не найден.")
        return []
    except ValueError as e:
        print(f"Ошибка: {e}")
        return []
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
        return []


# Пример использования
file_path = "transactions_excel.xlsx"
transactions = read_financial_operations_excel(file_path)

for transaction in transactions:
    print(transaction)