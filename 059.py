import random

colour = random.choice (["red", "blue", "green", "white", "pink"])
print("Select from red, blue, green, white or pink")
tryagain = True
while tryagain == True:
    theirchoices = input("enter the colour: ")
    theirchoices = theirchoices.lower()
    if colour == theirchoices:
        print("well done")
        tryagain = False
    else:
        if colour == "red":
            print("i bet you are seeing red right now!")
        elif colour == "blue":
            print("dont feel blue")
        elif colour == "green":
            print("i bet you are green with envy right now")
        elif colour == "white":
            print("are you white as a sheet, as your didn't guess correctly")
        elif colour == "pink":
            print("shame you are not feeling in the pink,as you got it wrong")