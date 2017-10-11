#!/usr/bin/python3.5

import sqlite3

SQL_SELECT_ALL = "SELECT id, original_url, short_url, created FROM calendar"

SQL_SELECT_TASK_BY_ID = SQL_SELECT_ALL + " WHERE id=?"

SQL_SELECT_TASKS_BY_DATE = SQL_SELECT_ALL + " WHERE date=?"

SQL_SELECT_TASKS_BY_DATETIME = SQL_SELECT_ALL + " WHERE date=? AND time=?"

SQL_SELECT_TASKS_BY_STATUS = SQL_SELECT_ALL + " WHERE task_status=?"

#SQL_INSERT_TASK = "INSERT INTO calendar"

SQL_UPDATE_TASK_STATUS =  "UPDATE calendar SET task_status=? WHERE id=?"


def connect(db_name=None):
    if db_name is None:
        db_name = ':memory:'

    conn = sqlite3.connect(db_name)

    # превращение кортежа в словарь (сделаем позже)

    return conn


def initialize(conn, creation_schema):
    with conn, open(creation_schema) as f:
        conn.executescript(f.read())


def show_tasks():
    """Выводит список всех задач"""

def add_task():
    """Добавляет новую задачу"""

def edit_task():
    """Редактирует задачу"""

def close_task():
    """Завершает задачу"""


def reopen_task():
    """Переоткрывает задачу"""
