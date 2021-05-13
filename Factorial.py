#!/usr/bin/env python3

# Created by Malcolm Tompkins
# Created on May 12, 2021
# Determines product of all numbers leading up to a number


def main():
    # Input

    user_input = (input("Enter your number: "))

    try:
        user_number = int(user_input)
        loop_counter = 1
        factorial = 1
        # Process and output
        while (loop_counter <= user_number):
            factorial = factorial * loop_counter
            loop_counter = loop_counter + 1
        print("{0:,.0f} is the product of the previous numbers before {1}"
              .format(factorial, user_number))

    except Exception:
        print("{} is not a positive integer".format(user_input))
    finally:
        print("Done.")


if __name__ == "__main__":
    main()
