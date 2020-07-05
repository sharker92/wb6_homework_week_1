from wb6_homework_week_1.src.ex03.flipping_an_image import flip_and_invert_image


def test_transpose_example_01():
    input = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    output = [[1, 0, 0], [0, 1, 0], [1, 1, 1]]

    assert output == flip_and_invert_image(input)


def test_transpose_example_02():
    input = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
    output = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]]

    assert output == flip_and_invert_image(input)
