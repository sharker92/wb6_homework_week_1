from wb6_homework_week_1.src.ex15.number_complement import find_complement


def test_find_complement_example_01():
    input = 5
    output = 2

    assert output == find_complement(input)


def test_find_complement_example_02():
    input = 1
    output = 0

    assert output == find_complement(input)
