from src.masks import get_mask_account, get_mask_card_number


# Тесты для маскировки номера карты
def test_standard_case(card_numbers):
    """Проверяем простой случай с 16-значным номером карты"""
    assert get_mask_card_number(card_numbers["standard"]) == "7000 79** **** 6361"


def test_short_card_number(card_numbers):
    """Проверяем, как функция обработает короткий номер карты (то есть менее 6 цифр)"""
    assert get_mask_card_number(card_numbers["short"]) == "7000"


def test_edge_case(card_numbers):
    """Проверяем, как функция обрабатывает номер карты ровно из 6 цифр"""
    assert get_mask_card_number(card_numbers["edge"]) == "7869 00"


def test_empty_string(card_numbers):
    """Проверяем, как функция обрабатывает пустую строку"""
    assert get_mask_card_number(card_numbers["empty"]) == ""


def test_various_lengths(card_numbers):
    assert get_mask_card_number(card_numbers["various"]) == "1234 56** 9012"


# Тесты для маскировки номера счета
def test_get_mask_account(account_numbers):
    """Проверяем обычный номер счета"""
    assert get_mask_account(account_numbers["standard"]) == "**9012"


def test_less_than_four_symbol_mask_account(account_numbers):
    for number in account_numbers["less_than_four"]:
        assert get_mask_account(number) == number


def test_empty_string_mask_account(account_numbers):
    assert get_mask_account(account_numbers["empty"]) == ""