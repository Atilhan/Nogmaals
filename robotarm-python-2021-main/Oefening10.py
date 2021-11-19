from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

# Jouw python instructies zet je vanaf hier:
step_9 = 9

for a in range (1,6):
    robotArm.grab()
    for b in range (step_9):
        robotArm.moveRight()
    step_9 -= 1
    robotArm.drop()
    for c in range(step_9):
        robotArm.moveLeft()
    step_9 -= 1

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()