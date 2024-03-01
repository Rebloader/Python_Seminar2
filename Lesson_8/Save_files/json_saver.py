import json


def save_as_json(data, filename):
    with open(filename, 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=4)
