import json

# prompt user for JSON file
json_file = input("Enter JSON file name: ")

# open and load the content
with open(json_file) as file:
    data = json.load(file)
print(data)