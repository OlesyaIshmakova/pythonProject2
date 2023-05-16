Цель:
Научиться работать с различными типами файлов.


Описание/Пошаговая инструкция выполнения домашнего задания:
Работа с тестовыми данными

Скачать файлы: https://github.com/agridyaev/otus-test-data/blob/master/hw/books.csv и https://github.com/agridyaev/otus-test-data/blob/master/hw/users.json.
Написать скрипт, который из двух данных файлов будет читать данные и на их основании создаст result.json файл со структурой: https://github.com/agridyaev/otus-test-data/blob/master/hw/reference.json.
Идея в том что нужно раздать все книги из csv файла пользователям из списка. Книги складываются в виде словарей в массив books у каждого пользователя.
Книг изначально больше чем пользователей, поэтому раздавать нужно по принципу "максимально поровну", т.е. если книг, например 10. а пользователей 3 то распределение будет таким - 4 3 3 (один получит оставшуюся книгу).
Итоговая структура должна соответствовать стандарту json и парситься соответствующей библиотекой.

Критерии оценки:
Задание оформить отдельным pull-request'ом (https://www.youtube.com/watch?v=swWqJBFpaNY)
В репозитории отсутствуют лишние файлы
Соблюдается минимальный кодстайл (встроенный в PyCharm)
В личном кабинете или репозитории приложен файл result.json с итоговым результатом.
Исходные файлы копировать не нужно.

Рекомендуем сдать до: 24.04.2023