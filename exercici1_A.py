# Given 2 numbers prints out witch is bigger and smaller.
def compareNum(num1, num2):
    if num1 > num2:
        print("The bigger number is {num1} and smaller is {num2}".format(num1=num1,num2=num2))
    elif num1 == num2:
        print("{num1} and {num2} are equal".format(num1=num1,num2=num2))
    else:
        print("The bigger number is {num2} and smaller is {num1}".format(num1=num1, num2=num2))
