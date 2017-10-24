# -*- encoding:utf-8 -*-
import magic
import json


def validate_csv(source):
    file_info = magic.from_file(source)
    csv_valid_string = 'with CRLF line terminators'

    if not csv_valid_string in file_info:
        return False

    return True


def validate_json(source):
    with open(source, 'r') as f:
        try:
            json_str = json.loads(f.read())
            return True
        except ValueError:
            return False

#print(validate_csv("/home/oliferuk/homework/test_files/test.csv"))
#print(validate_json("/home/oliferuk/homework/test_files/test.json"))