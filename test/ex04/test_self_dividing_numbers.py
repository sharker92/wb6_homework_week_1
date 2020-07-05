from wb6_homework_week_1.src.ex04.self_dividing_numbers import self_dividing_numbers


def test_self_dividing_numbers_example_01():
    input_l = 1
    input_r = 22
    output = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

    assert output == self_dividing_numbers(input_l, input_r)
