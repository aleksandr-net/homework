# -*- encoding:utf-8 -*-
import magic
import json


def validate_json(source):
    with open(source, 'r') as f:
        try:
            json_str = json.loads(f.read())
            return True
        except ValueError:
            return False

def validate_csv(source):
    file_info = magic.from_file(source)
    csv_valid_string = 'with CRLF line terminators'

    if not csv_valid_string in file_info:
        return False

    return True


def validate_xlsx(source):
    file_info = magic.from_file(source)
    xlsx_valid_string = 'Microsoft OOXML'

    if not xlsx_valid_string in file_info:
        return False

    return True


def validate_xls(source):
    file_info = magic.from_file(source)
    xls_valid_string = 'Composite Document File V2'

    if not xls_valid_string in file_info:
        return False

    return True


def validate_ods(source):
    file_info = magic.from_file(source)
    ods_valid_string = 'OpenDocument Spreadsheet'

    if not ods_valid_string in file_info:
        return False

    return True

#print(validate_csv("/home/oliferuk/homework/test_files/test.csv"))
#print(validate_json("/home/oliferuk/homework/test_files/test.json"))
#print(validate_xlsx("/home/oliferuk/homework/test_files/test.xlsx"))
#print(validate_xls("/home/oliferuk/homework/test_files/test1.xls"))
print(validate_ods("/home/oliferuk/homework/test_files/test.csv"))