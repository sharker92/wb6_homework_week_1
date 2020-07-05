from wb6_homework_week_1.src.ex13.reverse_vowels_of_a_string import reverse_vowels


def test_reverse_vowels_example_01():
    input = "hello"
    output = "holle"

    assert output == reverse_vowels(input)


def test_reverse_vowels_example_02():
    input = "leetcode"
    output = "leotcede"

    assert output == reverse_vowels(input)


def test_reverse_vowels_example_03():
    input = "aA"
    output = "Aa"

    assert output == reverse_vowels(input)


def test_reverse_vowels_example_04():
    input = "1a2"
    output = "1a2"

    assert output == reverse_vowels(input)


def test_reverse_vowels_example_05():
    input = ".a"
    output = ".a"

    assert output == reverse_vowels(input)


def test_reverse_vowels_example_06():
    input = "a a"
    output = "a a"

    assert output == reverse_vowels(input)
