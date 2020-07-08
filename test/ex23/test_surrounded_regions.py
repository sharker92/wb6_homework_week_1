from wb6_homework_week_1.src.ex23.surrounded_regions import surr_region


def test_surr_region_example_01():
    input = [["X", "X", "X", "X"],
             ["X", "O", "O", "X"],
             ["X", "X", "O", "X"],
             ["X", "O", "X", "X"]]

    output = [["X", "X", "X", "X"],
              ["X", "X", "X", "X"],
              ["X", "X", "X", "X"],
              ["X", "O", "X", "X"]]
    surr_region(input)

    assert output == input


def test_surr_region_example_02():
    input = [["O", "O", "O"],
             ["O", "O", "O"],
             ["O", "O", "O"]]

    output = [["O", "O", "O"],
              ["O", "O", "O"],
              ["O", "O", "O"]]
    surr_region(input)

    assert output == input
