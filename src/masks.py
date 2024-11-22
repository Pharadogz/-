from typing import Any


def get_mask_card_number(card_number: Any) -> str:
    """Принимает на вход номер карты, возвращает маску карты в типе str"""
    card_number = str(card_number)
    masked_card_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
    return str(masked_card_number)


def get_mask_account(account_number: Any) -> str:
    """Принимет номер счета, возвращает маску счета в типе str"""
    account_number = str(account_number)
    masked_account = "**" + account_number[-4:]
    return str(masked_account)
