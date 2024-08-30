# Словари
# Множества
# Промежуточный тест  +  Самостоятельная работа.
"""
# +-----------------------------------------------+
# |					CLASS WORK					|
# +-----------------------------------------------+
# """

# # 		Словари: dict = {key_1: value_1, key_2: value_2}

# student = {
# 	'name': 'Akel',
# 	'age': 15,
# 	'weight': 45.2
# }

# # add
# student.update({
# 	'merried': False,
# 	'hobby': ['coding', 'chess', 'cards', 'learning']
# })
# student['surname'] = 'Nurlanov'

# # edit
# student['age'] = 16
# student['weight'] = student['weight'] + 0.7

# # delete
# student.pop('merried')
# del student['weight']


# print(student.keys())
# print(student.values())
# for key, value in student.items():
# 	print(f'{key}: {value}')

# # create
# print(dict(enumerate('LETTERS')))


# # 		МНОЖЕСТВА: set = {value_1, value_2, value_3}

# # set filter
# numbers_1 = [1, 5, 2, 3, 2, 1, 4, 3 ,1]
# numbers_2 = {1, 5, 2, 3, 2, 1, 4, 3 ,1}

# print(numbers_1)
# print(numbers_2)
# print(numbers_2)

# beshparmak = {'мясо', 'тесто', 'лук'}
# plov = {'рис' 'мясо', 'морковка'}

# print(beshparmak.union(plov))					# Соединение			{'тесто', 'мясо', 'рисмясо', 'морковка', 'лук'}
# print(beshparmak.difference(plov))			# Различия				{'мясо', 'лук', 'тесто'}
# print(beshparmak.intersection(plov))			# Схожести				{'мясо'}
# print(beshparmak.symmetric_difference(plov))	# Симетричное различие	{'мясо', 'тесто', 'морковка', 'лук', 'рисмясо'}


"""
+-----------------------------------------------+
|					HOME WORK					|
+-----------------------------------------------+
"""

country_flags = {
	'kg': {'red', 'yellow'},
	'us': {'red', 'white', 'blue'},
	'fr': {'blue', 'white', 'red'},
	'de': {'black', 'red', 'yellow'},
	'jp': {'white', 'red'},
	'it': {'green', 'white', 'red'},
	'br': {'green', 'yellow', 'blue', 'white'},
	'ru': {'white', 'blue', 'red'},
	'ca': {'red', 'white'},
	'au': {'red', 'white', 'blue'},
	'in': {'orange', 'white', 'green', 'blue'},
	'mx': {'green', 'white', 'red'},
	'es': {'red', 'yellow'},
	'za': {'green', 'yellow', 'black', 'white', 'blue', 'red'},
	'kr': {'white', 'red', 'blue', 'black'}
}

while True:
	user_color = input('Enter the color: ').lower()
	
	if user_color in ['q', 'quit', 'exit', 'ex']:
		print('Program stopped')
		break

	user_color = set(user_color.split())

	incorrect = True
	for country in country_flags:
		if user_color.issubset(country_flags[country]):
			print(country)
			incorrect = False
	if incorrect:
		print('Country was not found')