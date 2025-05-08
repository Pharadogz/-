import json
import logging
import os

# Настройка логирования
logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)  # Уровень не ниже DEBUG

# Настройка обработчика для записи логов в файл
file_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

# Настройка формата записей в логе
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formatter)

# Добавление обработчика к логгеру
logger.addHandler(file_handler)


def read_json_transactions(file_path: str) -> list:
    """Читает JSON-файл и возвращает список словарей с данными о финансовых транзакциях.

    :param file_path: str, путь к JSON-файлу
    :return: list, список словарей с финансовыми транзакциями или пустой список
    """
    logger.debug(f"Проверка существования файла: {file_path}")

    if not os.path.isfile(file_path):
        logger.warning(f"Файл отсутствует: {file_path}")
        return []

    try:
        logger.debug(f"Открытие файла: {file_path}")
        with open(file_path, "r") as f:
            data = json.load(f)
            logger.debug("Чтение данных из файла прошло успешно.")

            # Проверка, содержит ли данные список
            if isinstance(data, list):
                logger.info(f"Успешное чтение данных из файла: {file_path}")
                return data
            else:
                logger.warning(f"Данные в файле {file_path} не являются списком")
                return []
    except json.JSONDecodeError as e:
        logger.error(f"Ошибка декодирования JSON в файле {file_path}: {e}")
        return []
    except Exception as e:
        logger.error(f"При чтении файла произошла ошибка {file_path}: {e}")
        return []


if __name__ == "__main__":
    json_file_path = "path/to/your/transactions.json"
    transactions = read_json_transactions(json_file_path)
    if transactions:
        print("Транзакции успешно загружены.")
    else:
        print("Не удалось загрузить транзакции.")