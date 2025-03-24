from unittest.mock import patch, MagicMock
import pytest
import requests

from src.external_api import convert_amount


@patch('requests.request')
def test_convert_amount(mock_request):
    # Тестовые данные
    transaction_test = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": 200.00,
            "currency": {
                "name": "руб.",
                "code": "USD"  # Меняем на USD для теста конвертации
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }

    # 1. Настраиваем мок
    mock_response = MagicMock()
    mock_response.json.return_value = {"result": 15000.00}  # Пример курса 1 USD = 75 RUB
    mock_request.return_value = mock_response

    # 2. Вызываем функцию
    result = convert_amount(transaction_test)

    # 3. Проверяем, что запрос был отправлен с правильными параметрами
    expected_url = (
        "https://api.apilayer.com/exchangerates_data/convert"
        f"?to=RUB&from=USD&amount=200.00"
    )
    mock_request.assert_called_once_with(
        "GET",
        expected_url,
        headers={"apikey": "ваш_api_ключ"},  # Укажите настоящий ключ или используйте мок
        timeout=10
    )

    # 4. Проверяем результат конвертации
    assert result == 15000.00
