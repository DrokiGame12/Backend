# Функции: виды параметров, возвращение данных, виды аргументов.
# DRY - don't repeat yourself (не повторяй себя)

"""
+-----------------------------------------------+
|					CLASS WORK					|
+-----------------------------------------------+
"""

# 	DEF 	define (определять)
"""Схема функции"""
# определение наименование(параметры):
# 	тело функции (задачи)
# 	возвращение результата
#
"""вызов функции"""
# наименование(аргументы)

# def get_data(name, surname = None):	# required positional parameter
#     print(f'Hello {name}!')

# get_data('Akel', 'Nurlanov')	# required positional argument
# get_data('Akel')				# non-required positional argument
# get_data(surname='Nurlanov', 
#          name='Akel')			# kyeword arguments


# #		3 ВИД	Кортеж - получечние остальных значений
# def plus(mult, *args):	# (1, 2, 3, 4, 5, 6, 7)
#     return args
# print(plus(2, 1, 2, 3, 4, 5, 6, 7))


# #		4 ВИД	Словарь - задается по ключам
# def menu(**kwargs):	# {'name': 'Akel', 'surname': 'Nurlanov', 'age': '15'}
#     return kwargs
# person = menu(name='Akel', surname='Nurlanov', age='15')
# print(person)


"""
+-----------------------------------------------+
|					HOME WORK					|
+-----------------------------------------------+
"""

# [x] = ERROR
# (+) = SUCCESS

movies = {
    "Django Unchained": {
        "John": 10,
        "Jack": 9
    },
    "Troy": {}
}

# def filter_input(message):
#     return input(message).title().strip()

# def get_mean(length, rates):
#     return round(sum(rates)/length, 1)

# def check_key(key, keys_dict):
#     if key in keys_dict.keys():
#         return True
#     else:
#         return False

""" Сделал через lambda """
filter_input = lambda message: input(message).title().strip()
get_mean = lambda length, rates: round(sum(rates)/length, 1)
check_key = lambda key, keys_dict: True if key in keys_dict.keys() else False

def add_movie():
    movie_name = filter_input('Enter adding movie name: ')

    if movie_name != '' and not check_key(movie_name, movies):
        movies.update({movie_name: {}})
        print(f'(+) Movie "{movie_name}" added successfully')
    else:
        print('[x] Such a movie already exists!')

def rate_movie():
    movie_name = filter_input('Enter rateing movie name: ')
    
    if check_key(movie_name, movies):
        user_name = filter_input('Enter your name: ')
        movie_raters = movies[movie_name]

        if user_name != '' and not check_key(user_name, movie_raters):
            rate = int(input('Enter your rating (0/10): '))

            if 0 <= rate <= 10:
                movie_raters.update({user_name: rate})
                print(f'(+) A rating has been added for "{movie_name}": {user_name} rated it {rate}/10')
            else:
                print('[x] The rating must be from 1 to 10!')
        else:
            print('[x] This user already exists!')
    else:
        print('[x] This movie doesn\'t exist')

def show_movies():
    for movie_name, raters in movies.items():
        count_raters = len(raters)

        if count_raters:
            mean_rating = get_mean(count_raters, raters.values())
            print(f'| "{movie_name}" is rated {mean_rating}/10')
        else:
            print(f'| Rating is not yet available for "{movie_name}"')


while True:

    print('',
          '1. Add new movie', 
          '2. Rate chosen movie', 
          '3. All movies and rating', 
          '4. Stop program',
          sep='\n')

    action = input('Enter your chosen action: ').lower()
    
    if action == '1' or action == 'add':
        add_movie()

    elif action == '2' or action == 'rate':
        rate_movie()

    elif action == '3' or action == 'all':
        show_movies()

    elif action == '4' or action == 'stop':
        print('The program has stopped.')
        break

    else:
        print('[x] There is no such action!')