import random
# Asks the user to guess a random number from 0 to 100.
def guessFrom0to100():
    ans = random.randrange(0, 100)
    low = 0
    high = 100
    correct = False
    while (not correct):
        guess = int(input("Guess a number from {low} to {high}: ".format(low=low, high=high)))
        if guess == ans:
            print("Well done! that's the number! {num}".format(num=guess))
            correct = True
        elif guess < ans:
            print("The number is bigger than {num}".format(num=guess))
            low = guess
        else:
            print("The number is smaller than {num}".format(num=guess))
            high = guess
