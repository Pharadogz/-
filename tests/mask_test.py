"""Ввод номера карты"""
greeting_carts = 'Введите номер карты:'
print(greeting_carts)


def get_mask_card_number(card, stars=2) -> str:
    """Маскинг номера"""
    return (f"{card.replace(' ', '')[:4]} "
            f"{card.replace(' ', '')[4:6]}{'*' * stars} "
            f"{card.replace(' ', '')[-4:]}")


print(get_mask_card_number("7000792289606361"))

"""Ввод номера счёта"""
greeting_account = 'Введите номер счёта:'
print(greeting_account)


def get_mask_account_number(card, stars=2) -> str:
    """Маскинг номера"""
    return f"{'*' * stars}{card.replace(' ', '')[-4:]}"


print(get_mask_account_number("73654108430135874305"))