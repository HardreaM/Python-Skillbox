import csv
import re

def strip_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

file_name = input().strip()

with open(file_name, 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)

    for row in reader:
        data_dict = {}

        for i, value in enumerate(row):
            header = headers[i]
            value = value.strip() 
            value = strip_html_tags(value)
            value = re.sub(r'\s+', ' ', value)

            if '\n' in value:
                value = value.split('\n')
            else:
                value = [value]

            data_dict[header] = value

        for key, value in data_dict.items():
            if isinstance(value, list):
                value_str = ', '.join(value)
            else:
                value_str = value

            print(f"{key}: {value_str}")
        print()