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

print("Dictionary")
print("\t",glossary["dictionary"])

print("Comments")
print("\t",glossary["comments"])

print("Variables")
print("\t",glossary["variables"])

print("Random Number")
print("\t",glossary["random number"])

print("Lists")
print("\t",glossary["lists"])

print("----------------Try it Yourself 6-4-----------------")

for k,v in glossary.items():
    print(k.title())
    print("\t",v.title())
