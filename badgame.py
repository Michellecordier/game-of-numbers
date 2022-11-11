import random

value = random.randrange(50)
while True:
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

    elif (input1 < value):
        msg = "too low"
        print (msg)