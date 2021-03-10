import random
def division(n,d):
    return n/d

quit=""
while quit != "q":    
    n=random.randrange(0,10)
    d=random.randrange(0,10) 
    try:
        print(n, "/", d, "=", division(n,d))
    except ZeroDivisionError:
       print("You have a divide by zero error, the denominator has been modified")
       d=random.randrange(1,10)
       print(n, "/", d, "=", division(n,d))
    except:
       print("You have an error, please try again")
    finally:
        print("Thanks for playing!")   
    
    quit=input("Would you like to continue, q to quit? ")