from wb6_homework_week_1.src.ex19.two_sum import two_sum


def test_two_sum_example_01():
    input = [2, 7, 11, 15]
    target = 9
    output = [0, 1]

    assert output == two_sum(input, target)
