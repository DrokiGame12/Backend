
"""
+-----------------------------------------------+
|					HOME WORK					|
+-----------------------------------------------+
"""

vowels = 'aeiouyаеёиоуыэюя'
consonants = 'бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxz'

while True:
	print('-'*30)
	word = input('Слово: ').lower()

	if word == 'exit' or word == 'выход':
		break

	# count_letters = len(word)
	count_letters = 0 

	# Хотел сделать по коду ASCII
	count_vowels = 0
	count_consonants = 0

	for letter in word:
		if letter in vowels:
			count_vowels += 1
		elif letter in consonants:
			count_consonants += 1
		else:
			count_letters -= 1
		count_letters += 1

	percent_vowels = round(count_vowels/count_letters*100, 1)
	percent_consonants = round(count_consonants/count_letters*100, 1)

	print(f'Кол-во всех букв: {count_letters}')
	print(f'Согласные буквы: {count_consonants}')
	print(f'Гласные буквы: {count_vowels}')
	print(f'Гласные / Согласные: {percent_vowels}% / {percent_consonants}%')