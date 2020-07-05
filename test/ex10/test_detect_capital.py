from wb6_homework_week_1.src.ex10.detect_capital import detect_capital_use


def test_detect_capital_use_example_01():
    input = "USA"
    output = True

    assert output == detect_capital_use(input)


def test_detect_capital_use_example_02():
    input = "FlaG"
    output = False

    assert output == detect_capital_use(input)
