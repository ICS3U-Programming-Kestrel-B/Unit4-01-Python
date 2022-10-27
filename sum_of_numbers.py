#!/usr/bin/env python3

# Created By: Kestrel Bryce
# Date: Oct. 21, 2022
# This program asks for a number
# and shows all the numbers leading up to
# it as well as the sum of those numbers

import math


def main():
    # introductory paragraph
    print("This program asks for a number")
    print("and shows all the numbers leading up to")
    print("it as well as the sum of those numbers")
    print("")

    # input
    # getting user_year
    user_num_string = input("Enter a number: ")

    # initializing counter
    counter = 0

    # initializing sum
    sum = 0

    # process
    # checking that user_year is an integer
    try:
        user_num_int = int(user_num_string)
    except ValueError:
        print("\n")
        print(
            ("Please enter a valid number. {} is not valid\n").format(user_num_string)
        )
    finally:
        print("")

    # checking that user_num_int is positive
    if user_num_int < 0:
        print("Please enter a positive number")

    # output
    while counter <= user_num_int:
        # printing the numbers
        print(("{}").format(counter))
        # updating sum
        sum = sum + counter
        # incrementing counter
        counter = counter + 1
    else:
        print(("The sum is {}").format(sum))


if __name__ == "__main__":
    main()
