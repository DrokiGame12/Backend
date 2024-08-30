# Контекстный менеджер “with”
# Работа с файлами

"""
+-----------------------------------------------+
|					CLASS WORK					|
+-----------------------------------------------+
"""

# W - write
# A - add
# R - read
# X - exist

# # Старая версия
# file = open('new_file.txt', 'w', encoding='UTF-8')            # WRITE
# file.write('Привет, мир!')
# file.close()

# # Новая версия
# with open('new_file.txt', 'a', encoding='UTF-8') as file:     # ADD
#     file.write('\nПривет, мир!')

# with open('new_file.txt', 'x', encoding='UTF-8') as file:     # EXIST
#     file.write('\nПривет, мир!')

# with open('new_file.txt', 'r', encoding='utf-8') as file:     # READ
#     print(file.read())
#     print(file.readline())
#     print(file.readlines())

"""
+-----------------------------------------------+
|					HOME WORK					|
+-----------------------------------------------+
"""

MAX_NUM = 100	# Сan customize as you wish. (If enter odd number, the max number is not found!)

class Hidden_Number:
	"""
	Can find your hidden number
	"""
	max_number = MAX_NUM
	possible_number = MAX_NUM // 2
	last_possible_number = -1
	attempts = []
	min_number = 0
	attempts_count = 1

	def find_possible_number(self):
		"""
		Find possible number
		"""
		self.attempts_count += 1
		self.last_possible_number = self.possible_number
		self.attempts.append(self.possible_number)
		self.possible_number = round((self.max_number + self.min_number)/2)
		
	
	def reset(self):
		"""
		Reset all data
		"""
		self.max_number = MAX_NUM
		self.possible_number = MAX_NUM // 2
		self.last_possible_number = -1
		self.attempts = []
		self.min_number = 0
		self.attempts_count = 1

	def smaller(self):
		self.max_number = self.possible_number
		hn.find_possible_number()

	def bigger(self):
		self.min_number = self.possible_number
		hn.find_possible_number()

	def check_user_answers(self) -> bool:
		"""
		True - correct answers (success)
		False - incorrect answers (error)
		"""
		return self.max_number - self.min_number != 0 and self.last_possible_number != self.possible_number

def test_game():
	"""
	Testing my code: checking all numbers and print error's index
	"""
	error_count = 0
	for i in range(MAX_NUM+1):
		try:
			attempts_count = 0
			while True:
				if attempts_count >= MAX_NUM:
					print(f'{i} - ERROR (attempts_count)')
					error_count += 1
					break
				elif hn.check_user_answers():
					if i == hn.possible_number:
						break
					elif i > hn.possible_number:
						hn.bigger()
					elif i < hn.possible_number:
						hn.smaller()
					attempts_count += 1
				else:
					print(f'{i} - ERROR (check_user_answer)')
					error_count += 1
					break
		except:
			print(f'{i} - ERROR (except)')
			error_count += 1
		hn.reset()
	
	print(f'[{"x" if error_count else "+"}] In program {error_count if error_count else "no"} errors.')


def file_write(text:str, file:str='result.txt', mode:str='a') -> None:
	"""
	function: Write any text in file
	Takes: text(str), file(str), mode(str)
	Returns: nothing(None)
	"""
	with open(file, mode, encoding='utf-8') as file:
		file.write(text)

def game():
	print(f'Загадайте число от 0 до {MAX_NUM}...')
	file_write(f'\n[+] Guessing a number between 0 and {MAX_NUM}:\n')
	while True:
		if hn.check_user_answers():
			user_answer = input(f'Ваше число больше или меньше чем {hn.possible_number}? (меньше/равно/больше)(</=/>)\nОтвет: ').lower().strip()
			
			if user_answer == 'q':
				print('Конец программы...')
				break

			if user_answer == 'равно' or user_answer == '=':
				hn.attempts.append(hn.possible_number)
				attempts = " -> ".join(map(str, hn.attempts))
				print(f'[+] Загаданное число: {hn.possible_number}\n[+] Нужно попыток: {hn.attempts_count}\n[+] Попытки: {attempts}\n[+] Информация сохранена. (для выхода введте "q")\n')
				file_write(f'Hidden number: {hn.possible_number} ({hn.attempts_count} attempts) | {attempts}\n')
				hn.reset()

			elif user_answer == 'больше' or user_answer == '>':
				hn.bigger()
				print()

			elif user_answer == 'меньше' or user_answer == '<':
				hn.smaller()
				print()
			else:
				print('[x] Пишите только меньше, равно, больше или <, =, >\n')
		else:
			print('[x] Вы где-то ошиблись, невозможное число...\n')
			hn.reset()

hn = Hidden_Number()
game()
# test_game()