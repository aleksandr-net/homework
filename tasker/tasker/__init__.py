#!/usr/bin/python3.5

import os.path as Path
import sys
from tasker import storage


get_connection = lambda : storage.connect("tasker.sqlite")


def action_show_tasks():

    with get_connection() as conn:
        storage.show_tasks(conn)


def action_add(): # Добавить задачу
    header = input("\nВведите название задачи: ")
    description = input("\nВведите описание задачи: ")
    start_date = input("\nВведите время начала задачи в формате 'ГГГГ-ММ-ДД ЧЧ:ММ:СС' (по умолчанию - текущее время): ")
    

    with get_connection() as conn:
        header = storage.add_task(conn, header, description, start_date)

    print("Задача добавлена:\nЗаголовок: {}\nОписание: {}\n".format(header, description))


def action_edit():

    with get_connection() as conn:
        storage.edit_task(conn)


def action_close():

    with get_connection() as conn:
        storage.close_task(conn)


def action_reopen():

    with get_connection() as conn:
        storage.reopen_task(conn)


def action_show_menu():
    print("""Ежедневник. Выберите действие:

1. Вывести список задач
2. Добавить задачу
3. Отредактировать задачу
4. Завершить задачу
5. Начать задачу сначала
m. Показать меню
q. Выход""")


def action_exit():
    sys.exit(0)


def main():
    creation_schema = Path.join(
        Path.dirname(__file__), 'schema.sql'
    )

    with get_connection() as conn:
        storage.initialize(conn, creation_schema)

    actions = {
        '1': action_show_tasks,
        '2': action_add,
        '3': action_edit,
        '4': action_close,
        '5': action_reopen,
        'm': action_show_menu,
        'q': action_exit
    }

    action_show_menu()

    while True:
        cmd = input('\nВведите команду: ')
        action = actions.get(cmd)

        if action:
            action()
        else:
            print('Неизвестная команда')
