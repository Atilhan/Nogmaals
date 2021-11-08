from RobotArm import RobotArm

robotArm = RobotArm('exercise 2')

# Jouw python instructies zet je vanaf hier:
robotArm.grab()

for a in range (1,10):
    robotArm.moveRight()

robotArm.drop()

for a in range (5,10):
    robotArm.moveLeft()

robotArm.grab()

for a in range (5,10):
    robotArm.moveRight()

robotArm.drop()

for a in range (8,10):
    robotArm.moveLeft()

robotArm.grab()
for a in range (8,10):
    robotArm.moveRight()

robotArm.drop()

# voor dit opdracht heb ik rondom andere respositories gekeken welke de beste aanpak had, zelf hiervoor
# had ik het idee om een loop te gebruiken om de armen heen en weer te brengen, maar wou zekerheid
# rondkijken hoe andere het hadden gedaan en of het logischer kon gemaakt worden.
# De code hierboven kan ik controleren waar de armen heen moeten op een overzichtelijk en simpel manier.





# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()