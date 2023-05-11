import csv
import json
from files import CSV_F_PATH, JSON_F_PATH
# печатает все строки из файла работало
books_list = []
with open(CSV_F_PATH) as csv_file:
    books = csv.DictReader(csv_file)
    for book in books:
        books_dict = dict(title=book["Title"],
                          author=book["Author"],
                          pages=int(book["Pages"]),
                          genre=book["Genre"])
    books_list.append(books_dict)
# list.append(item)     append()      принимает      один      аргумент      item      и      добавляет     его      в      конец      list.# открыть json пользователи
users_list = []
with open(JSON_F_PATH) as json_file:
    users = json.load(json_file)
    users_list = users['users']        # print(users_list)
    for user in users:
        user_dict = dict(name=user["name"],
                         gender=user["gender"],
                         address=user["address"],
                         age=user["age"],
                         books=[])
    users_list.append(user_dict)

count_users = len(users_list)
num_books = len(books)
print(count_users, 'кол-во пользователей')
print(num_books, 'кол-во книг')
max_books = num_books // count_users
remaining_books = num_books % count_users
print('по', max_books,'книг каждому')
print(remaining_books,'остаток книг')
book_index = 0
for i, user in enumerate(users_list):
    for j in range(max_books):
        user['books'].append(books[book_index])
        book_index += 1
if i < remaining_books:
    user['books'].append(books[book_index])
    book_index += 1
with open('result.json', 'w') as f:
    json.dump(users_list, f, indent=4)
    # s = json.dumps(data, f)
    # f.write(s)
