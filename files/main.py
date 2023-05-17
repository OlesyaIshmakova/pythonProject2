import csv
import json
from files import CSV_F_PATH, JSON_F_PATH

users_list = []
with open(JSON_F_PATH) as f:
    users = json.load(f)
    for user in users["users"]:
        users_dict = {
            "name": user["name"],
            "gender": user["gender"],
            "address": user["address"],
            "age": user["age"],
            "books": []
        }
        users_list.append(users_dict) #добавляет элемент x в конец списка.

books_list = []
with open(CSV_F_PATH) as f:
    books = csv.DictReader(f)
    for book in books:
        books_dict = dict(title = book["Title"], author = book["Author"], pages = int(book["Pages"]), genre = book["Genre"])
        books_list.append(books_dict)#добавляет элемент x в конец списка.

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
    if remaining_books > 0:
        user['books'].append(books_list[book_index])
        remaining_books -= 1
        book_index += 1
    # print(book_index, max_books)

with open("result.json", "w") as s:
    result = json.dumps(users_list, indent=4)
    s.write(result)
