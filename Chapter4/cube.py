print("-------------------------Exercise 4-8---------------------------")
numList = list(range(1,11))
print(numList)

for cube in numList:
    cube = cube**3
    print(cube)

print("-------------------------Exercise 4-9---------------------------")
cubedNum = [c**3 for c in numList]
print(cubedNum)
