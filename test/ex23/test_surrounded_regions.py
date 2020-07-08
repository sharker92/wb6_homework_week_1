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


def test_surr_region_example_03():
    input = [["X", "O", "X"],
             ["X", "O", "X"],
             ["X", "O", "X"]]

    output = [["X", "O", "X"],
              ["X", "O", "X"],
              ["X", "O", "X"]]
    surr_region(input)

    assert output == input


def test_surr_region_example_04():
    input = [["X", "X", "X", "X", "X"],
             ["X", "O", "O", "O", "X"],
             ["X", "X", "O", "O", "X"],
             ["X", "X", "X", "O", "X"],
             ["X", "O", "X", "X", "X"]]

    output = [["X", "X", "X", "X", "X"],
              ["X", "X", "X", "X", "X"],
              ["X", "X", "X", "X", "X"],
              ["X", "X", "X", "X", "X"],
              ["X", "O", "X", "X", "X"]]
    surr_region(input)

    assert output == input


def test_surr_region_example_04():
    input = [["O", "O", "O", "O", "X", "X"],
             ["O", "O", "O", "O", "O", "O"],
             ["O", "X", "O", "X", "O", "O"],
             ["O", "X", "O", "O", "X", "O"],
             ["O", "X", "O", "X", "O", "O"],
             ["O", "X", "O", "O", "O", "O"]]

    output = [["O", "O", "O", "O", "X", "X"],
              ["O", "O", "O", "O", "O", "O"],
              ["O", "X", "O", "X", "O", "O"],
              ["O", "X", "O", "O", "X", "O"],
              ["O", "X", "O", "X", "O", "O"],
              ["O", "X", "O", "O", "O", "O"]]
    surr_region(input)

    assert output == input


def test_surr_region_example_05():
    input = [["X", "O", "X", "O", "X", "O"],
             ["O", "X", "O", "X", "O", "X"],
             ["X", "O", "X", "O", "X", "O"],
             ["O", "X", "O", "X", "O", "X"]]
    output = [["X", "O", "X", "O", "X", "O"],
              ["O", "X", "O", "X", "O", "X"],
              ["X", "O", "X", "O", "X", "O"],
              ["O", "X", "O", "X", "O", "X"]]
    surr_region(input)


def test_surr_region_example_06():
    input = [["X", "O", "X", "O", "X", "O", "O", "O", "X", "O"],
             ["X", "O", "O", "X", "X", "X", "O", "O", "O", "X"],
             ["O", "O", "O", "O", "O", "O", "O", "O", "X", "X"],
             ["O", "O", "O", "O", "O", "O", "X", "O", "O", "X"],
             ["O", "O", "X", "X", "O", "X", "X", "O", "O", "O"],
             ["X", "O", "O", "X", "X", "X", "O", "X", "X", "O"],
             ["X", "O", "X", "O", "O", "X", "X", "O", "X", "O"],
             ["X", "X", "O", "X", "X", "O", "X", "O", "O", "X"],
             ["O", "O", "O", "O", "X", "O", "X", "O", "X", "O"],
             ["X", "X", "O", "X", "X", "X", "X", "O", "O", "O"]]

    output = [["X", "O", "X", "O", "X", "O", "O", "O", "X", "O"],
              ["X", "O", "O", "X", "X", "X", "O", "O", "O", "X"],
              ["O", "O", "O", "O", "O", "O", "O", "O", "X", "X"],
              ["O", "O", "O", "O", "O", "O", "X", "O", "O", "X"],
              ["O", "O", "X", "X", "O", "X", "X", "O", "O", "O"],
              ["X", "O", "O", "X", "X", "X", "X", "X", "X", "O"],
              ["X", "O", "X", "X", "X", "X", "X", "O", "X", "O"],
              ["X", "X", "O", "X", "X", "X", "X", "O", "O", "X"],
              ["O", "O", "O", "O", "X", "X", "X", "O", "X", "O"],
              ["X", "X", "O", "X", "X", "X", "X", "O", "O", "O"]]
    surr_region(input)

    assert output == input
