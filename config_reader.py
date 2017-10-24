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


def validate_filetype(source):
    file_info = magic.from_file(source)
    csv_valid_string = 'with CRLF line terminators'
    xlsx_valid_string = 'Microsoft OOXML'
    xls_valid_string = 'Composite Document File V2'
    ods_valid_string = 'OpenDocument Spreadsheet'
    xml_valid_string = 'XML 1.0 document'

    if csv_valid_string in file_info:
        print("It's csv!")
    elif xlsx_valid_string in file_info:
        print("It's xlsx!")
    elif xls_valid_string in file_info:
        print("It's xls!")
    elif ods_valid_string in file_info:
        print("It's ods!")
    elif xml_valid_string in file_info:
        print("It's xml!")
    elif validate_json(source):
        print("It's json!")
    else:
        print("Unknown filetype")


def read_params(source):
    return validate_filetype(source)

#print(validate_csv("/home/oliferuk/homework/test_files/test.csv"))
#print(validate_json("/home/oliferuk/homework/test_files/test.json"))
#print(validate_xlsx("/home/oliferuk/homework/test_files/test.xlsx"))
#print(validate_xls("/home/oliferuk/homework/test_files/test1.xls"))
read_params("/home/oliferuk/homework/test_files/test.txt")