from typing import Any


def log(filename: Any = None):
    """ Логирует вызов функции и ее результат в файл или в консоль """
    import pytest
    from io import StringIO
    import sys
    from typing import Any, Callable
    from functools import wraps

    def log(filename: Any = None):
        """ логирует вызов функции и ее результат в файл или в консоль """

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

    @log(filename="mylog.txt")
    def my_function(x, y):
        return x + y

    class TestMyFunction:

        @pytest.fixture(autouse=True)
        def setup(self):
            # Перехватываем вывод в stdout для проверки логов
            self.held_output = StringIO()
            self.original_stdout = sys.stdout
            sys.stdout = self.held_output

            yield

            # Возвращаем стандартный поток вывода
            sys.stdout = self.original_stdout

        def test_addition(self):
            result = my_function(2, 3)
            assert result == 5

        def test_zero_input(self):
            result = my_function(2, 0)
            assert result == 2

        def test_large_numbers(self):
            result = my_function(1000000, 2000000)
            assert result == 3000000

        def test_negative_numbers(self):
            result = my_function(-1, -2)
            assert result == -3

        def test_mixed_signs(self):
            result = my_function(-5, 5)
            assert result == 0

        def test_logging(self):
            # Проверяем, что логирование работает корректно
            my_function(2, 3)
            output = self.held_output.getvalue()
            assert "Function my_function called with args: (2, 3), kwargs: {}. Result: 5" in output

        def test_exception_handling(self):
            # Проверяем обработку исключений
            with pytest.raises(ZeroDivisionError):
                my_function(2, 0)

    if __name__ == "__main__":
        pytest.main()
