import json

# function that loads JSON file
def load_json_file(file):
    with open(file) as file:
        data = json.load(file)
    return data

# helper function that checks the instance of the data
def instance_of_data(dt):
    if isinstance(dt, dict):
        return "dict"
    elif isinstance(dt, list):
        return "list"
    else:
        return "plain"

# helper function that returns true if the user
def check_back_quit(user_input):
    return user_input == "back" or user_input == "quit"

# function that gets valid input from user given the instance of the data
def get_valid_input(instance, data):
    user_input = ""
    if instance == "dict":    # if instance is dict
        user_input = input("Enter a key to drill into, 'back' to go up, or 'quit' to exit: ")   # request input
        while not check_back_quit(user_input):  # if the user does not enter 'back' or 'quit'
            if user_input not in data.keys():   # if the user did not enter a valid key
                user_input = input("Key is invalid. Enter one of the listed keys: ")  # notify user and try again
            else:
                break # break loop because input is valid
    elif instance == "list":    # if instance is list
        user_input = input("Type a number (0-" + str(len(data) - 1) + ") to drill into, 'back' to go up, or 'quit' to exit: ") # request input
        while not check_back_quit(user_input):  # if the user does not enter 'back' or 'quit'
            if not user_input.isdigit() or (0 > int(user_input) or len(data) < int(user_input)): # if the user input is not valid integer
                user_input = input("Number is invalid: Type a number (0-" + str(len(data) - 1) + ") to drill into: ")  # notify user and try again
            else:
                break   # break loop because input is valid
    return user_input   # return user's input

# main method
def main():
    # get user input and load the file
    while True:
        try:
            json_data = input("Please enter json file path: ")
            data = load_json_file(json_data)
            break
        except FileNotFoundError:
            print("File not found. Please try again.")
        except IsADirectoryError:
            print("Directory not found. Please try again.")

    print("\nData successfully loaded.")
    current_data = data # the current data being viewed
    user_input = ""
    history = [] # the history stake

    while True:
        # determine the type of data
        instance = instance_of_data(current_data)
        if instance == "dict":    # if the instance is a dict
            keys = current_data.keys()
            print("Current data: dict with keys: [" + ", ".join(keys) + "]")
            user_input = get_valid_input(instance, current_data)
        elif instance == "list":    # if the instance is a list
            print("Current data: list with " + str(len(current_data)) + " items.")
            user_input = get_valid_input(instance, current_data)
        if user_input == "quit":    # if the user enters "quit", terminate the program
            print("\nProgram terminated.")
            break
        elif user_input == "back":  # if the user enters "back", pop from stack and go back a level, if possible
            if not history: # if history stack is empty, notify user and continue
                print("\nYou are already at the top.")
                continue
            else:   # pop from the stack and continue
                current_data = history.pop()
                print("\nBack to previous level.")
                continue
        if instance != "plain": # if the instance is not plain, add the current data to the stack
            history.append(current_data)
            if instance == "dict":
                current_data = current_data[user_input]
            elif instance == "list":
                current_data = current_data[int(user_input)]
        else:   # if instance is plain text, there is nothing to navigate.
            print("Current data: " + current_data)
            user_input = input("There is no thing else to navigate into. Enter 'back' to go up, or 'quit' to exit: ")   # requests that the user goes back or exits program
            continue
        print()

if __name__ == '__main__':
    main()