from random import randint, randrange
import time, os, sys
game = True
kans_1 = 0
kans_2 = 0
rounds = 1

def clearScreen(sleepTime):
    time.sleep(sleepTime)
    os.system("cls")

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.03)

clearScreen(1)
print_slow ('PS you can terminate the game by typing : Terminate \n')
clearScreen(1)
print_slow ('You have 10 chances to guess !')
time.sleep (3)

while game:
    clearScreen(0)
    number = randint(1,1000)
    kans_1 = 0
    print (number)
    print('------------------------------------')
    print("This is round:", rounds)
    print('------------------------------------')
    print("Points earned:", (kans_2))
    print('------------------------------------')
    rounds += 1

    if rounds == 20:
        game = False

    elif kans_2 == 20:
        game = False

    while kans_1 < 10:
        kans_1 += 1
        print ("Your current guessing chance (You have 10 chances to guess !):", (kans_1))
        guess = input('Guess a number between 1 & 1000 : ')
        print('\n')

        if guess =="Terminate":
            print ('Game has been terminated')      
            clearScreen(1)
            game = False 
            kans_1 = 10
            break

        guess = int(guess)
        if (guess) == number:
            print("You've guessed right !\n")
            kans_2 += 1
            break

        else:
            print("You've guessed wrong ! try again !\n")
            clearScreen(0)
            time.sleep (0)     

        if  guess > number and guess < number + 20:
            print("You're close! only 20 difference lower between", (guess))
        elif guess < number and guess > number - 20:
            print("You're close ! only 20 difference higher between", (guess))
        elif guess > number and guess < number + 50:
            print("You're close! only 50 difference lower between", (guess))
        elif guess < number and guess > number - 50:
            print("You're close ! only 50 difference higher between", (guess))
        elif guess > number:
            print("You're way off, guess lower than" , (guess))
        elif guess < number:
            print("You're way off, guess higher than" , (guess))

clearScreen(1)
print_slow ('Checken your total score...')
time.sleep(1)
clearScreen(2)
print ("Loading ⏳ ...")
clearScreen(2)
print("Loading ⏳ ..")
clearScreen(2)
print("Loading ⏳ .")
clearScreen(2)
print('▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ \n')
print ("You total points are:", (kans_2) ) 
print('\n') 
print('Thanks for playing. Want to play again ? \n')
print('▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ \n')

