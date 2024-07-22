import pytest

from src.decorator import log


def predicate_is_int(x):
    """Проверка на целое число"""
    return type(x) is int


@log(predicate_is_int, "Значение должно быть целым числом", "mylog.txt")
def square(x):
    """Функция возведения числа в квадрат"""
    return x * x


with pytest.raises(ValueError, match="Значение должно быть целым числом"):
    square("4")
assert square(2) == 4
assert square(-2) == 4


@log(predicate_is_int, "Значение должно быть целым числом")
def square(x):
    return x * x
