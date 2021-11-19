from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')
# Jouw python instructies zet je vanaf hier:


# for a in range(8):
#     robotArm.moveRight()
# for b in range(20):
#     robotArm.grab()
#     color = robotArm.scan()
#     if color == "red":
#         for c in range(8):
#             robotArm.moveRight()
#         robotArm.drop()
#         robotArm.moveLeft()
#     else:
#         robotArm.drop()
#         robotArm.moveLeft()

for a in range (9):
    robotArm.grab()
    color = robotArm.scan()
    if color == "red":
        for b in range(9-a):
            robotArm.moveRight()
        robotArm.drop()
        for c in range(9-a):
            robotArm.moveLeft()
    else:
        robotArm.drop()
    robotArm.moveRight()


    




# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()