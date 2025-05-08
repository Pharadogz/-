import pytest

from src.processing import filter_by_state, sort_by_date


# Параметризация тестов для различных значений статуса
@pytest.mark.parametrize(
    "state, expected_result",
    [
        ("EXECUTED", [{"id": 1, "state": "EXECUTED"}, {"id": 3, "state": "EXECUTED"}]),
        ("PENDING", [{"id": 2, "state": "PENDING"}]),
        ("CANCELLED", [{"id": 4, "state": "CANCELLED"}]),
    ],
)
def test_filter_by_state(sample_data, state, expected_result):
    assert filter_by_state(sample_data, state) == expected_result


def test_filter_by_state_empty(empty_data):
    assert filter_by_state(empty_data, "EXECUTED") == []


# Параметризация тестов для проверки сортировки
@pytest.mark.parametrize(
    "sort_arg, expected_result",
    [
        (
            True,
            [
                {"id": 1, "date": "2023-10-05"},
                {"id": 3, "date": "2023-10-01"},
                {"id": 4, "date": "2023-09-20"},
                {"id": 2, "date": "2023-09-15"},
            ],
        ),
        (
            False,
            [
                {"id": 2, "date": "2023-09-15"},
                {"id": 4, "date": "2023-09-20"},
                {"id": 3, "date": "2023-10-01"},
                {"id": 1, "date": "2023-10-05"},
            ],
        ),
    ],
)
def test_sort_by_date(sample_date, sort_arg, expected_result):
    assert sort_by_date(sample_date, sort_arg) == expected_result


def test_sort_by_date_empty(empty_info):
    assert sort_by_date(empty_info) == []


def test_sort_by_date_same_dates(same_date_info):
    expected_result = [
        {"id": 1, "date": "2023-10-05"},
        {"id": 2, "date": "2023-10-05"},
    ]
    assert sort_by_date(same_date_info) == expected_result