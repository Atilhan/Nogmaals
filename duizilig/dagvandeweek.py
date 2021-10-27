request_day = input('Welke dag van de week wilt u opvragen ? kies met : ma , di , wo , do , vr , za , zo : ')

while request_day:

    if request_day == "ma":
        print ('Maandag')
    
    elif request_day == "di":
        print ("Maandag , Dinsdag")

    elif request_day == "wo":
        print ("Maandag , Dinsdag , Woensdag")

    elif request_day == "do":
        print ("Maandag , Dinsdag , Woensdag , Donderdag ")

    elif request_day == "vr":
        print ("Maandag , Dinsdag , Woensdag , Donderdag , Vrijdag ")

    elif request_day == "za":
        print ("Maandag , Dinsdag , Woensdag , Donderdag , Vrijdag , Zaterdag")

    elif request_day == "zo":
        print ("Maandag , Dinsdag , Woensdag , Donderdag ,Vrijdag , Zaterdag , Zondag")
    break

#Bovenste Code gemaakt op eigen ervaring en onderste als uitdagingscode.
#---------------------------------------------------------------------------------------------#
#formaat heeft gewerkt maar ik vind het lastig om te zien wat het precies doet

days = ['ma','di','wo','do','vr','za','zo']
vraag = input("Welke dag van de week kiest u? {} ".format(days))
current= 0

while current < days.index(vraag) + 1:
    print(days[current])
    current += 1


#format testing
#txt = "For only {price} dollars!"
# print(txt.format(price = 49))








