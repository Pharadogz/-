import pytest

from src.decorators import error_function, my_function


# Тест успешного выполнения функции
def test_my_function_success(capsys):
    result = my_function(1, 2)
    assert result == 3


# Тест обработки исключения в функции с делением на ноль
def test_error_function_zero_division(capsys):
    with pytest.raises(Exception):
        error_function(0)
    captured = capsys.readouterr()
    assert (
        captured.out
        == "Starting error_function with arguments (0,), {}\nerror_function error: ZeroDivisionError. Inputs: (0,), {}\n"
    )


# Тест логирования в файл
def test_logging_to_file():
    my_function(1, 2)
    with open("mylog.txt", "r") as file:
        log_content = file.readlines()
    assert "Starting my_function with arguments (1, 2), {}\n" == log_content[0]


# Тест логирования ошибки функции в файл
def test_error_logging_to_file():
    with pytest.raises(Exception):
        error_function(0)
    with open("mylog.txt", "r") as file:
        log_content = file.readlines()
    assert "Starting my_function with arguments (1, 2), {}\n" == log_content[0]