# Принципы ООП
# 1. Наследование - на основе одного класса можно создать другие классы
# 2. Полиморфизм
# 3. Инкапсуляция
# 4. Абстракция

# gitignore

# принципы ооп
# 4 Наследование,Полиморфизм,Инкапсуляция,Абстракция
# gitignore
# на основе одного класса можно создать другие классы
import random
# from lesson1 import Manga
# naruto=Manga('Naruto','Kishimoto')

# print(naruto)

# cупер класс\родительский класс
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def reads(self):
        print('я читаю книгу:',self.title)

    def words_author(self):
        print('привет меня зовут:',self.author,' читай с лева на право')

# DRY - Don't Repeat Yourself
# book1 = Book('властелин колец','Толкин')
# book1.reads()
# book1.words_author()

# дочерний класс
class Manga(Book):
    def __init__(self, title, author,png='png'):
        super().__init__(title, author)
        Book.__init__(self, title, author)
        self.png = png

    #     обращается к внутренностям родительского класса
    def words_author(self):
        print('привет меня зовут:',self.author, 'читай с права на лево')

    def reads(self):
        print('я читаю мангу:',self.title)
        self.words_author()

manga=Manga('naruto','Kishimoto')
manga.reads()