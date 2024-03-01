import csv


def save_as_csv(data, filename):
    keys = data[0].keys()
    with open(filename, 'w', newline='', encoding='UTF-8') as file:
        writer = csv.DictWriter(file, keys)
        writer.writeheader()
        writer.writerows(data)
