#!/usr/bin/env python3

# Created by: Emmanuel
# Created on: Nov 2022
# This program uses a while loop and multiplies


def main():
    # this function finds factorial of a number using while loop

    # input
    positive_string = input("Enter a positive integer: ")
    print("")

    # variables
    factorial = 1
    loop_counter = 0

    # process & output
    try:
        positive_integer = int(positive_string)
        if positive_integer >= 0:
            while loop_counter < positive_integer:
                loop_counter = loop_counter + 1
                factorial = factorial * loop_counter
            print("{0}! = {1}.".format(positive_integer, factorial))
        else:
            print("You did not enter a positive integer")
    except ValueError:
        print("{0} is not a valid input".format(positive_string))
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()