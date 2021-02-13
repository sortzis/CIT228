rivers={
    "Missouri":["United States", "Canada"],
    "Yangtze":"China",
    "Congo":["Democratic Republic of Congo", "Central African Republic", "Angola", "Republic of the Congo", "Tanzania", "Cameroon", "Zambia", "Burundi", "Rwanda"]
}

print("-----------------Rivers & Countries-------------")
for key, value in rivers.items():
    print(f"The {key.title()} river flows through {value}")

print("--------------Rivers-------------------")
for key in rivers.keys():
    print(key.title())

print("----------------Countries---------------")
for value in rivers.values():
    print(value)