import json
glossary={
    "dictionary":"Python data type that stores key:value pairs.",
    "comments":"Comments are code lines that will not be executed.",
    "variables":"Containers for storing data values.",
    "random number":"A function to call a random number.",
    "lists":"An ordered, and changeable collection.",
    "operators":"A symbol to perform an arithmetic function in Python.",
    "tuple":"An ordered, and unchangeable collection.",
    "Elif":"The same as else/if in other programming languages.",
    "For":"The beginning of a for loop.",
    "Class":"An object constructor"
}

for k,v in glossary.items():
    print(k.title())
    print("\t",v.title())

def menu():
    selection = int(input("1-Create File, 2-Read File, 3-Add to File, 4-Quit Program"))
    while selection !=1 and selection !=2 and selection != 3 and selection != 4:
        print("You've made an invalid selection, please enter the correct number")
        selection = int(input("1-Create File, 2-Read File, 3-Add to File, 4-Quit Program"))
    return selection

def create(object):
    overwrite = input("You are about to create a new file, existing data will overwritten (q to quit, any key to continue)")
    if overwrite != "q":
        with open("Chapter10/glossary.json","w") as write_file:
            json.dump(object, write_file, indent=4, sort_keys=True)
            print("Chapter10/glossary.json has been created!")

def append(new_item):
    with open("Chapter10/glossary.json", "r+") as add_file:
        glossaryDictionary = json.load(add_file)
        glossaryDictionary.update(new_item)
        add_file.seek(0)
        json.dump(glossaryDictionary, add_file, indent=4, sort_keys=True)
        print("Data has been added to Chapter10/glossary.json")

def read():
    try:
        with open("Chapter10/glossary.json") as read_file:
            glossaryDictionary = json.load(read_file)
    except FileNotFoundError:
        print("The file does not exist or cannot be found.")
        print("Please make a different menu selection.")
    else:
        for key, value in glossaryDictionary.items():
            print("Key Term: ", key.title(), "Definition: ", value.title())

def get_key():
    term = input("Enter the Python term you've learned: ")
    return term

def get_value():
    definition = input("Enter the Python term's definition: ")
    return definition

choice = menu()
while choice != 4:
    if choice == 1:
        create(glossary)
    elif choice == 2:
        read()
    elif choice == 3:
        key = get_key()
        value = get_value()
        new_glossary = {key:value}
        append(new_glossary)
    else:
        print("There is no corresponding menu option, please try again")
    choice = menu()