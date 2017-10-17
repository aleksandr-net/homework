#!/usr/bin/python3.5
import datetime


def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        raise ValueError("Неправильный формат даты. Должно быть 'ГГГГ-ММ-ДД ЧЧ:ММ:СС'")


def compare(start_date, end_date):
    try:
        start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S')

        if start_date > end_date:
            raise ValueError

    except ValueError:
        raise ValueError('Дата окончания задачи не может быть в прошлом!')
