#!/usr/bin/python3.5

import json

def http_headers_to_json(in_path, out_path):

    in_file = open(in_path)

    if in_file.read(3) == 'GET':
        in_file.seek(0)
        line = in_file.readline()
        line_1 = list(line.split(' '))
        dic = {'method': line_1[0], 'uri': line_1[1], 'protocol': line_1[2]}

        for line in in_file:
            temp = line.strip('\n').split(': ')

            if temp[0] != '':
                dic2 = {temp[0]: temp[1]}
                dic.update(dic2)
        jsonarray = json.dumps(dic)
        out_file = open(out_path, 'w')
        out_file.write(jsonarray)
        out_file.close()
        in_file.close()
    else:
        in_file.seek(0)

    in_file = open(in_path)

    if in_file.read(4) == 'HTTP':
        in_file.seek(0)
        line = in_file.readline()
        dic = {'protocol': line[0:8], 'status_code': line[9:12], 'status_message': line[13::].strip('\n')}

        for line in in_file:
            temp = line.strip('\n').split(': ')

            if temp[0] != '':
                dic2 = {temp[0]: temp[1]}
                dic.update(dic2)
        jsonarray = json.dumps(dic)
        out_file = open(out_path, 'w')
        out_file.write(jsonarray)
        out_file.close()
        in_file.close()
    else:
        return
