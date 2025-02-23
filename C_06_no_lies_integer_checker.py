# Functions go here


def int_check(question):

    error = "Oops - please enter an integer"

    while True:

        try:
            response = int(input(question))


            return response

        except ValueError:
            print(error)



while True:
    print()

    name = input("Name: ")

    age = int_check("Age: ")

    if age < 12:
        print(f"Sorry, {name} is too young")
        continue
    elif age > 120:
        print(f"Sorry, {name} is too old")
        continue
    else:
        print(f"{name} bought a ticket")

