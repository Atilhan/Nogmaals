from random import randint, randrange
import time, os, sys
game = True
kans_1 = 0
kans_2 = 0


def clearScreen(sleepTime):
    time.sleep(sleepTime)
    os.system("cls")

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.04)

clearScreen(0.0)
print ('PS you can terminate the game by typing : Terminate')
time.sleep (0)
print ('You have 10 chances to guess !')

while game:
        clearScreen(0)
        number = randint(1,1000)
        print (number)
        kans_1 = 0
        print(kans_2)

        if kans_2 == 20:
            game = False


        while kans_1 < 10:
            kans_1 += 1
            print ("Your current guessing chance:", (kans_1))
            guess = input('Guess a number between 1 & 1000 : ')
            if guess =="Terminate":
                print ('Game has been terminated')
                clearScreen(0)
                game = False 
                kans_1 = 10
            elif int(guess) == number:
                print("You've guessed right !\n")
                kans_2 += 1
                break
            else:
                print("You've guessed wrong ! try again !\n")
                time.sleep (0)
            
        kans_2 += 1

            

        



    






