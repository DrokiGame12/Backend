# Lambda функции. 
# Обработка исключений.

"""
+-----------------------------------------------+
|					CLASS WORK					|
+-----------------------------------------------+
"""


# def get_square(lenght:int, widht:int) -> int:
#     """
#     | Принимает длину и ширину комнаты
#     | Возвращает площадь комнаты
#     """
#     return lenght * widht

# print(help(get_square))


# word = 'Bishkek'
# cities = ['Tokmok', 'Karakol', 'Kant']

# def get_lenght(objects:any) -> int:
#     """
#     Принимает слово
#     Возвращает длину слова
#     """
#     count = 0
#     for i in objects:
#         count += 1
#     return count

# print(len(word))
# print(get_lenght(word))
# print(len(cities))
# print(get_lenght(cities))


# def up_first_letter(word:str) -> str:
#     return word.title()

# def show_words(func, objects) -> None:
#     for i in objects:
#         print(func(i))

# names = ('akel', 'dastan', 'emir')
# # print(map(len, names))
# show_words(up_first_letter, names)


#   LAMBDA ... lambda param: action ...
# summ = lambda num_1, num_2: num_1 + num_2

# map, filter, sorted

# filter(True/False, object)
# cities = ['Tokmok', 'Karakol', 'Kant']

# mapped_cities = list(map(lambda city: city.upper(), cities))
# print(mapped_cities)

# filtered_cities = list(filter(lambda city: 'a' in city.lower(), cities))
# print(filtered_cities)

# sorted_cities = sorted(cities, key=lambda city: city[-1])
# print(sorted_cities)

# try:
#     print(2 * 'HI')
# except:
#     print('Найдена ошибка')
# else:
#     print('OK')
# finally:
#     print('Проверка завершена')

# days = 1 
# data = {}
# while days <= 7:
#     print(data)
#     try:
#         data[days] = int(input(f'Enter expense for day #{days}: '))
#     except:
#         print('Enter just number!')
#     days += 1
# print(sum(data.values()))
# print(sum(data.values) / len(data))

"""
+-----------------------------------------------+
|					HOME WORK					|
+-----------------------------------------------+
"""

all_numbers_1, target_number_1 = [312, 996, 31, 1991], 1000
all_numbers_2, target_number_2 = [5, 20.18, 103, 4], 27


# Вариант в одну строку
nearest_number_1 = lambda all_num, target_num: (target_num, list(sorted(all_num, key=lambda num: abs(target_num - num))))
print(nearest_number_1(all_numbers_1, target_number_1))
print(nearest_number_1(all_numbers_2, target_number_2))



# Вариант с документацией и более понятный
def nearest_number_2(all_numbers:list|tuple, target_number:int):
	"""
	Принимает список или кортеж чисел и целевое число
	Возвращает кортеж с целевым числом и отсортированный список в порядке приближенности к целевому числу
	"""
	sorted_numbers = list(sorted(all_numbers, key= lambda number: abs(target_number - number)))
	return (target_number, sorted_numbers)
print(nearest_number_2(all_numbers_1, target_number_1))
print(nearest_number_2(all_numbers_2, target_number_2))


numbers = [i for i in range(-5, 6)]
print(f'\nПервоначальный список: {", ".join(map(str, numbers))}')

# Анонимная lambda в map и filter
print('Квадраты чисел: ', end='')
print(list(map(lambda num: num**2, numbers)))			# lambda возвращает измененное число

print('Четные числа: ', end='')
print(list(filter(lambda num: num%2==0, numbers)))	# lambda возвращает True или False
													# если True то оставляет число
													# елси False то ничего не возвращает



# Пример использования try except 
iterable = [i for i in range(11)]		# Список
iterable = ('Akel', 'Nurlanov', 14)		# Кортеж
iterable = 'Hello, World!'				# Строка

# Длина не будет изменятся от действий пользователя, поэтому его можно получить сразу
lenght = len(iterable) - 1 

def get_by_index(obj:list|tuple|str, index:str) -> any:
	"""
	Принимает объект (список, кортеж, строка) и действие как строку
	Возвращает результат как строку: 
	1) Всё проходит хорошо: возвращает элемент по индексу
	2) Есть ошибка в индексе: возвращает ошибку и инструкцию
	"""
	try:
		return f'{int(index)}) {obj[int(index)]}'
	except ValueError:
		return 'Нужно вводить только индекс как число!'
	except IndexError:
		return f'Нужно строго вводить от -{lenght+1} до {lenght}!'

print(f'\nLenght {lenght+1}:{iterable} ')
while True:
	action = input(f'Введите индекс ({lenght}): ')
	if action == 'q':
		print('Program stopped.')
		break
	print(get_by_index(iterable, action))