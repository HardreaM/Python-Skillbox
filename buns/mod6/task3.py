def is_armstrong(number):
    digits = [int(i) for i in str(number)]
    degree = len(digits)
    summary = 0
    for digit in digits:
        summary += digit ** degree
    return summary == number

def get_armstrong_generator():
    ARMSTRONG_MAX_VALUE = 115_132_219_018_763_992_565_095_597_973_971_522_401
    for i in range(10, ARMSTRONG_MAX_VALUE + 1):
        if is_armstrong(i):
            yield i

armstrong_generator = get_armstrong_generator()

def get_armstrong_numbers():
    return next(armstrong_generator)


for i in range(8):
    print(get_armstrong_numbers(), end=' ')