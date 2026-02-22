now_text = input("Сколько сейчас часов?")
now_num = int(now_text)
iftar_text = input("Во сколько время Ифтара?")
iftar_num = int(iftar_text)
result = iftar_num - now_num
print(f'До Ифтара осталось: {result}')
