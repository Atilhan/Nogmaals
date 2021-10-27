# name of student: Atilhan Kara
# number of student: 99024233
# purpose of program: 
# function of program:
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) #Variable ToPay is asking within a input what amount you have to pay.
paid = int(float(input('Paid amount: ')) * 100) #Variable paid is asking within a input the amount you've paid.
change = paid - toPay #Variable change is telling us that it's towards the variable paid & subtract variable toPay from it (paid - toPay)

if change > 0: # if variable "change" is greater than 0
  coinValue = 500 # This variable has been given the value 500
  
  while change > 0 and coinValue > 0: #While the variable change & coinValue are greater than 0
    nrCoins = change // coinValue #Variable nrCoins is directing / telling us that variable change & coinValue has to be divided by // into whole numbers instead of a float

    if nrCoins > 0: #If the variable nrCoins is greater than 0
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #Printing the string 'return maximal' and adding to that the value of nrcoins & CoinValue.
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #This line of code is requesting how many coins you've returned by looking at CoinValue + the input you inserted 
      change -= nrCoinsReturned * coinValue #

# comment on code below: 
#i've added varriables of multiple coin options of 500 down to 1 
    if coinValue == 500:
      coin500 = nrCoinsReturned
      coinValue == 300
    elif coinValue == 300:
      coin300 = nrCoinsReturned
      coinValue = 200
    elif coinValue == 200:
      coin200 = nrCoinsReturned
      coinValue = 100
    elif coinValue == 100:
      coin100 = nrCoinsReturned
      coinValue = 50
    elif coinValue == 50:
      coin50 = nrCoinsReturned
      coinValue = 20
    elif coinValue == 20:
      coin20 = nrCoinsReturned
      coinValue = 10
    elif coinValue == 10:
      coin10 = nrCoinsReturned
      coinValue = 5
    elif coinValue == 5:
      coin5 = nrCoinsReturned
      coinValue = 2
    elif coinValue == 2:
      coin2 = nrCoinsReturned
      coinValue = 1
    elif coinValue == 1:
      coin1 = nrCoinsReturned
    else:
      coinValue = 0

if change > 0: # if the variable change is greater than 0, it has to print the amount of change not returned else it will print that you're  done & how much you returned (coins)

  print('Change not returned: ', str(change) + ' cents')
else:

  print("You're done. You've returned: ", str(nrCoins) + ' coin(s)')

#-----------------------------------------------------------------------------------------------------------------
