import random

value = random.randrange(50)
guessesRemaining = 6
while guessesRemaining > 0 :
    msg = "guess a number"
    print(msg)
    input_str = input()
    input1 = int(input_str)
    if (input1 == value):
        msg = "yay"
        print(msg)
        break

    elif (input1 > value):
        msg = "too high"
        print (msg)
        guessesRemaining -= 1
        print ("guesses remaining " + str(guessesRemaining))

    elif (input1 < value):
        msg = "too low"
        print (msg)
        guessesRemaining -= 1
        print ("guesses remaining " + str(guessesRemaining))
