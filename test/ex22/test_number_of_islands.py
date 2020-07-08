from wb6_homework_week_1.src.ex22.number_of_islands import num_islands


def test_num_islands_example_01():
    input = [["1", "1", "1", "1", "0"],
             ["1", "1", "0", "1", "0"],
             ["1", "1", "0", "0", "0"],
             ["0", "0", "0", "0", "0"]]
    output = 1

    assert output == num_islands(input)


def test_num_islands_example_02():
    input = [["1", "1", "0", "0", "0"],
             ["1", "1", "0", "0", "0"],
             ["0", "0", "1", "0", "0"],
             ["0", "0", "0", "1", "1"]]
    output = 3

    assert output == num_islands(input)


def test_num_islands_example_03():
    input = [["1", "0", "1", "1", "0", "1", "1"]]
    output = 3

    assert output == num_islands(input)
