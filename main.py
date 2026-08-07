import json

# function that loads JSON file
def load_json_file(file):
    with open(file) as file:
        data = json.load(file)
    return data

# function that checks the instance of the data
def instance_of_data(dt):
    if isinstance(dt, dict):
        print("This is a dictionary")
    elif isinstance(dt, list):
        print("This is a list")
    else:
        print("This is a plain value")

# main method
def main():
    # get user input and load the file
    json_data = input("Please enter json file path: ")
    data = load_json_file(json_data)
    print("Loaded json data:")

    # determine the type of data
    instance_of_data(data)

if __name__ == '__main__':
    main()