import logging
from pathlib import Path
from unittest.mock import patch, MagicMock
import pytest
import requests

from src.external_api import convert_amount


def setup_test_logging():
    """Настройка системы логирования для тестов"""
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)

    log_file = logs_dir / "test_external_api.log"

    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file, mode='w'),
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
            "operationAmount": {
                "amount": 200.00,
                "currency": {
                    "code": "USD"
                }
            }
        }

        # Настраиваем мок
        mock_response = MagicMock()
        mock_response.json.return_value = {"result": 15000.00}
        mock_request.return_value = mock_response

        # Вызываем функцию
        result = convert_amount(transaction_test)

        # Проверяем вызов API
        mock_request.assert_called_once_with(
            "GET",
            "https://api.apilayer.com/exchangerates_data/convert",
            params={"to": "RUB", "from": "USD", "amount": 200.00},
            headers={"apikey": "ваш_api_ключ"},
            timeout=10
        )

        # Проверяем результат
        assert result == 15000.00
        logger.info("Тест пройден успешно")

    except Exception as e:
        logger.error(f"Ошибка в тесте: {str(e)}", exc_info=True)
        raise
