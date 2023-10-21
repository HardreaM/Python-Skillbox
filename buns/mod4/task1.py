def check_list(list):
    if list.count(list[0]) == len(list):
        return "Все числа равны"
    if len(set(list)) == len(list):
        return "Все числа разные"
    return "Есть равные и неравные числа"

print(check_list(list(map(int, input().split()))))