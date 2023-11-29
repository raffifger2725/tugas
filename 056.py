import random
num = random.randint(1,10)
correct = False
while correct == False:
    guess = int(input("enter the number: "))
if guess == num:
    correct = True
    print(num)        