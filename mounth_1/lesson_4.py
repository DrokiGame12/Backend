# Списки []
# Индексы [0]
# Срезы [start:stop:step]
# Встроенные функции к наборам элементов
# List comprehention - Списковое включение [object cycle condition]
# Кортежи

"""
+-----------------------------------------------+
|					CLASS WORK					|
+-----------------------------------------------+
"""


# #		Списки
# list_test = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list_test)			# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# #		Индексы
# print(list_test[0])		# 0
# print(list_test[3])		# 3
# print(list_test[-2])		# 8


# #		Срезы: [start:stop:step] 
# #		ненужные значения можно ИГНОРИРОВАТЬ
# print(list_test[1:4])		# [1, 2, 3]
# print(list_test[-2:])		# [8, 9]
# print(list_test[:2])		# [0, 1]

# print(list_test[::-1])	# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# print(list_test[::3])		# [0, 3, 6, 9]
# print(list_test[:5:2])	# [0, 2, 4]


# # 		ДОБАВЛЕНИЕ
# list_test.append('1')		# Добавление в конец
# list_test.insert(1, '2')	# Добавление по координатам
# list_test.extend(['3'])	# Соединение в конец
# print(list_test)


# # 		ИЗМЕНЕНИЕ
# list_test[0] = '4'		# Изменение значения по индексу
# list_test.sort()			# Сортировка по возрастанию (используется знак <)
# list_test.reverse()		# Разворот полностью
# 							# равносильно list_test = list_test[::-1]
# print(list_test)


# # 		УДАЛЕНИЕ
# list_test.remove(3)			# Удаление по значению
# first = list_test.pop(0)		# Удаление или вырезание по индексу
# del list_test[2::3]			# Удаление по срезу
# print(list_test, '---', first)


# 			Свойства массива
# list_test_link = list_test			# Сохдает ссылку
# list_test_copy = list_test.copy()		# Создает копию

# print(id(list_test))
# print(id(list_test_link))
# print(id(list_test_copy))

# print(list_test == list_test_link)	# True
# print(list_test == list_test_copy)	# True

# print(list_test is list_test_link)	# True
# print(list_test is list_test_copy)	# False


# 		Списковое включение | List comprehention
# 				[переменная цикл условие]

# list_test_edit = [num * 10 for num in list_test if num != 3]
# print(list_test_edit)	# [0, 10, 20, 40, 50, 60, 70, 80, 90]


# # 		Некоторые функции...
# print(len(list_test))	# Кол-во значений
# print(sum(list_test))	# Сумма значений
# print(min(list_test))	# Минимальное значение
# print(max(list_test))	# Максимальное значение


# # 		Кортежи - type(tuple)
# # 		| Является НЕизменяемым

# tuple_test = ('word', True, 34, 56.1)
# print(tuple_test)	# ('word', True, 34, 56.1)


"""
+-----------------------------------------------+
|					HOME WORK					|
+-----------------------------------------------+
"""

mentors = ["Тимур", "Арсен", "Гулина", "Даниель"]

def name_check(name):
	if len(name) <= 15:
		if not name in mentors:
			return True
		else:
			print('Такой ментор уже существует!')
			return False
	else:
		print('Имя должно быть меньше 15!')
		return False

while True:
	print(' ')
	# print(f'Менторы: {mentors}')
	print('1. Добавление')
	print('2. Изменение')
	print('3. Удаление')
	print('4. Выход')

	action = input('Номер действия: ').lower()

	if action == '1' or action == 'добавление':
		new_mentor_name = input('Введите имя нового ментора: ').title()

		if len(mentors) < 10:
			if name_check(new_mentor_name):
				mentors.append(new_mentor_name)
				print('Ментор успешно добавлен!')
		else:
			print('Минимальное кол-во менторов 10!')

	elif action == '2' or action == 'изменение':
		edit_mentor = input('Выберите изменяемого ментора: ').title()

		for i in range(len(mentors)):
			if edit_mentor == mentors[i]:
				new_mentor_name = input('Введите новое имя: ').title()
				if name_check(new_mentor_name):
					mentors[i] = new_mentor_name
				break
		else:
			print('Такого ментора нет!')

	elif action == '3' or action == 'удаление':
		delete_mentor = input('Выберите удаляемого ментора: ').title()
		print(delete_mentor.isalpha())
		if delete_mentor.isalpha():
			for i in range(len(mentors)-1):
				if delete_mentor == mentors[i]:
					mentors.remove(delete_mentor)
			else:
				print('Такого ментора нет!')

		else:
			delete_mentor = int(delete_mentor)
			if delete_mentor < len(mentors):
				mentors.pop(delete_mentor)
			else:
				print('Неверный индекс!')

	elif action == '4' or action == 'выход':
		final_mentors = tuple(mentors)
		print('\nМенторы:\n', final_mentors, end='\n') 
		break

	else:
		print('Неизвестное действие!')