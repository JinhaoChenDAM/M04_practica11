# Prints out 5 names, and ask to choose one then prints out a diffrent result
# if the input is not in those 5 names, prints out not in list.
def names():
    nameList = ["Jinhao", "Guillermo", "Fernando", "Alex", "Bili"]
    chosenName = input("Choose 1 name from {name1} {name2} {name3} {name4} {name5}: "
                        .format(name1=nameList[0], name2=nameList[1], name3=nameList[2], name4=nameList[3],
                                name5=nameList[4]))
    if chosenName not in nameList:
        print("This name is not from the 5 names given above")
    if chosenName == nameList[0]:
        print("Hello {name}!".format(name=nameList[0]))
    if chosenName == nameList[1]:
        print("Hello {name}!".format(name=nameList[1]))
    if chosenName == nameList[2]:
        print("Hello {name}!".format(name=nameList[2]))
    if chosenName == nameList[3]:
        print("Hello {name}!".format(name=nameList[3]))
    if chosenName == nameList[4]:
        print("Hello {name}!".format(name=nameList[4]))
