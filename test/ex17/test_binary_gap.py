from wb6_homework_week_1.src.ex17.binary_gap import binary_gap


def test_binary_gap_example_01():
    input = 22
    output = 2

    assert output == binary_gap(input)


def test_binary_gap_example_02():
    input = 5
    output = 2

    assert output == binary_gap(input)


def test_binary_gap_example_03():
    input = 6
    output = 1

    assert output == binary_gap(input)


def test_binary_gap_example_04():
    input = 8
    output = 0

    assert output == binary_gap(input)
