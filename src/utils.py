import logging
from pathlib import Path
from unittest.mock import patch, MagicMock

import pytest

from src.external_api import convert_amount


# Настройка логирования для тестов
def setup_test_logging() -> object:
    """Настройка системы логирования для тестов"""
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)

    log_file = logs_dir / "test_external_api.log"

    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file, mode='w'),  # Перезаписываем файл при каждом запуске
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)


logger = setup_test_logging()

@patch('requests.request')
def test_convert_amount(mock_request):
    """Тестирование функции конвертации суммы транзакции"""
    try:
        logger.info("Начало теста test_convert_amount")

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

        logger.debug(f"Тестовые данные: {transaction_test}")

        # 1. Настраиваем мок
        mock_response = MagicMock()
        mock_response.json.return_value = {"result": 15000.00}  # Пример курса 1 USD = 75 RUB
        mock_request.return_value = mock_response
        logger.debug("Mock для requests.request успешно настроен")

        # 2. Вызываем функцию
        result = convert_amount(transaction_test)
        logger.info(f"Результат конвертации: {result}")

        # 3. Проверяем, что запрос был отправлен с правильными параметрами
        expected_url = (
            "https://api.apilayer.com/exchangerates_data/convert"
            f"?to=RUB&from=USD&amount=200.00"
        )
        mock_request.assert_called_once_with(
            "GET",
            expected_url,
            headers={"apikey": "ваш_api_ключ"},
            timeout=10
        )
        logger.debug("Проверка параметров запроса прошла успешно")

        # 4. Проверяем результат конвертации
        assert result == 15000.00
        logger.info("Тест test_convert_amount завершен успешно")

    except Exception as e:
        logger.error(f"Ошибка в тесте test_convert_amount: {str(e)}", exc_info=True)
        raise


if __name__ == "__main__":
    pytest.main(["-v"])
