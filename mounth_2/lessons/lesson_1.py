# OOП 1: 
## Основы ООП
## Создание первых классов
## Атрибуты и Методы классов
## Принцип ООП - Наследовани

"""
+-----------------------------------------------+
|					CLASS WORK					|
+-----------------------------------------------+
"""

# CLASS:
# 	CONSTRUCTOR(self):
#		function __init__
# 	METHOD(self):
# 		dunction method
# 	METHOD(self):
# 		dunction method
# 	...

class Transport:
	def __init__(self, the_year, the_model, the_color, penalties=0):
		# fields / attributs
		self.year = the_year
		self.model = the_model
		self.color = the_color
		self.penalties = penalties

	def change_color(self, new_color):
		self.color = new_color

class Plane(Transport):
	counter = 0
	def __init__(self, the_year, the_model, the_color):
		super.__init__(the_year, the_model, the_color)
		Plane.counter += 1


class Car(Transport):
	counter = 0
	# __init__ - constructor
	def __init__(self, the_year, the_model, the_color, penalties=0):
		# super class
		super().__init__(the_year, the_model, the_color)	# constructor matching
		self.penalties = penalties
		Car.counter += 1
	# method
	def drive(self):
		print(f'Car {self.model} is driving...')

	def signal(self, nunmber_of_times, sound):
		while nunmber_of_times > 0:
			print(f'Car {self.model} signaling {sound}')
			nunmber_of_times -= 1

class Truck(Car):
	def __init__(self, the_year, the_model, the_color, penalties=0):
		super().__init__(the_year, the_model, the_color, penalties)

bmw_car = Car(2020, "BMW X6", 'red')
print(bmw_car.penalties)

honda_car = Car(2021, "Honda Fit", 'blue', 500)
print(honda_car.penalties)

bmw_car.drive()
bmw_car.signal(3, 'beep')
honda_car.signal(2, 'Krya')

print('STOP')
print('END')

