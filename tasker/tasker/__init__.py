#!/usr/bin/python3.5

import os.path as Path
import sys
import datetime
from tasker import storage


get_connection = lambda : storage.connect("tasker.sqlite")


def action_show_tasks():
    """Вывести весь список задач"""
    with get_connection() as conn:
        rows = storage.show_tasks(conn)

    print('\nID - Заголовок - Описание - Время начала - Время окончания - Статус\n')
    template = '{row[id]} - {row[header]} - {row[description]} - {row[start_date]} - {row[end_date]} - {row[status]}'

    for row in rows:
        print(template.format(row=row))


def action_add(): # Добавить задачу
    header = input("\nВведите название задачи: ")
    description = input("\nВведите описание задачи: ")
    start_date = input("\nВведите время начала задачи в формате 'ГГГГ-ММ-ДД ЧЧ:ММ:СС' (по умолчанию - текущее время): ")
    end_date = input("\nВведите время окончания задачи в формате 'ГГГГ-ММ-ДД ЧЧ:ММ:СС': ")

    if start_date == '':
        start_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with get_connection() as conn:
        cursor = storage.add_task(conn, header, description, start_date, end_date)

    print("Задача добавлена:\nЗаголовок: {}\nОписание: {}\nВремя начала: {}\nВремя окончания: {}".format(header, description, start_date, end_date))


def action_edit():
    action_show_tasks()
    task_id = input("\nВыберите задачу по ID: ")
    header = input("\nВведите название задачи: ")
    description = input("\nВведите описание задачи: ")
    start_date = input("\nВведите время начала задачи в формате 'ГГГГ-ММ-ДД ЧЧ:ММ:СС' (по умолчанию - текущее время): ")
    end_date = input("\nВведите время окончания задачи в формате 'ГГГГ-ММ-ДД ЧЧ:ММ:СС': ")

    if start_date == '':
        start_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with get_connection() as conn:
        cursor = storage.edit_task(conn, task_id, header, description, start_date, end_date)

    print("Задача обновлена:\nЗаголовок: {}\nОписание: {}\nВремя начала: {}\nВремя окончания: {}".format(header, description, start_date, end_date))


def action_close():
    action_show_tasks()
    task_id = input("\nВыберите задачу по ID: ")
    end_date = input("\nВведите фактическое время окончания задачи в формате 'ГГГГ-ММ-ДД ЧЧ:ММ:СС' (по умолчанию - текущее время): ")

    if end_date == '':
        end_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with get_connection() as conn:
        cursor = storage.close_task(conn, task_id, end_date)


def action_reopen():
    action_show_tasks()
    task_id = input("\nВыберите задачу по ID: ")
    start_date = input("\nВведите время начала задачи в формате 'ГГГГ-ММ-ДД ЧЧ:ММ:СС' (по умолчанию - текущее время): ")
    end_date = input("\nВведите время окончания задачи в формате 'ГГГГ-ММ-ДД ЧЧ:ММ:СС': ")

    if start_date == '':
        start_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with get_connection() as conn:
        cursor = storage.reopen_task(conn, task_id, start_date, end_date)



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
