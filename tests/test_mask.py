import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_numbers(numbers_16):
    assert get_mask_card_number(numbers_16) == "7000 79** **** 6361"


def test_get_mask_card_numbers_with_spaces(numbers_16):
    assert get_mask_card_number(numbers_16) == "7000 79** **** 6361"


def test_get_mask_card_number_int(numbers_16_int):
    assert get_mask_card_number(numbers_16_int) == "7000 79** **** 6361"


def test_get_mask_card_number_maxnumber(numbers_19):
    assert get_mask_card_number(numbers_19) == "7000 79** **** 1123"


def test_get_mask_card_number_minnumber(numbers_13):
    assert get_mask_card_number(numbers_13) == "7000 79** **** 9606"


def test_get_mask_account(numbers_20):
    assert get_mask_account(numbers_20) == "**1234"


def test_get_mask_account_with_spaces(numbers_20):
    assert get_mask_account(numbers_20) == "**1234"


def test_get_mask_account_int(numbers_20_int):
    assert get_mask_account(numbers_20_int) == "**1234"
