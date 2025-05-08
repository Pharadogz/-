from src.search_transactions import search_transactions


def test_search_matching_transactions():
    transactions = [
        {"id": 1, "description": "Оплата за услуги", "amount": 100},
        {"id": 2, "description": "Покупка товара", "amount": 200},
        {"id": 3, "description": "Оплата за интернет", "amount": 50},
    ]
    search_string = "оплата"
    expected_result = [
        {"id": 1, "description": "Оплата за услуги", "amount": 100},
        {"id": 3, "description": "Оплата за интернет", "amount": 50},
    ]
    result = search_transactions(transactions, search_string)
    assert result == expected_result


def test_search_no_matching_transactions():
    transactions = [
        {"id": 1, "description": "Оплата за услуги", "amount": 100},
        {"id": 2, "description": "Покупка товара", "amount": 200},
        {"id": 3, "description": "Оплата за интернет", "amount": 50},
    ]
    search_string = "отмена"
    expected_result = []
    result = search_transactions(transactions, search_string)
    assert result == expected_result


def test_search_empty_transactions():
    search_string = "оплата"
    result = search_transactions([], search_string)
    assert result == []


def test_search_no_description():
    transactions_with_no_description = [
        {"id": 1, "amount": 100},
        {"id": 2, "description": "Покупка товара", "amount": 200},
        {"id": 3, "description": "Оплата за интернет", "amount": 50},
    ]
    search_string = "оплата"
    expected_result = [
        {"id": 3, "description": "Оплата за интернет", "amount": 50},
    ]
    result = search_transactions(transactions_with_no_description, search_string)
    assert result == expected_result


if __name__ == "__main__":
    test_search_matching_transactions()
    test_search_no_matching_transactions()
    test_search_empty_transactions()
    test_search_no_description()
    print("Все тесты пройдены успешно!")