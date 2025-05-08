from functools import wraps


def log(filename=None):
    """Декоратор log автоматически логирует начало и конец выполнения функции"""

    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            # Подготовка сообщения для начала выполнения#
            start_message = (
                f"Starting {function.__name__} with arguments {args}, {kwargs}"
            )
            # Логируем начало, добавляя новые данные в конец файла
            if filename:
                with open(filename, "a") as file:
                    file.write(start_message + "\n")
            else:
                print(start_message)

            try:
                # Вызов функции и получение результата
                result = function(*args, **kwargs)

                # Сообщение об успешном выполнении
                message_success = f"{function.__name__} successful, result: {result}"
                # Логируем успешное завершение
                if filename:
                    with open(filename, "a") as file:
                        file.write(message_success + "\n")
                else:
                    print(message_success)

                return result

            except Exception as e:
                # Подготовка сообщения об ошибке
                message_error = f"{function.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                # Логируем ошибку
                if filename:
                    with open(filename, "a") as file:
                        file.write(message_error + "\n")
                else:
                    print(message_error)

                raise

        return wrapper

    return decorator


# Пример использования декоратора
@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


# Успешное выполнение
my_function(1, 2)


# Ошибка при запуске функции
@log()
def error_function(x):
    return 1 / x