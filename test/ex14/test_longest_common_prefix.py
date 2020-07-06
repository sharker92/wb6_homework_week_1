from wb6_homework_week_1.src.ex14.longest_common_prefix import longest_common_prefix


def test_longest_common_prefix_example_01():
    input = ["flower", "flow", "flight"]
    output = "fl"

    assert output == longest_common_prefix(input)


def test_longest_common_prefix_example_02():
    input = ["dog", "racecar", "car"]
    output = ""

    assert output == longest_common_prefix(input)


def test_longest_common_prefix_example_03():
    input = []
    output = ""

    assert output == longest_common_prefix(input)


def test_longest_common_prefix_example_04():
    input = ["aca", "cba"]
    output = ""

    assert output == longest_common_prefix(input)
