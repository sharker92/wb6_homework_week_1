from wb6_homework_week_1.src.ex06.plus_one import plus_one


def test_plus_one_example_01():
    input = [1, 2, 3]
    output = [1, 2, 4]

    assert output == plus_one(input)


def test_plus_one_example_02():
    input = [4, 3, 2, 1]
    output = [4, 3, 2, 2]

    assert output == plus_one(input)
