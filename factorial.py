#!/usr/bin/env python3

# Created by Ethan Prieur
# Created on March 2022
# This is a program that checks if a certain year is a leap year


def main():
    # This function is the main function

    counter = 1
    number_pro = 1

    # Input

    number_as_string = input("Enter a Number: ")

    # Process & Output

    try:
        number_as_int = int(number_as_string)
        if number_as_int == 0:
            print("The Product is 1")
        elif number_as_int < 0:
            print("That isn't a Positive Integer")
        else:
            while counter <= number_as_int:
                number_pro = number_pro * counter
                counter = counter + 1
            print("The product is {0}".format(number_pro))
    except Exception:
        print("Come on dude enter a number")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
