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


def validate_custom(source):
    pass


def validate_filetype(source):
    file_info = magic.from_file(source)
    csv_valid_string = 'with CRLF line terminators'
    xlsx_valid_string = 'Microsoft OOXML'
    xls_valid_string = 'Composite Document File V2'
    ods_valid_string = 'OpenDocument Spreadsheet'
    xml_valid_string = 'XML 1.0 document'

    if csv_valid_string in file_info:
        return 'csv'
    elif xlsx_valid_string in file_info:
        return 'xlsx'
    elif xls_valid_string in file_info:
        return 'xls'
    elif ods_valid_string in file_info:
        return 'ods'
    elif xml_valid_string in file_info:
        return 'xml'
    elif validate_json(source):
        return 'json'
    elif validate_custom(source):
        return 'custom'
    else:
        return 'unknown'


def read_params(source):
    if validate_filetype(source) == 'csv':
        # read as csv
        pass
    if validate_filetype(source) == 'custom':
        # read as custom
        pass

#print(validate_csv("/home/oliferuk/homework/test_files/test.csv"))
#print(validate_json("/home/oliferuk/homework/test_files/test.json"))
#print(validate_xlsx("/home/oliferuk/homework/test_files/test.xlsx"))
#print(validate_xls("/home/oliferuk/homework/test_files/test1.xls"))
read_params("/home/oliferuk/homework/test_files/test.txt")