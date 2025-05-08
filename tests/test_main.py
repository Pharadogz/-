import unittest
from unittest.mock import mock_open, patch

import pandas as pd

from src.main import (
    filter_by_keyword,
    filter_transactions,
    load_csv,
    load_json,
    load_xlsx,
    sort_transactions,
)


@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data='[{"status": "EXECUTED", "description": "Sample transaction"}]',
)
def test_load_json(mock_file):
    result = load_json("dummy_path.json")
    expected = [{"status": "EXECUTED", "description": "Sample transaction"}]
    assert result == expected
    mock_file.assert_called_once_with("dummy_path.json", "r", encoding="utf-8")


@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data="description,status\nSample transaction,EXECUTED\nAnother transaction,CANCELED",
)
def test_load_csv(mock_file):
    result = load_csv("dummy_path.csv")
    expected = [
        {"description": "Sample transaction", "status": "EXECUTED"},
        {"description": "Another transaction", "status": "CANCELED"},
    ]
    assert result == expected
    mock_file.assert_called_once_with("dummy_path.csv", newline="", encoding="utf-8")


@patch("pandas.read_excel")
def test_load_xlsx(mock_read_excel):
    mock_read_excel.return_value = pd.DataFrame(
        {"description": ["Sample transaction"], "status": ["EXECUTED"]}
    )
    result = load_xlsx("dummy_path.xlsx")
    expected = [{"description": "Sample transaction", "status": "EXECUTED"}]
    assert result == expected
    mock_read_excel.assert_called_once_with("dummy_path.xlsx")


def test_filter_transactions():
    transactions = [
        {"status": "EXECUTED"},
        {"status": "CANCELED"},
        {"status": "PENDING"},
    ]
    result = filter_transactions(transactions, "executed")
    expected = [{"status": "EXECUTED"}]
    assert result == expected


def test_sort_transactions():
    transactions = [
        {"date": "2023-01-02"},
        {"date": "2023-01-01"},
        {"date": "2023-01-03"},
    ]
    result_asc = sort_transactions(transactions, ascending=True)
    result_desc = sort_transactions(transactions, ascending=False)

    assert result_asc[0]["date"] == "2023-01-01"
    assert result_desc[0]["date"] == "2023-01-03"


def test_filter_by_keyword():
    transactions = [
        {"description": "Buy fruits"},
        {"description": "Do not eat bread"},
        {"description": "Sell clothes"},
    ]
    result = filter_by_keyword(transactions, "bread")
    expected = [{"description": "Do not eat bread"}]
    assert result == expected


if __name__ == "__main__":
    unittest.main()