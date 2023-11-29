import random
num = random.randint(1,5)
guess = int(input("Enter the number: "))
if guess == num:
    print("well done")
elif guess > num:
    print("too high")
    guess = int(input("Guess again: "))
    if guess == num:
        print("correct")
    else:
        print("you lose")
elif guess < num:
    print("too low")
    guess = int(input("guess again:"))
    if guess == num:
        print("correct")
    else:
        print("you lose")