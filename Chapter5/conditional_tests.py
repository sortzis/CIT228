print("-------------------------Hands On #1---------------------------")
print("-------------------------Try it Yourself 5-1---------------------------")
color = "orange"
number1 = 10
number2 = 20
sports = ["football","hockey","soccer","tennis","basketball"]

print("-------------------------True Results---------------------------")
print(number1, "<", number2, number1<number2)
print(number1, "<=", number2, number1<=number2)
print(color, "== orange", color=="orange")
print("orange==orange", color.lower()=="orange")
for s in sports:
    if s == "football":
        print("Football is a sport")





print("-------------------------False Results---------------------------")
print(number1, ">", number2, number1>number2)
print(number1, ">=", number2, number1>=number2)
print(color, "!=", "orange", color!="orange")
print("orange!=orange", color.lower()!="orange")
for s in sports:
    if s == "cheerleading":
        print("Cheerleading is not a sport")