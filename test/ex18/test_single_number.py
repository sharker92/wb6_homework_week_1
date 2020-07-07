from wb6_homework_week_1.src.ex18.single_number import single_number


def test_single_number_example_01():
    input = [2, 2, 1]
    output = 1

    assert output == single_number(input)


def test_single_number_example_02():
    input = [4, 1, 2, 1, 2]
    output = 4

    assert output == single_number(input)


def test_single_number_example_03():
    input = [1]
    output = 1

    assert output == single_number(input)


def test_single_number_example_04():
    input = [1, 3, 1, -1, 3]
    output = -1

    assert output == single_number(input)
