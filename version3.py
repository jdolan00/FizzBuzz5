# produces range from 1-100
for num in range(1, 101):
    # if num is divisible by both 3 and 5 it is caught in this conditional and fizzbuzz is printed
    if num % 3 == 0 and num % 5 == 0:
        print(num, "FizzBuzz")
    # if num is divisible by 3 it is caught in this conditional and fizz is printed
    elif num % 3 == 0:
        print(num, "Fizz")
    # if num is divisible by 5 it is caught in this conditional and buzz is printed
    elif num % 5 == 0:
        print(num, "Buzz")
    else:
        # if number is not divisible by either it is not printed
        print(num)
