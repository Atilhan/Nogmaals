game = True
import time, os, sys

def clearScreen(sleepTime):
    time.sleep(sleepTime)
    os.system("cls")

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.04)

print ('PS you can terminate the game by typing : (Terminate)')
while game:

        from random import randint, randrange
        number = randint(1,1000)

        for x in range(10):
            guess = (int(input('Guess a number between 1 & 1000 : ')))


            if guess =="Terminate":
                print ('Game has been terminated')
                break

            if guess == number:
                print_slow("You've guessed right !\n")
                break

            else:
                print_slow("You've guessed wrong ! try again !\n")
                time.sleep (1)







