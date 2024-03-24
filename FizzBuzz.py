import random

# the number will loop through 1 -100
# if divisible  by 3 print fizz
# if divisible by 5, print buzz
# if divisible by 3 and 6 then, print fizzbuzz

choice = int(input("How many Fizz Buzz "))


def fizzBuzz(choice):
    for num in range(1, choice):
        if num % 5 == 0 and num % 3 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("buzz")
        else:
            print(num)


fizzBuzz(choice)
