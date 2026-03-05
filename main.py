import random
print("=========Number Guessing Game==========\n")
print("Enter the range you want(eg. 1 50): ")
a, b = map(int, input().split())
x = random.randint(a, b)
print("Guess the number")
n = 0
trial = 0
while n != x:
    n = int(input())
    if x == n:
        print("Found!")
        found = True
    elif n > x:
        print("Too high!")
    else:
        print("Too low!")
    trial += 1
print(f"You have guessed in {trial} trial!")