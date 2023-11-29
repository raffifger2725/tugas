import random
num = random.randint(1,10)
correct = False
while correct == False:
    guess = int(input("Enter the  number: "))
    if guess == num:
        correct = True
    elif guess > num:
        print("too high")
    else:
        print("too low")