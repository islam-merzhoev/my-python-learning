nickname = input('Введите ваш ник: ')
print(f'Ваш ник: {nickname}')
wins = int(input('Сколько побед? '))
loses = int(input('Сколько поражений? '))
total_games = wins + loses
win_rate = (wins / total_games) * 100
win_rate_rounded = round(win_rate, 1)
print(f"Всего игр: {total_games}, Винрейт: {win_rate_rounded}%")
