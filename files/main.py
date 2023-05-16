import csv
import json

from files import CSV_F_PATH, JSON_F_PATH

users_list = []
# перезаписть файла с нужными полями
with open(JSON_F_PATH) as f:
    users = json.load(f)
# Обработка и запись в новый список пользователей с атрибутами
    for user in users:
        users_dict = {
        "name": user["Name"],
        "gender": user["Gender"],
        "address": user["Address"],
        "age": user["Age"],
        "books": []
        }
    users_list.append(users_dict)

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

total_users = len(users_list)
total_books = len(books_list)
print(total_users, 'кол-во пользователей')
print(total_books, 'кол-во книг')

max_books = total_books // total_users
remaining_books = total_books % total_users
print('по', max_books,'книг каждому')
print(remaining_books,'остаток книг')

book_index = 0
for user in users_list:
    for i in range(max_books):
        user['books'].append(books_list[book_index])
        book_index += 1
        if 0 < remaining_books:
            user['books'].append(books_list[book_index])
            remaining_books -= 1
            book_index += 1
            print(book_index, max_books)

with open("result.json","w") as f:
    result = json.dumps(users_list, indent=4)
    f.write(s)
