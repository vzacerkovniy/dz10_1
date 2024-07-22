import datetime
from contextlib import redirect_stdout


def log(predicate=None, error_message=None, filename=None):
    """Декоратор, выдающий функцию с логами"""

    def wrapper(func):
        def inner(a):
            if not predicate(a):
                raise ValueError(error_message)
            if not filename:
                time_1 = datetime.datetime.now()
                print(f"{time_1} - Starting function...")
                result = func(a)
                print(result)
                time_2 = datetime.datetime.now()
                print(f"{time_2} - Finnish!")
                print(f"Execution time: {time_2 - time_1}")
                return func(a)
            else:
                with open(filename, "w") as f, redirect_stdout(f):
                    time_1 = datetime.datetime.now()
                    print(f"{time_1} - Starting function...")
                    result = func(a)
                    print(result)
                    time_2 = datetime.datetime.now()
                    print(f"{time_2} - Finnish!")
                    print(f"Execution time: {time_2 - time_1}")
                    return func(a)

        return inner

    return wrapper
