num = int(input("How many friends do you want to invite to the party: "))
if num < 10:
    for i in range(0,num):
        name = input("Enter the name: ")
        print(name, "has been invited")
else:
    print("too many people")