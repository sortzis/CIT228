rivers={
    "Missouri":["United States", "Canada"],
    "Yangtze":"China",
    "Congo":["Democratic Republic of Congo", "Central African Republic", "Angola", "Republic of the Congo", "Tanzania", "Cameroon", "Zambia", "Burundi", "Rwanda"]
}

for key, value in rivers.items():
    if type(value)==list:
        print(f"The {key.title()} river flows through: ")
        for v in value:
            print("\t\t\t\t",v)
    else:
        print(f"The {key.title()} river flows through {value.title()}")