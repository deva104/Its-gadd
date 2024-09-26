import math
import random
import time


def main():
    lower = int(input("Enter Lower bound: "))
    upper = int(input("Enter Upper bound: "))

    random.seed(time.time())

    x = random.randint(lower, upper)
    total_chances = math.ceil(math.log2(upper - lower + 1))

    print(f"         You've only {total_chances} chances to guess the integer!")

    count = 0
    flag = False

    while count < total_chances:
        count += 1

        guess = int(input("Guess a number: "))

        if x == guess:
            print(f"Congratulations you did it in {count} try!")
            flag = True
            break
        elif x > guess:
            print("You guessed too small!")
        else:
            print("You guessed too high!")

    if not flag:
        print(f"\nThe number is {x}")
        print("\tBetter Luck Next time!")


main()
















































