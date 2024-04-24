# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.smoke
def test1_positive():
    assert all_division(12, 2) == 6


@pytest.mark.smoke
def test_2_zero():
    with pytest.raises(ZeroDivisionError):
        all_division(5, 0)


def test_3_by_itself():
    assert all_division(5, 5) == 1


def test_4_by_one():
    assert all_division(8, 1) == 8


def test_5_the_first_zero():
    assert all_division(0, 15) == 0
