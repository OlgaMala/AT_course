# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize('result, a, b', [
    pytest.param(4, 8, 2, marks=pytest.mark.smoke()),
    pytest.param(8, 16, 2, marks=pytest.mark.skip())])
def test1_positive(result, a, b):
    assert all_division(a, b) == result
