# Functions go here
from zipfile import error


def int_check(question, low, high):

    error = f"Oops - please enter an integer between {low} and {high}."

    while True:

        try:
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)



while True:
    print()

    my_num = int_check(question="Choose a number: ", low=1, high=10)
    print(f"You chose {my_num}")
