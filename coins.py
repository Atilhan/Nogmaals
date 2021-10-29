# name of student: Atilhan Kara
# number of student: 99024233
# purpose of program: 
# function of program:
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) #Variable ToPay is asking within a input what amount you have to pay.
paid = int(float(input('Paid amount: ')) * 100) #Variable paid is asking within a input the amount you've paid.
change = paid - toPay #Variable change is telling us that it's towards the variable paid & subtract variable toPay from it (paid - toPay)

coin500 = 0
coin300 = 0
coin200 = 0
coin100 = 0
coin50 = 0
coin20 = 0
coin10 = 0
coin5 = 0
coin2 = 0
coin1 = 0


if change > 0: #if variable "change" is greater than 0
  coinValue = 500 #This variable has been given the value 500
  
  while change > 0 and coinValue > 0: #While the variable change & coinValue are greater than 0
    nrCoins = change // coinValue #

    if nrCoins > 0: #If the variable nrCoins is greater than 0
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #Printing the string 'return maximal' and adding to that the value of nrcoins & CoinValue.
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #This line of code is requesting how many coins you've returned by looking at CoinValue + the input you inserted
      change -= nrCoinsReturned * coinValue # nrCoinsReturned will be multiplied with coinValue & the answer will be cut off from variable change.

# comment on code below: Value's between 500 to 1 have been added, also variables of Coin500 until 1 have been added to mention
# the value each variable gets and so I can mention the values of the variables in a print
    if coinValue == 500:
      coinValue = 300
      coin500 = nrCoinsReturned
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
      coin2 = nrCoinsReturned
      coinValue = 2
    elif coinValue == 2:
      coin1 = nrCoinsReturned
      coinValue = 1
    else:
      coinValue = 0

if change > 0: #If change is greater than 0 , then it will be printed the following str + the int of change to str 
  print('Change not returned: ', str(change) + ' cents')
else:
  if coin500 > 0:
    print (coin500)
  if coin300 > 0:
    print (coin300)
  if coin200 > 0:
    print (coin200)
  if coin100 > 0:
    print (coin100)
  if coin50 > 0:
    print (coin50)
  if coin20 > 0:
    print (coin20)
  if coin10 > 0:
    print (coin10)
  if coin5 > 0:
    print (coin5)
  if coin2 > 0:
    print (coin2)
  if coin1 > 0:
    print (coin1)
print('done')
#-----------------------------------------------------------------------------------------------------------------