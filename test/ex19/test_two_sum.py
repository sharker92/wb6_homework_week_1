from wb6_homework_week_1.src.ex19.two_sum import two_sum


def test_two_sum_example_01():
    input = [2, 7, 11, 15]
    target = 9
    output = [0, 1]

    assert output == two_sum(input, target)


def test_two_sum_example_02():
    input = [3, 2, 4]
    target = 6
    output = [1, 2]

    assert output == two_sum(input, target)


def test_two_sum_example_03():
    input = [3, 3]
    target = 6
    output = [1, 0]

    assert output == two_sum(input, target)
