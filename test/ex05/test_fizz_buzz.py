from wb6_homework_week_1.src.ex05.fizz_buzz import fizz_buzz


def test_fizz_buzz_example_01():
    input = 15
    output = [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz"
    ]

    assert output == fizz_buzz(input)
