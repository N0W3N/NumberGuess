import random
import sys
secretNumber = random.randint(1,10)
counter = 0
print("I'm thinking about a number between 1 and 10..")

while True:

    try:
        player_number = int(input("Enter your number: "))
        if player_number == secretNumber:
            counter = counter + 1
            print("You're right!. The secret number was {0} and it took you {1} tries.".format(secretNumber, counter) )
            sys.exit()
        else:
            counter = counter + 1
            print("You're wrong.. try it again!" + "\n" + "You have tried it {0} times so far".format(counter))
    except ValueError:
        print("Please enter a number")



