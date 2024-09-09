def fizzbuzz(int_num: int):
    if int_num % 3 == 0 and int_num % 5 == 0:
        return "FizzBuzz"

    elif int_num % 5 == 0:
        return "Buzz"

    elif int_num % 3 == 0:
        return "Fizz"

    else:
        return int_num