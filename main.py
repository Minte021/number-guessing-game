import random
x = random.randint(1, 100)
print("=========Number Guessing Game==========\n")
print("Guess a number from 1 - 100!")
n = 0
while n != x:
    n = int(input())
    if x == n:
        print("Found!")
        found = True
    elif n > x:
        print("Too high!")
    else:
        print("Too low!")
