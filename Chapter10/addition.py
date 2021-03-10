def addition(n,d):
    return n+d

quit=""
while quit != "q":
    try:
        n = int(input("Type an integer"))
        d = int(input("Type another integer"))
    except ValueError:
        print("You entered a non-integer")
    else:
        print(n, "+", d, "=", addition(n,d))
    finally:
        print("Thank you for the math problems!")

    quit=input("Would you like to continue, q to quit?")
