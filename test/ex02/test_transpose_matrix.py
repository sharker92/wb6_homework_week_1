from wb6_homework_week_1.src.ex02.transpose_matrix import transpose


def test_transpose_example_01():
    input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    output = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

    assert output == transpose(input)


def test_transpose_example_02():
    input = [[1, 2, 3], [4, 5, 6]]
    output = [[1, 4], [2, 5], [3, 6]]

    assert output == transpose(input)
