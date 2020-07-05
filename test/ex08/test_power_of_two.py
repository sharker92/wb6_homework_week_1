from wb6_homework_week_1.src.ex08.power_of_two import is_power_of_two


def test_is_power_of_two_example_01():
    input = 1
    output = True

    assert output == is_power_of_two(input)


def test_is_power_of_two_example_02():
    input = 16
    output = True

    assert output == is_power_of_two(input)


def test_is_power_of_two_example_02():
    input = 218
    output = False

    assert output == is_power_of_two(input)
