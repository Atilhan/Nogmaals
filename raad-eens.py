from random import randint, randrange
import time, os, sys
game = True
x = 0


def clearScreen(sleepTime):
    time.sleep(sleepTime)
    os.system("cls")

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.04)

print ('PS you can terminate the game by typing :Terminate')
while game:
        clearScreen(3)
        number = randint(1,1000)
        print (number)
        x = 0

        while x < 10:
            x += 1
            print ("Dit is je", (x) , "kans")
            guess = input('Guess a number between 1 & 1000 : ')
            if guess =="Terminate":
                print ('Game has been terminated')
                clearScreen(1)
                game = False 
                x = 10

            elif int(guess) == number:
                print_slow("You've guessed right !\n")
                break
            else:
                print_slow("You've guessed wrong ! try again !\n")
                time.sleep (1)

    






