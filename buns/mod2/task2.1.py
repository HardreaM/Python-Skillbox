import csv

file_name = input().strip()

with open(file_name, 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)
    
    data = []
    
    for row in reader:
        if all(row):
            data.append(row)

print(headers)
print(data)