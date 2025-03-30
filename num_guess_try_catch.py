#!/usr/bin/env python3
# Created by Dylan Mutabazi
# Date : March 2025
# This program makes the use guess randomly generated number 0 - 9 with try catch
import random


def main():
    # creates a random number between 0-9 and asks user to guess the number
    random_number = random.randint(0, 9)
    number_as_string = input("Guess a number between 0 - 9: ")

    try:
        # converts number_as_string into an inte
        number_as_int = int(number_as_string)

    # if user input can not be converted into an int then it prints our the message
    except ValueError:
        print(number_as_string, " is not a integer")

    # else if it can it tells the user if they got it right or wrong using else if
    else:
        if number_as_int == random_number:
            print("Good guess mate !!!")
        else:
            print("good try but your number was:", random_number)

    # outro message
    finally:
        print("")
        print("Thanks for playing")


if __name__ == "__main__":
    main()
