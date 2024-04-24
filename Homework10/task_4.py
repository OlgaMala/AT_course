# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.


import pytest


@pytest.mark.usefixtures("date_start_end")
class Test:

    def test_first(self, time_func):
        print(time_func)
        pass

    def test_second(self):
        pass

    def test_third(self):
        pass
