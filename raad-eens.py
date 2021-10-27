game = True

while game:
        from random import randint, randrange
        number = randint(1,1000)
        print (number)

        for x in range(10):
            guess = int (input('Guess a number between 1 & 1000 : '))

            if guess == number:
                print("You've guessed right !")
                break

            else:
                print('Try again !')







