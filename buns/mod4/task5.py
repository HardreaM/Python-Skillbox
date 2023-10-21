filename = input()

with open(filename, 'r') as file:
    data = file.read()

stats = {}

for char in data:
    if char.isalpha():
        if char in stats:
            stats[char] += 1
        else:
            stats[char] = 1

with open("result.txt", 'w') as output_file:
    for item in sorted(stats.items(), key=lambda x: x[1]):
        output_file.write(f"{item[0]}: {item[1]}\n")