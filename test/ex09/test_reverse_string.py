from wb6_homework_week_1.src.ex09.reverse_string import reverse_string


def test_reverse_string_example_01():
    input = ["h", "e", "l", "l", "o"]
    output = ["o", "l", "l", "e", "h"]

    reverse_string(input)

    assert output == input


def test_reverse_string_example_02():
    input = ["H", "a", "n", "n", "a", "h"]
    output = ["h", "a", "n", "n", "a", "H"]

    reverse_string(input)

    assert output == input
