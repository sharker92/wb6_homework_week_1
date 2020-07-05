from wb6_homework_week_1.src.ex11.reverse_words_in_a_string_iii import reverse_words


def test_reverse_words_example_01():
    input = "Let's take LeetCode contest"
    output = "s'teL ekat edoCteeL tsetnoc"

    assert output == reverse_words(input)
