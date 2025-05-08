import json
import csv
import pandas as pd
from src.counter_transactions import transactions


def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def load_csv(file_path):
    with open(file_path, newline="", encoding="utf-8") as csvfile:
        return list(csv.DictReader(csvfile))


def load_xlsx(file_path):
    df = pd.read_excel(file_path)
    return df.to_dict(orient="records")


def filter_transactions(transactions, status):
    return [
        transaction
        for transaction in transactions
        if transaction.get("status", "").lower() == status.lower()
    ]


def sort_transactions(transactions, ascending):
    return sorted(transactions, key=lambda x: x["date"], reverse=not ascending)


def filter_by_keyword(transactions, keyword):
    return [
        transaction
        for transaction in transactions
        if keyword.lower() in transaction.get("description", "").lower()
    ]


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ")

    if choice == "1":
        print("Для обработки выбран JSON-файл")
    elif choice == "2":
        print("Для обработки выбран CSV-файл")
    elif choice == "3":
        print("Для обработки выбран XLSX-файл")
    else:
        print("Некорректный выбор. Завершение программы.")
        return

    statuses = {"EXECUTED", "CANCELED", "PENDING"}
    filtered_transactions = transactions.copy()

    status = input(
        "Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\nПользователь: "
    )
    if status.upper() in statuses:
        print(f'Операции отфильтрованы по статусу "{status.upper()}"')
    else:
        print(f'Статус операции "{status}" недоступен.')

    sort_choice = (
        input("Отсортировать операции по дате? Да/Нет\nПользователь: ").strip().lower()
    )
    if sort_choice == "да":
        result = (
            input("Отсортировать по возрастанию или по убыванию? \nПользователь: ")
            .strip()
            .lower()
        )
        if result == "по возрастанию":
            print("по возрастанию")
        else:
            print("по убыванию")

    currency_filter = (
        input("Выводить только рублевые транзакции? Да/Нет\nПользователь: ")
        .strip()
        .lower()
    )
    if currency_filter == "да":
        filtered_transactions = [
            transaction
            for transaction in filtered_transactions
            if str(transaction.get("amount", "")).endswith("руб")
        ]

    keyword_filter = (
        input(
            "Отфильтровать список транзакций по определенному слову в описании? Да/Нет\nПользователь: "
        )
        .strip()
        .lower()
    )
    if keyword_filter == "да":
        keyword = input("Введите слово для фильтрации по описанию: ")
        filtered_transactions = filter_by_keyword(filtered_transactions, keyword)
        print("Распечатываю итоговый список транзакций...")

    if filtered_transactions:
        print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
        for transaction in filtered_transactions:
            # Используем get() с значением по умолчанию
            date = transaction.get('date', 'Дата не указана')
            description = transaction.get('description', 'Описание отсутствует')
            account = transaction.get('account', 'Счет не указан')
            amount = transaction.get('amount', 'Сумма не указана')

            print(f"{date} {description}")
            print(f"Счет {account}")
            print(f"Сумма: {amount}")
            print()
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


if __name__ == "__main__":
    main()