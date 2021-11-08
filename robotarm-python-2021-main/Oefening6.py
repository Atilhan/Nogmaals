from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')

# Jouw python instructies zet je vanaf hier:
for a in range (10):
    robotArm.moveRight()

for a in range(1,9):
    robotArm.moveLeft()
    robotArm.moveLeft()
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()