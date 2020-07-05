from wb6_homework_week_1.src.ex12.valid_palindrome import is_palindrome


def test_is_palindrome_example_01():
    input = "A man, a plan, a canal: Panama"
    output = True

    assert output == is_palindrome(input)


def test_is_palindrome_example_02():
    input = "race a car"
    output = False

    assert output == is_palindrome(input)


def test_is_palindrome_example_03():
    input = "0P"
    output = False

    assert output == is_palindrome(input)


def test_is_palindrome_example_04():
    input = "ab_a"
    output = True

    assert output == is_palindrome(input)
