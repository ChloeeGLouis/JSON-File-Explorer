import json

# function that loads JSON file
def load_json_file(file):
    with open(file) as file:
        data = json.load(file)
    return data

# function that checks the instance of the data
def instance_of_data(dt):
    if isinstance(dt, dict):
        return "dict"
    elif isinstance(dt, list):
        return "list"
    else:
        return "plain"

# def navigate_json():

# main method
def main():
    terminate = False    # tracks if user quits program
    # get user input and load the file
    json_data = input("Please enter json file path: ")
    data = load_json_file(json_data)
    current_data = data

    while not terminate:
        # determine the type of data
        instance = instance_of_data(current_data)

        # if the instance is a dict
        if instance == "dict":
            keys = current_data.keys()
            key = input("Current data: dict with keys: [" + ", ".join(keys) + "]\nEnter a key to drill into: ")
            while key not in keys:
                key = input("Key is invalid. Enter one of the listed keys: ")
            current_data = current_data[key]
            print(current_data)

        # if the instance is a list
        elif instance == "list":
            print("Current data: list with " + str(len(current_data)) + " items.")
            number = input("Type a number (0-" + str(len(current_data) - 1) + ") to drill into: ")
            print("number: " + str(number))
            while 0 > int(number) or int(number) > len(current_data):
                number = input("Number is out of range: Type a number (0-" + str(len(current_data) - 1) + ") to drill into: ")
            current_data = current_data[int(number)]
            print(current_data)

        # if the instance is plain
        else:
            print("There is nothing else to navigate into.")
            terminate = True

if __name__ == '__main__':
    main()