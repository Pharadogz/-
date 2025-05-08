def filter_by_currency(transactions, currency):
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions):
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start, end):
    for number in range(start, end + 1):
        # Форматируем номер карты в виде XXXX XXXX XXXX XXXX
        card_number = f"{number:0>16}"
        formatted_card_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        yield formatted_card_number