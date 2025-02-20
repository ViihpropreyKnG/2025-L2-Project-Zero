# Functions go here
from idlelib.rpc import response_queue


def number_check(question, num_type, exit_code=None):


    if num_type == "integer":
        error = "Oops - please enter an integer more than zero."
        change_to = int
    else:
        error = "Oops - please enter a number more than zero."
        change_to = float

    while True:
        response = input(question).lower()

        if response == "xxx":
            return response

        try:
            response = int(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)



while True:
    print()

    my_float = number_check(question="Please enter a number more than 0: ", num_type="float")
    print(f"Thanks. You chose {my_float}")
    print()
    my_int = number_check(question="Please enter an integer more than 0", num_type="integer", exit_code="")

    if my_int == "":
        print("You have chosen infinite mode.")
    else:
        print(f"Thanks. You chose {my_int}")
