def get_hidden_nickname(name, stars=3):
    return name[:2] + '*' * stars
print(get_hidden_nickname('Islam_51'))
print(get_hidden_nickname('Legend', 5))
