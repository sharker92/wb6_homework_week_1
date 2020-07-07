from wb6_homework_week_1.src.ex20.valid_anagram import is_anagram


def test_is_anagram_example_01():
    input_t = "anagram"
    input_s = "nagaram"
    output = True

    assert output == is_anagram(input_s, input_t)


def test_is_anagram_example_02():
    input_t = "rat"
    input_s = "car"
    output = False

    assert output == is_anagram(input_s, input_t)
