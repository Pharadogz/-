from src.masks import get_mask_account, get_mask_card


def mask_account_card(info: str) -> str:
    """Разделяем тип и номер"""
    parts = info.split()
    card_type = " ".join(parts[:-1])  # Все, кроме последнего элемента
    number = parts[-1]  # Последний элемент - номер
    # Используем импортированные функции для маскировки
    if "Счет" in card_type:
        masked_number = get_mask_account(number)  # Используем get_mask_account
    else:
        masked_number = get_mask_card(number)  # Используем get_mask_card_number
    return f"{card_type} {masked_number}"


def get_date(date: str) -> str:
    """Разделяем строку на дату и время"""
    date_part = date.split("T")[0]
    year, month, day = date_part.split("-")
    return f"{day}.{month}.{year}"  # Форматируем дату в нужный формат