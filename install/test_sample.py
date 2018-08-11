"""Test Sample."""


def func(x):
    """Функция прибавления единицы."""
    return x + 1


def test_answer():
    """Тестирование функции прибавления единицы."""
    assert func(3) == 5
