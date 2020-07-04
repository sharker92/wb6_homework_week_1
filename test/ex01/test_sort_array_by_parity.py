from wb6_homework_week_1.src.ex01.sort_array_by_parity import sort_array_by_parity


def test_sort_array_by_parity_example_01():
    input = [3, 1, 2, 4]
    output = [2, 4, 3, 1]

    assert output == sort_array_by_parity(input)
