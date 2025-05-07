import pytest
import pandas as pd
from pathlib import Path
import tempfile

# Правильный импорт функций
from src.transactions import (
    load_transactions_csv,
    load_transactions_excel,
    load_transactions
)

def test_csv_loading():
    """Тест загрузки CSV"""
    # Создаем временный CSV файл
    with tempfile.NamedTemporaryFile(suffix='.csv', mode='w', delete=False) as f:
        f.write("id,amount,category\n1,100,food\n2,200,transport")
        csv_path = f.name

    # Тестируем функцию правильно
    result = load_transactions_csv(csv_path)

    # Проверяем результаты
    assert len(result) == 2
    assert result[0]['amount'] == 100
    assert result[1]['category'] == 'transport'

    # Удаляем временный файл
    Path(csv_path).unlink()

def test_excel_loading():
    """Тест загрузки Excel"""
    # Создаем временный Excel файл
    df = pd.DataFrame({
        'id': [1, 2],
        'amount': [100, 200],
        'category': ['food', 'transport']
    })

    with tempfile.NamedTemporaryFile(suffix='.xlsx', delete=False) as f:
        df.to_excel(f.name, index=False)
        excel_path = f.name

    # Тестируем функцию правильно
    result = load_transactions_excel(excel_path)

    # Проверяем результат
    assert len(result) == 2
    assert result[0]['amount'] == 100
    assert result[1]['category'] == 'transport'

    # Удаляем временный файл
    Path(excel_path).unlink()

def test_auto_detection():
    """Тест автоопределения формата"""
    # Тестируем CSV
    with tempfile.NamedTemporaryFile(suffix='.csv', mode='w', delete=False) as f:
        f.write("id,amount\n1,100\n2,200")
        csv_path = f.name

    result = load_transactions(csv_path)
    assert len(result) == 2

    # Тестируем Excel
    df = pd.DataFrame({'id': [1], 'amount': [100]})
    with tempfile.NamedTemporaryFile(suffix='.xlsx', delete=False) as f:
        df.to_excel(f.name, index=False)
        excel_path = f.name

    result = load_transactions(excel_path)
    assert len(result) == 1

    # Удаляем временные файлы
    Path(csv_path).unlink()
    Path(excel_path).unlink()