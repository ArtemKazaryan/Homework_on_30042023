
# !!!!!!  ДЛЯ ЗАПУСКА ОТДЕЛЬНЫХ ЗАДАНИЙ РАСКОММЕНТИРУЙТЕ ИХ РЕШЕНИЕ, ЕСЛИ ПОТРЕБУЕТСЯ  !!!!!!

# Домашняя работа на 30.04.2023.

# Модуль 8. Упаковка данных
#
# Тема: Упаковка данных. Часть 2


# Задание 1
# К уже реализованному классу «Автомобиль» добавьте
# возможность упаковки и распаковки данных с использованием json и pickle.

# Решение:
print()
print('-'*49)
print('*'*11, 'РЕЗУЛЬТАТЫ ПО ЗАДАНИЮ №1:', '*'*11)

import pickle
import json

class Car:
    def __init__(self, car_model, year_of_manufacture, manufacturer,
                 engine_capacity, car_color, price):
        self.car_model = car_model
        self.year_of_manufacture = year_of_manufacture
        self.manufacturer = manufacturer
        self.engine_capacity = engine_capacity
        self.car_color = car_color
        self.price = price

    def set_car_info(self):
        self.car_model = input('Введите название модели автомобиля: ')
        self.year_of_manufacture = input('Введите год выпуска: ')
        self.manufacturer = input('Введите производителя: ')
        self.engine_capacity = input('Введите объем двигателя, л: ')
        self.car_color = input('Введите цвет автомобиля: ')
        self.price = input('Введите цену, $: ')
        car_list = [self.car_model, self.year_of_manufacture, self.manufacturer, self.engine_capacity, self.car_color, self.price]
        with open('car_pickle.pkl', 'wb') as pickle_out:
            pickle.dump(car_list, pickle_out)
            print('Информация об автомобиле сериализована в формат pickle (сохранена в файл car_pickle.pkl)')
        with open('car_json.json', 'w') as write_file:
            json.dump(car_list, write_file)
            print('Информация об автомобиле сериализована в формат json (сохранена в файл car_json.json)')
        print()

    def print_car_info(self):
        with open('car_pickle.pkl', 'rb') as pickle_in:
            car_list_from_pickle = pickle.load(pickle_in)
            print(f'ИНФОРМАЦИЯ ОБ АВТОМОБИЛЕ ПОСЛЕ ДЕСЕРИАЛИЗАЦИИ ИЗ ФОРМАТА pickle:')
            print(f'Название модели автомобиля: {car_list_from_pickle[0]}')
            print(f'Год выпуска: {car_list_from_pickle[1]}')
            print(f'Производитель: {car_list_from_pickle[2]}')
            print(f'Объем двигателя, л: {car_list_from_pickle[3]}')
            print(f'Цвет автомобиля: {car_list_from_pickle[4]}')
            print(f'Цена, $: {car_list_from_pickle[5]}')
            print()
        with open('car_json.json', 'r') as read_file1:
            car_list_from_json = json.load(read_file1)
            print(f'ИНФОРМАЦИЯ ОБ АВТОМОБИЛЕ ПОСЛЕ ДЕСЕРИАЛИЗАЦИИ ИЗ ФОРМАТА json:')
            print(f'Название модели автомобиля: {car_list_from_json[0]}')
            print(f'Год выпуска: {car_list_from_json[1]}')
            print(f'Производитель: {car_list_from_json[2]}')
            print(f'Объем двигателя, л: {car_list_from_json[3]}')
            print(f'Цвет автомобиля: {car_list_from_json[4]}')
            print(f'Цена, $: {car_list_from_json[5]}')
            print()

car = Car(car_model='Не определена', year_of_manufacture='Не определён',
          manufacturer='Не определён', engine_capacity='Не определён',
          car_color='Не определён', price='Не определена')

print()
car.set_car_info()
car.print_car_info()



# Задание 2
# К уже реализованному классу «Книга» добавьте возможность
# упаковки и распаковки данных с использованием json и pickle.
#
# Решение:
print()
print('-'*49)
print('*'*11, 'РЕЗУЛЬТАТЫ ПО ЗАДАНИЮ №2:', '*'*11)

import pickle
import json

