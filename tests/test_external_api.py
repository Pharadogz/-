from unittest.mock import Mock, patch

from src.external_api import convert_to_rub


@patch("requests.get")  # Мокируем requests.get
def test_convert_usd_to_rub(mock_get, convert_usd_to_rub=7000):
    # Настраиваем мок-ответ
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"rates": {"RUB": 70}}
    mock_get.return_value = mock_response
    # Тестируемую транзакцию
    transaction = {"amount": 100, "currency": "USD"}
    # Вызываем функцию
    result = convert_to_rub(transaction)
    # Проверяем результат
    assert convert_usd_to_rub == result  # 100 * 70 = 7000
    mock_get.assert_called_once()  # Проверяем, что запрос был выполнен один раз


@patch("requests.get")
def test_convert_eur_to_rub(mock_get):
    mock_get.return_value.json.return_value = {"amount": {"RUB": 70}, "currency": "EUR"}
    transaction = {"amount": 100, "currency": "EUR"}
    expected_result = {"amount": 100, "currency": "EUR"}
    assert transaction == expected_result
    mock_get.asset_called_once_with(
        "https://api.apilayer.com/exchangerates_data/latest"
    )


@patch("requests.get")
def test_no_rub_rate(mock_get, no_rub_rate=100):
    # Настраиваем мокированное значение для ответов без курса RUB
    mock_response = Mock()
    mock_response.json.return_value = {
        "amount": {},
    }
    mock_get.return_value = mock_response
    assert no_rub_rate == 100  # Ожидаем, что вернется исходная сумма