from src.fizzbuzz.fizzbuzz_kata import fizzbuzz

def test_fizz_three():
    assert fizzbuzz(3) == "Fizz"

def test_mult_three():
    assert fizzbuzz(9) == "Fizz"

def test_five_buzz():
    assert fizzbuzz(5) == "Buzz"

def test_mult_five():
    assert fizzbuzz(25) == "Buzz"

def test_mult_three_five():
    assert fizzbuzz(15) == "FizzBuzz"