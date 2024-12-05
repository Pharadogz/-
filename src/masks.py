def get_mask_card(card_number: str) -> str:
    """функция, маскировки номера карты"""
    new_list = list()
    new_list.append(card_number[0:4])
    new_list.append(card_number[4:6] + "**")
    new_list.append("****")
    new_list.append(card_number[12:])
    return "".join(new_list)


from typing import Any


def get_mask_account(acc_number: str) -> str:
    """Функция, маскировки номера счета"""
    new_list = list()
    new_list.append("**" + acc_number[-4:])
    return "".join(new_list)


def get_mask_card_number(card_number: Any) -> str:
    """Принимает на вход номер карты, возвращает маску карты в типе str"""
    card_number = str(card_number)
    card_number = card_number.replace(" ", "")
    if card_number.isdigit() and 12 < len(card_number) < 20:
        masked_card_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
        return str(masked_card_number)
    raise ValueError("Некорректный номер карты")


# client_acc_number = 73654108430135874305
# client_card_number = 7000792289606361
# print(get_mask_account(str(client_acc_number)))
# print(get_mask_card(str(client_card_number)))
def get_mask_account(account_number: Any) -> str:
    """Принимет номер счета, возвращает маску счета в типе str"""
    account_number = str(account_number)
    account_number = account_number.replace(" ", "")
    if account_number.isdigit() and len(account_number) == 20:
        masked_account = "**" + account_number[-4:]
        return str(masked_account)
    raise ValueError("Некорректный номер счёта")
