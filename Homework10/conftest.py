from datetime import datetime
import time
import pytest


@pytest.fixture(scope="class")
def date_start_end():
    print("Начало выполнения тестов класса ", datetime.now())
    yield
    print("Окончание выполенния тестов класса ", datetime.now())


@pytest.fixture
def date_2():
    print(datetime.now)


@pytest.fixture
def time_func():
    t = time.time()
    yield
    t2 = time.time()
    el_time = t2 - t
    print("Время выполнения", el_time)
