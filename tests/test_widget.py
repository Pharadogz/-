import pytest

from src.widget import get_date, mask_account_card


# Тесты для функции mask_account_card
def test_mask_account_card(account_card_data):
    for input_data, expected_result in account_card_data:
        assert mask_account_card(input_data) == expected_result


def test_mask_account_card_invalid(invalid_account_card_data):
    for input_data in invalid_account_card_data:
        with pytest.raises(IndexError):
            mask_account_card(input_data)


# Тесты для функции get_date
def test_get_date(date_data):
    for input_date, expected_result in date_data:
        assert get_date(input_date) == expected_result


def test_get_date_invalid(invalid_date_data):
    for input_date in invalid_date_data:
        with pytest.raises(ValueError):
            get_date(input_date)

@pytest.mark.parametrize(
    "value, expected",
    [
        ("Visa Platinum ", "Номер карты не указан"),
        ("Счёт ", "Номер счета не указан"),
        ("", "Нет данных"),
        ("1", "Некорректный номер карты"),
    ],
)
def test_mask_account_card_valueerror(value, expected):
    with pytest.raises(ValueError):
        mask_account_card(value) == expected


@pytest.mark.parametrize(
    "value, expected", [("2024-03-11T02:26:18.671407", "11.03.2024"),
                        ("2024-08-06", "06.08.2024")]
)
def test_get_date(value, expected):
    assert get_date(value) == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        ("20/12/2023", "Некорректный формат даты"),
        ("06.05.2021", "Некорректный формат даты"),
        ("Двадцать второе июня сорок первого года",
         "Некорректный формат даты"),
        ("aa-bb-cc", "Некорректный формат даты"),
        ("", "Некорректный формат даты"),
    ],
)
def test_get_date_valueerror(value, expected):
    with pytest.raises(ValueError):
        var = expected == get_date(value)
