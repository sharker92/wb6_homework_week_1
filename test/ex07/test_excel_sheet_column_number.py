from wb6_homework_week_1.src.ex07.excel_sheet_column_number import title_to_number


def test_title_to_number_example_01():
    input = "A"
    output = 1

    assert output == title_to_number(input)


def test_title_to_number_example_02():
    input = "AB"
    output = 28

    assert output == title_to_number(input)


def test_title_to_number_example_03():
    input = "ZY"
    output = 701

    assert output == title_to_number(input)
