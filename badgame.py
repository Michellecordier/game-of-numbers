import random

def wrongGuess(msg, guessesRemaining):
    print (msg)
    guessesRemaining -= 1
    print ("guesses remaining " + str(guessesRemaining))
    return guessesRemaining

value = random.randrange(50)
guessesRemaining = 6
while guessesRemaining > 0 :
    msg = "guess a number"
    print(msg)
    input_str = input()
    input1 = int(input_str)
    if (input1 == value):
        msg = "yay!!!"
        print(msg)
        break

    elif (input1 > value):
        msg = "too high"
        guessesRemaining = wrongGuess (msg, guessesRemaining)

    elif (input1 < value):
        msg = "too low"
        guessesRemaining = wrongGuess (msg, guessesRemaining)
