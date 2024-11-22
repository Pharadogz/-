from src import masks


def mask_account_card(card_info: str) -> str:
    """Принимает тип и номер карты/счета, возвращает замаскированный номер карты/счета"""
    card_infolist = card_info.split()
    if card_infolist[0] == "Счет":
        returned_number = masks.get_mask_account(card_infolist.pop(-1))
    else:
        returned_number = masks.get_mask_card_number(card_infolist.pop(-1))
    card_infolist.append(returned_number)
    masked_number = " ".join(card_infolist)
    return str(masked_number)


def get_date(core_date: str) -> str:
    """Принимает дату и время в формате ISO 8601, возвращает дату в формате ДД.ММ.ГГГГ"""
    core_date_list = core_date.split("-")
    returned_date = core_date_list[2][:2] + "." + core_date_list[1] + "." + core_date_list[0]
    return returned_date