class Book:
    def __init__(self, book_title, year_of_release, publisher,
                 genre, author, price):
        self.book_title = book_title
        self.year_of_release = year_of_release
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def set_book_info(self):
        self.book_title = input('Введите название книги: ')
        self.year_of_release = input('Введите год выпуска: ')
        self.publisher = input('Введите издателя: ')
        self.genre = input('Введите жанр: ')
        self.author = input('Введите автора: ')
        self.price = input('Введите цену, руб.: ')
        book_list = [self.book_title, self.year_of_release, self.publisher, self.genre, self.author, self.price]
        with open('book_pickle.pkl', 'wb') as pickle_out:
            pickle.dump(book_list, pickle_out)
            print('Информация о книге сериализована в формат pickle (сохранена в файл book_pickle.pkl)')
        with open('book_json.json', 'w') as write_file:
            json.dump(book_list, write_file)
            print('Информация о книге сериализована в формат json (сохранена в файл book_json.json)')
        print()

    def print_book_info(self):
        with open('book_pickle.pkl', 'rb') as pickle_in:
            book_list_from_pickle = pickle.load(pickle_in)
            print(f'ИНФОРМАЦИЯ О КНИГЕ ПОСЛЕ ДЕСЕРИАЛИЗАЦИИ ИЗ ФОРМАТА pickle:')
            print(f'Название книги: {book_list_from_pickle[0]}')
            print(f'Год выпуска: {book_list_from_pickle[1]}')
            print(f'Издатель: {book_list_from_pickle[2]}')
            print(f'Жанр: {book_list_from_pickle[3]}')
            print(f'Автор: {book_list_from_pickle[4]}')
            print(f'Цена, руб.: {book_list_from_pickle[5]}')
            print()
        with open('book_json.json', 'r') as read_file2:
            book_list_from_json = json.load(read_file2)
            print(f'ИНФОРМАЦИЯ О КНИГЕ ПОСЛЕ ДЕСЕРИАЛИЗАЦИИ ИЗ ФОРМАТА json:')
            print(f'Название книги: {book_list_from_json[0]}')
            print(f'Год выпуска: {book_list_from_json[1]}')
            print(f'Издатель: {book_list_from_json[2]}')
            print(f'Жанр: {book_list_from_json[3]}')
            print(f'Автор: {book_list_from_json[4]}')
            print(f'Цена, руб.: {book_list_from_json[5]}')
            print()

book = Book(book_title='Не определено', year_of_release='Не определён',
          publisher='Не определён', genre='Не определён',
          author='Не определён', price='Не определена')

print()
book.set_book_info()
book.print_book_info()



# Задание 3
# К уже реализованному классу «Стадион» добавьте
# возможность упаковки и распаковки данных с использованием json и pickle.
#
# Решение:
print()
print('-'*49)
print('*'*11, 'РЕЗУЛЬТАТЫ ПО ЗАДАНИЮ №3:', '*'*11)

import pickle
import json

class Stadium:
    def __init__(self, stadium_name, opening_date, country, city, capacity):
        self.stadium_name = stadium_name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def set_stadium_info(self):
        self.stadium_name = input('Введите название стадиона: ')
        self.opening_date = input('Введите дату открытия: ')
        self.country = input('Введите страну расположения: ')
        self.city = input('Введите город расположения: ')
        self.capacity = input('Введите вместимость стадиона, чел.: ')
        print()
        stadium_list = [self.stadium_name, self.opening_date, self.country, self.city, self.capacity]
        with open('stadium_pickle.pkl', 'wb') as pickle_out:
            pickle.dump(stadium_list, pickle_out)
            print('Информация о стадионе сериализована в формат pickle (сохранена в файл stadium_pickle.pkl)')
        with open('stadium_json.json', 'w') as write_file:
            json.dump(stadium_list, write_file)
            print('Инфорация о стадионе сериализована в формат json (сохранена в файл stadium_json.json)')
        print()

    def print_stadium_info(self):
        with open('stadium_pickle.pkl', 'rb') as pickle_in:
            stadium_list_from_pickle = pickle.load(pickle_in)
            print(f'ИНФОРМАЦИЯ О СТАДИОНЕ ПОСЛЕ ДЕСЕРИАЛИЗАЦИИ ИЗ ФОРМАТА pickle:')
            print(f'Название стадиона: {stadium_list_from_pickle[0]}')
            print(f'Дата открытия: {stadium_list_from_pickle[1]}')
            print(f'Страна расположения: {stadium_list_from_pickle[2]}')
            print(f'Город расположения: {stadium_list_from_pickle[3]}')
            print(f'Вместимость, чел.: {stadium_list_from_pickle[4]}')
            print()
        with open('stadium_json.json', 'r') as read_file3:
            stadium_list_from_json = json.load(read_file3)
            print(f'ИНФОРМАЦИЯ О СТАДИОНЕ ПОСЛЕ ДЕСЕРИАЛИЗАЦИИ ИЗ ФОРМАТА json:')
            print(f'Название стадиона: {stadium_list_from_json[0]}')
            print(f'Дата открытия: {stadium_list_from_json[1]}')
            print(f'Страна расположения: {stadium_list_from_json[2]}')
            print(f'Город расположения: {stadium_list_from_json[3]}')
            print(f'Вместимость, чел.: {stadium_list_from_json[4]}')
            print()

stadium = Stadium(stadium_name='Не определено', opening_date='Не определена',
          country='Не определена', city='Не определён',
          capacity='Не определена')

print()
stadium.set_stadium_info()
stadium.print_stadium_info()