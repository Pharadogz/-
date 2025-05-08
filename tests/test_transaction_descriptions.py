import pytest

from src.generators import transaction_descriptions


# Параметризованный тест для проверки корректных описаний
@pytest.mark.parametrize(
    "expected",
    [
        [
            "Перевод организации",
            "Перевод со счета на счет",
            "Перевод со счета на счет",
            "Перевод с карты на карту",
            "Перевод организации",
        ],
    ],
)
def test_transaction_descriptions(transactions_data, expected):
    descriptions_gen = transaction_descriptions(transactions_data)
    descriptions = list(descriptions_gen)
    assert descriptions == expected


# Тестирование работы генератора с пустым списком
def test_transaction_descriptions_empty():
    descriptions_gen = transaction_descriptions([])
    descriptions = list(descriptions_gen)
    assert descriptions == []  # Ожидаем пустой список


# Тестирование работы генератора с неполными транзакциями
def test_transaction_descriptions_incomplete(transactions_data):
    incomplete_data = transactions_data[:-1]  # Удаляем последнюю транзакцию
    descriptions_gen = transaction_descriptions(incomplete_data)
    descriptions = list(descriptions_gen)
    assert descriptions == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
    ]


def test_transaction_descriptions_single():
    single_transaction = [{"description": "Перевод организации"}]
    generated_descriptions = list(transaction_descriptions(single_transaction))
    assert generated_descriptions == ["Перевод организации"]