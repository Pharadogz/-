from typing import Any


def get_mask_card_number(card_number: Any) -> str:
    """Принимает на вход номер карты, возвращает маску карты в типе str"""
    card_number = str(card_number)
    card_number = card_number.replace(" ", "")
    if card_number.isdigit() and 12 < len(card_number) < 20:
        masked_card_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
        return str(masked_card_number)
    raise ValueError("Некорректный номер карты")


def get_mask_account(account_number: Any) -> str:
    """Принимет номер счета, возвращает маску счета в типе str"""
    account_number = str(account_number)
    account_number = account_number.replace(" ", "")
    if account_number.isdigit() and len(account_number) == 20:
        masked_account = "**" + account_number[-4:]
        return str(masked_account)
    raise ValueError("Некорректный номер счета")