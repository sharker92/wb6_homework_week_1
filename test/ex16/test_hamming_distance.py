from wb6_homework_week_1.src.ex16.hamming_distance import hamming_distance


def test_hamming_distance_example_01():
    input_x = 1
    input_y = 4
    output = 2

    assert output == hamming_distance(input_x, input_y)
