def validate_args(func):
    def wrapped_func(*args):
        if len(args) < 1:
            return "Not enough arguments"
        elif len(args) > 1:
            return "Too many arguments"
        if not isinstance(args[0], int):
            return "Wrong types"
        if args[0] < 0:
            return "Negative argument"
        return func(*args)

    wrapped_func.__name__ = func.__name__
    wrapped_func.__doc__ = func.__doc__

    return wrapped_func