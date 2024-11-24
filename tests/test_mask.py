import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_numbers(numbers_16):
    assert get_mask_card_number(numbers_16) == "7000 79** **** 6361"


def test_get_mask_card_numbers_with_spaces(numbers_16_spases):
    assert get_mask_card_number(numbers_16_spases) == "7000 79** **** 6361"


def test_get_mask_card_number_int(numbers_16_int):
    assert get_mask_card_number(numbers_16_int) == "7000 79** **** 6361"


def test_get_mask_card_number_maxnumber(numbers_19):
    assert get_mask_card_number(numbers_19) == "7000 79** **** 1123"


def test_get_mask_card_number_minnumber(numbers_13):
    assert get_mask_card_number(numbers_13) == "7000 79** **** 9606"


def test_get_mask_account(numbers_20):
    assert get_mask_account(numbers_20) == "**1234"


def test_get_mask_account_with_spaces(numbers_20_spases):
    assert get_mask_account(numbers_20_spases) == "**1234"


def test_get_mask_account_int(numbers_20_int):
    assert get_mask_account(numbers_20_int) == "**1234"


@pytest.mark.parametrize("value, expected", [
    ("7000792289606361", "Некорректный номер счета"),
    ("7000792289606361123", "Некорректный номер счета"),
    ("Тестовые_буквы", "Некорректный номер счета"),
    ("a1b2c3d4e5f6g7h8i9j0", "Некорректный номер счета"),
    ("", "Некорректный номер счета"),
    ("700079228960636112345", "Некорректный номер счета"),
])
def test_get_mask_account_valueerror(value, expected):
    with pytest.raises(ValueError):
        get_mask_account(value) == expected