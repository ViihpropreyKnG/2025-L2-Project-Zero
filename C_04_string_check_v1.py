# Functions go here
def string_check(question, valid_ans_list):
    """Checks that users enter the full word or the first letter of word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            if response == item:
                return item

        # check if the response is the entire word
            elif response == item[0]:
                return item

        print(f"Please choose an option from {valid_ans_list}")

# Main routine goes here
levels = ['easy', 'medium', 'hard']

like_coffee = string_check(question="Do you like coffee?", valid_ans_list=['yes', 'no'])
print(f"You chose {like_coffee}")
choose_level = string_check(question="Choose a level: ", levels)
print(f"You chose {choose_level}")
