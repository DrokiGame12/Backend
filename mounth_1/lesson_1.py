# print('Пишите каждый день через пробел')
# weekly_expenses = list(map(int, input('Расходы дней: ').split()))

# amount_of_expenses = sum(weekly_expenses)
# print(f'Общая сумма расходов: {amount_of_expenses}')

# average_consumption = round(amount_of_expenses / len(weekly_expenses), 1)
# print(f'Средний расход в день: {average_consumption}')



monday = int(input('Понедельник: '))
tuesday = int(input('Вторник: '))
wednesday = int(input('Среда: '))
thursday = int(input('Четверг: '))
friday = int(input('Пятница: '))
saturday = int(input('Суббота: '))
sunday = int(input('Вокресенье: '))

amount_of_expenses = monday + tuesday + wednesday + thursday + friday + saturday + sunday
print(f'Общая сумма расходов: {amount_of_expenses}')

average_consumption = round((amount_of_expenses / 7), 1)
print(f'Средний расход в день: {average_consumption}')
