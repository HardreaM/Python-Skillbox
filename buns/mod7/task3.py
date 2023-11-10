import time
from task1 import validate_args
from task2 import memoize

def timer(func):
    def wrapped_func(*args):
        if not hasattr(func, 'total_time'):
            func.total_time = 0

        if not hasattr(func, 'call_count'):
            func.call_count = 0

        if func.call_count == 0:
            func.start_time = time.time()

        func.call_count += 1
        result = func(*args)
        func.call_count -= 1

        if func.call_count == 0:
            end_time = time.time()
            func.total_time += (end_time - func.start_time)
            print(f"Время выполнения {func.__name__}: {func.total_time} секунд")

        return result

    wrapped_func.__name__ = func.__name__
    wrapped_func.__doc__ = func.__doc__

    return wrapped_func


@validate_args
@memoize
@timer
def fibonacci(n):
    '''Docs'''
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(200)) #С Мемоизацией для n=200: 0.00099s   Без мемоизации для n=30: 3.8s: