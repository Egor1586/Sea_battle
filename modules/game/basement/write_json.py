'''
Цей модуль допомагає писати у файлах `json`
'''
import os
import json

def write_json(fd: str, name_dict: dict):
    path_to_file = os.path.abspath(os.path.join(__file__, "..", "..", "static", fd))
    with open(path_to_file, "w") as data_json:
        # return json.load(data_json)
        json.dump(obj= name_dict, fp= data_json, indent=4)