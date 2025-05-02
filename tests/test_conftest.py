import pytest
from datetime import datetime


def test_numbers_16(numbers_16):
    """Проверка, что фикстура возвращает строку с 16 цифрами."""
    assert isinstance(numbers_16, str)
    assert len(numbers_16) == 16
    assert numbers_16.isdigit()


def test_numbers_16_spases(numbers_16_spases):
    """Проверка, что фикстура возвращает строку с 16 цифрами и пробелами."""
    assert isinstance(numbers_16_spases, str)
    # Удаляем пробелы и проверяем длину
    assert len(numbers_16_spases.replace(" ", "")) == 16
    # Проверяем, что остаются только цифры и пробелы
    assert all(c.isdigit() or c.isspace() for c in numbers_16_spases)


def test_numbers_16_int(numbers_16_int):
    """Проверка, что фикстура возвращает целое число с 16 цифрами."""
    assert isinstance(numbers_16_int, int)
    assert len(str(numbers_16_int)) == 16


def test_numbers_20(numbers_20):
    """Проверка, что фикстура возвращает строку с 20 цифрами."""
    assert isinstance(numbers_20, str)
    assert len(numbers_20) == 20
    assert numbers_20.isdigit()


def test_numbers_20_spases(numbers_20_spases):
    """Проверка, что фикстура возвращает строку с 20 цифрами и пробелами."""
    assert isinstance(numbers_20_spases, str)
    assert len(numbers_20_spases.replace(" ", "")) == 20
    assert all(c.isdigit() or c.isspace() for c in numbers_20_spases)


def test_numbers_20_int(numbers_20_int):
    """Проверка, что фикстура возвращает целое число с 20 цифрами."""
    assert isinstance(numbers_20_int, int)
    assert len(str(numbers_20_int)) == 20


def test_numbers_19(numbers_19):
    """Проверка, что фикстура возвращает строку с 19 цифрами."""
    assert isinstance(numbers_19, str)
    assert len(numbers_19) == 19
    assert numbers_19.isdigit()


def test_numbers_21(numbers_21):
    """Проверка, что фикстура возвращает строку с 21 цифрой."""
    assert isinstance(numbers_21, str)
    assert len(numbers_21) == 21
    assert numbers_21.isdigit()


def test_numbers_13(numbers_13):
    """Проверка, что фикстура возвращает строку с 13 цифрами."""
    assert isinstance(numbers_13, str)
    assert len(numbers_13) == 13
    assert numbers_13.isdigit()


def test_numbers_12(numbers_12):
    """Проверка, что фикстура возвращает строку с 12 цифрами."""
    assert isinstance(numbers_12, str)
    assert len(numbers_12) == 12
    assert numbers_12.isdigit()


def test_letters(letters):
    """Проверка, что фикстура возвращает строку с буквами."""
    assert isinstance(letters, str)
    assert not letters.isdigit()
    assert any(c.isalpha() for c in letters)


def test_numbers_and_letters(numbers_and_letters):
    """Проверка, что фикстура возвращает строку с цифрами и буквами."""
    assert isinstance(numbers_and_letters, str)
    assert any(c.isdigit() for c in numbers_and_letters)
    assert any(c.isalpha() for c in numbers_and_letters)


def test_blank(blank):
    """Проверка, что фикстура возвращает пустую строку."""
    assert isinstance(blank, str)
    assert len(blank) == 0


def test_test_dict_list(test_dict_list):
    """Проверка, что фикстура возвращает список словарей с корректными данными."""
    assert isinstance(test_dict_list, list)
    for item in test_dict_list:
        assert isinstance(item, dict)
        assert 'id' in item and isinstance(item['id'], int)
        assert 'state' in item and item['state'] in ('EXECUTED', 'CANCELED')
        assert 'date' in item
        # Проверяем, что дата в ISO формате
        try:
            datetime.fromisoformat(item['date'])
        except ValueError:
            pytest.fail(f"Неверный формат даты: {item['date']}")


def test_test_dict_list_incorrect_date(test_dict_list_incorrect_date):
    """Проверка, что фикстура возвращает список словарей с некорректными датами."""
    assert isinstance(test_dict_list_incorrect_date, list)
    for item in test_dict_list_incorrect_date:
        assert isinstance(item, dict)
        assert 'date' in item
        # Проверяем, что дата НЕ в ISO формате
        with pytest.raises(ValueError):
            datetime.fromisoformat(item['date'])


def test_test_dict_list_incorrect_date_second_version(test_dict_list_incorrect_date_second_version):
    """Проверка альтернативной фикстуры с некорректными датами."""
    assert isinstance(test_dict_list_incorrect_date_second_version, list)
    for item in test_dict_list_incorrect_date_second_version:
        assert isinstance(item, dict)
        assert 'date' in item
        # Проверяем, что дата НЕ в ISO формате
        with pytest.raises((ValueError, TypeError)):
            datetime.fromisoformat(item['date'])