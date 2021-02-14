import random
counter = 0
numberCorrect = 0
numberIncorrect = 0
while counter < 10:
    randNumber1 = random.randrange(1,1000)
    randNumber2 = random.randrange(1,1000)
    correctAnswer = int(randNumber1 + randNumber2)
    yourAnswer = int(input(f"What is the integer value of {randNumber1} + {randNumber2}?"))
    if correctAnswer==yourAnswer:
        print("Great job, you answered correctly!")
        numberCorrect +=1
    else:
        print("Oops, the correct answer is ",correctAnswer)
        numberIncorrect += 1
        if numberIncorrect > 5:
            print("See a tutor ASAP")
            break
    counter +=1

print("You answered ", numberCorrect, " questions correctly!")
print("You answered ", numberIncorrect, " questions incorrect.")
print("Thanks for playing!")