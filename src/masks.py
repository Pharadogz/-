import logging
from pathlib import Path
from typing import Any
from datetime import datetime


# Настройка логирования
def setup_logging():
    """Настройка системы логирования"""
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)

    log_file = logs_dir / f"masking_{datetime.now().strftime('%Y%m%d')}.log"

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file, mode='w'),  # Перезаписываем файл при каждом запуске
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)


logger = setup_logging()


def get_mask_card(card_number: str) -> str:
    """Функция маскировки номера карты"""
    try:
        card_number = str(card_number).replace(" ", "")
        if card_number.isdigit() and 12 < len(card_number) < 20:
            pass
        else:
            raise ValueError("Некорректный номер карты")

        masked = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        logger.info(f"Успешная маскировка карты: {masked}")
        return masked
    except Exception as e:
        logger.error(f"Ошибка маскировки карты: {e}", exc_info=True)
        raise


def get_mask_account(account_number: Any) -> str:
    """Функция маскировки номера счета"""
    try:
        account_number = str(account_number).replace(" ", "")
        if not (account_number.isdigit() and len(account_number) == 20):
            raise ValueError("Некорректный номер счёта")

        masked = f"**{account_number[-4:]}"
        logger.info(f"Успешная маскировка счета: {masked}")
        return masked
    except Exception as e:
        logger.error(f"Ошибка маскировки счета: {e}", exc_info=True)
        raise


# Пример использования
if __name__ == "__main__":
    try:
        print(get_mask_card("1234567890123456"))  # "1234 56** **** 3456"
        print(get_mask_account("12345678901234567890"))  # "**7890"

        # Тест с ошибкой
        print(get_mask_card("123"))  # Вызовет исключение и запишет в лог
    except Exception:
        pass  # Ошибки уже логируются


