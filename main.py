import csv
import json
from files import CSV_F_PATH, JSON_F_PATH
books = []# обнулитьсписок
# печатает все строки из файла работало
with open(CSV_F_PATH) as csv_file:
    rd = csv.DictReader(csv_file)
    for row in rd:
        books.append(row)        # print(book)
# открыть json пользователи
with open(JSON_F_PATH) as json_file:
    users = json.load(json_file)
    users_list = users['users']        # print(users_list)
count_users = len(users_list)
num_books = len(books)
print(count_users, 'кол-во пользователей')
print(num_books, 'кол-во книг')
max_books = num_books // count_users
remaining_books = num_books % count_users
print('по', max_books,'книг каждому')
print(remaining_books,'остаток книг')
# перезаписть файла с нужными полями
with open(JSON_F_PATH) as f:
    users = json.load(f)
# Обработка и запись в новый список пользователей с атрибутами
for user in users:
    user_dict = {
        "name": user["name"],
        "gender": user["gender"],
        "address": user["address"],
        "age": user["age"],
        "books": []
    }
    users_list.append(user_dict)
# Открытие файла с книгами books.json запись с атрибутами reference.json
books_list = []
with open(CSV_F_PATH) as f:
    books = csv.DictReader(f)
    for book in books:
        books_dict = {
            "title": book["Title"],
            "author": book["Author"],
            "pages": int(book["Pages"]),
            "genre": book["Genre"]
        }
        books_list.append(books_dict)

book_index = 0
for i, user in enumerate(users_list):
    for j in range(max_books):
        user['books'].append(books[book_index])
        book_index += 1
        if i < remaining_books:
            user['books'].append(books[book_index])
        book_index += 1

with open('result.json','w') as f:
    json.dump(users_list, f, indent=4)

