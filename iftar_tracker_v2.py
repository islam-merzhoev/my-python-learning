hours = int(input('Сколько часов осталось до Ифтара?'))
if hours == 0:
    print('Приятного аппетита!')
elif hours == 1:
    print('Последний час, сабр!')
elif hours < 5:
    print('Скоро Финиш!')
else:
    print('До контрольной отметки осталось:', hours - 5, 'ч.')
