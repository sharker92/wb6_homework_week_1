from wb6_homework_week_1.src.ex21.friend_circles import find_circle_num


def test_find_circle_num_example_01():
    input = [[1, 1, 0],
             [1, 1, 0],
             [0, 0, 1]]
    output = 2

    assert output == find_circle_num(input)


def test_find_circle_num_example_02():
    input = [[1, 1, 0],
             [1, 1, 1],
             [0, 1, 1]]
    output = 1

    assert output == find_circle_num(input)


def test_find_circle_num_example_03():
    input = [[1, 1, 1],
             [1, 1, 1],
             [1, 1, 1]]
    output = 1

    assert output == find_circle_num(input)


def test_find_circle_num_example_04():
    input = [[1, 0, 0, 1],
             [0, 1, 1, 0],
             [0, 1, 1, 1],
             [1, 0, 1, 1]]
    output = 1

    assert output == find_circle_num(input)


def test_find_circle_num_example_05():
    input = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
             [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
             [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
             [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]
    output = 8

    assert output == find_circle_num(input)
