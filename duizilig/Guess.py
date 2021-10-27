Number = False
import time

while not Number:
    Guess = input ('Guess the secret word ! (Answer with capital): ')
    if Guess == "Quit":
        Number = True
        print ("You've guessed right ! ")

    else:
        print ("You've guessed wrong ! try again !")
        time.sleep (2.5)


    


#question why this doens't work when I switch between the true & false:

# Number = False

# while Number:
#     Guess = input ('Guess the secret word ! (Answer with capital): ')
    
#     if Guess == "Quit":
#         Guess = True
#         print (" You've guessed right ! ")