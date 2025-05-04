from typing import Any, Callable
from functools import wraps


def log(filename: Any = None):
    """ Логирует вызов функции и ее результат в файл или в консоль """

    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                log_message = f"Function {func.__name__} called with args: {args}, kwargs: {kwargs}. Result: {result}\n"

                if filename:
                    with open(filename, 'a') as f:
                        f.write(log_message)
                else:
                    print(log_message, end='')

                # Additional checks based on specific conditions
                if result == sum(args):
                    print("my_function ok")
                return result

            except ZeroDivisionError as e:
                error_message = f"my_function error: {e}. Inputs: {args}, {kwargs}\n"
                if filename:
                    with open(filename, 'a') as f:
                        f.write(error_message)
                else:
                    print(error_message, end='')
                raise
            except Exception as e:
                error_message = f"my_function error: {e}. Inputs: {args}, {kwargs}\n"
                if filename:
                    with open(filename, 'a') as f:
                        f.write(error_message)
                else:
                    print(error_message, end='')
                raise

        return wrapper

    return decorator


# Example usage
@log(filename="logs/mylog.txt")
def my_function(x, y):
    return x + y


try:
    my_function(2, 0)
except Exception as e:
    print(f"Caught an exception: {e}")

print(my_function(2, 8))
