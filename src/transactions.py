from pathlib import Path
from typing import List, Dict

import pandas as pd

from src.generators import transactions


def load_transactions_csv(file_path: str) -> List[Dict]:
    """Чтение транзакций из CSV файлов"""
    try:
        df = pd.read_csv(file_path)
        return df.to_dict('records')
    except Exception as e:
        print(f"Ошибка чтения CSV: {e}")
        return []


def load_transactions_excel(file_path: str) -> List[Dict]:
    """Чтение транзакций из Excel файла"""
    try:
        df = pd.read_excel(file_path)
        return df.to_dict('records')
    except Exception as e:
        print(f"Ошибка чтения Excel: {e}")
        return []


def load_transactions(file_path: str) -> List[Dict]:
    """Автоматическое определение формата и чтение файла"""
    path = Path(file_path)
    if path.suffix.lower() == '.csv':
        return load_transactions_csv(file_path)
    elif path.suffix.lower() in ('.xlsx', '.xls'):
        return load_transactions_excel(file_path)
    else:
        print(f"Неподдерживаемый формат файла: {path.suffix}")
        return []


# Пример использования
if __name__ == '__main__':
    transactions_path = Path(__file__).parent / 'data' / 'transactions_lib'

    print(f"Загружено {len(transactions)} транзакций из CSV")
    print(f"Загружено {len(transactions)} транзакций из Excel")
