
# import time
# while True:
#     from datetime import datetime
#     now = datetime.now()  
#     print (now.month,now.day,now.year,now.hour,now.minute,now.second)
#     time.sleep(1)

#boven is een digital time 
#------------------------------------------------------------------#
#Onderste is mijn code

time_PM = 1
time_AM = 12

while time_PM <= 12:
    print (time_PM , 'PM')
    time_PM += 1

while time_AM <= 24:
    print (time_AM , 'AM')
    time_AM += 1

#------------------------------------------------------------------#