"""
+-----------------------------------------------+
|					CLASS WORK					|
+-----------------------------------------------+
"""

# time = input('Введите время суток: ').lower()

# if time == 'morning' or time == 'утро':
# 	print('Good morning!')
# elif time == 'day' or time == 'день':
# 	print('Good afternoon!')
# elif time == 'evening' or time == 'вечер':
# 	print('Good evening!')
# else:
# 	print('Время неизвестно...')

# print('hello' if False else 'bye')

#+----------------------------+#

# temperature = int(input('Введите температуру: '))

# if 0 >= temperature >= -20:
# 	print(f'{temperature}℃ это ХОЛОДНО')
# elif 15 >= temperature >= 1:
# 	print(f'{temperature}℃ это ПРОХЛАДНО')
# elif 25 >= temperature >= 16:
# 	print(f'{temperature}℃ это TЕПЛО')
# elif 40 >= temperature >= 26:
# 	print(f'{temperature}℃ это ЖАРКО')
# else:
# 	print(f'Температура {temperature}℃ это сметртельно для человека')

#+----------------------------+#

# monday = int(input('Понедельник: '))
# tuesday = int(input('Вторник: '))
# wednesday = int(input('Среда: '))
# thursday = int(input('Четверг: '))
# friday = int(input('Пятница: '))
# saturday = int(input('Суббота: '))
# sunday = int(input('Вокресенье: '))

# amount_of_expenses = monday + tuesday + wednesday + thursday + friday + saturday + sunday
# print(f'Общая сумма расходов: {amount_of_expenses}')

# average_consumption = round((amount_of_expenses / 7), 1)
# print(f'Средний расход в день: {average_consumption}')

# if 1 <= amount_of_expenses <= 500:
# 	print('Мало')
# elif 501 <= amount_of_expenses <= 700:
# 	print('Среднее')
# elif 701 <= amount_of_expenses:
# 	print('Много')
# else:
# 	print('Ничего не потрачено')
	


"""
+-----------------------------------------------+
|					HOME WORK					|
+-----------------------------------------------+
"""

USER = '\033[96m'+ '\033[1m' 	# CYAN + BOLD
ERROR = '\033[91m' + '\033[4m' 	# RED + UNDERLINE
GREEN = '\033[92m' + '\033[1m' 	# GREEN + BOLD
END = '\033[0m'					# STANDARD FONT

def check_date(num):
	if 0 <= num <= 9:
		return f'0{num}'
	else:
		return f'{num}'

def print_seccses(text):
	print(f'Ваш знак зодиака: {GREEN}{text}{END}' )

print('')

day = int(input('Введите день рождения: ' + USER))
mounth = int(input(END + 'Введите месяц рождения: ' + USER))
print(END + f'+{"-" * 30}+')

# day, mounth = map(int, input().split('.'))
print(f'{USER}[{check_date(day)}.{check_date(mounth)}]{END} - ', end='')

if (21 <= day <= 31 and mounth == 3) or (1 <= day <= 19 and mounth == 4):
	print_seccses('Овен')
elif (20 <= day <= 30 and mounth == 4) or (1 <= day <= 20 and mounth == 5):
	print_seccses('Телец')
elif (21 <= day <= 31 and mounth == 5) or (1 <= day <= 21 and mounth == 6):
	print_seccses('Близнецы')
elif (22 <= day <= 30 and mounth == 6) or (1 <= day <= 22 and mounth == 7):
	print_seccses('Рак')
elif (23 <= day <= 31 and mounth == 7) or (1 <= day <= 22 and mounth == 8):
	print_seccses('Лев')
elif (23 <= day <= 31 and mounth == 8) or (1 <= day <= 22 and mounth == 9):
	print_seccses('Дева')
elif (23 <= day <= 30 and mounth == 9) or (1 <= day <= 23 and mounth == 10):
	print_seccses('Весы')
elif (24 <= day <= 31 and mounth == 10) or (1 <= day <= 22 and mounth == 11):
	print_seccses('Скорпион')
elif (23 <= day <= 30 and mounth == 11) or (1 <= day <= 21 and mounth == 12):
	print_seccses('Стрелец')
elif (22 <= day <= 31 and mounth == 12) or (1 <= day <= 20 and mounth == 1):
	print_seccses('Козерог')
elif (21 <= day <= 31 and mounth == 1) or (1 <= day <= 18 and mounth == 2):
	print_seccses('Водолей')
elif (19 <= day <= 29 and mounth == 2) or (1 <= day <= 20 and mounth == 3):
	print_seccses('Рыбы')
else:
	print(f'{ERROR}Считается неверной датой!{END}')

	print('Причина:')
	if day <= 0 or 32 <= day:
		print('| День неверный!') 
	if mounth <= 0 or 13 <= mounth:
		print('| Месяц неверный!')
	if mounth == 2 and 30 <= day:
		print('| В феврале не может быть больше 29 дней!')

print('')