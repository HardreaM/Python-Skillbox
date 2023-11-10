def memoize(func):
    memory = dict()

    def wrapped_func(*n):
        if n in memory:
            return memory[n]
        else:
            result = func(*n)
            memory[n] = result
            return result

    wrapped_func.__name__ = func.__name__
    wrapped_func.__doc__ = func.__doc__

    return wrapped_func


@memoize
def fibonacci(n):
    '''Docs'''
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    print(fibonacci(450))