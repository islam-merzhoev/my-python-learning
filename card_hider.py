def get_hidden_card(card_number, stars_count=4):
    stars = '*' * stars_count
    tail = card_number[-4:]
    return stars + tail
print(get_hidden_card('1234567812345678'))
print(get_hidden_card('1234567812345678', 2))
