from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')

# Jouw python instructies zet je vanaf hier:
# for x in range(9):
#     robotArm.moveRight()
# for y in range(12):
#     robotArm.grab()
#     color = robotArm.scan()
#     if color == 'white':
#         robotArm.grab()
#         robotArm.moveRight()
#         robotArm.drop()
#         robotArm.moveLeft()
#     else:
#         robotArm.drop()
#         robotArm.moveLeft()





for a in range(9):
    robotArm.moveRight()
for b in range(15):
    robotArm.grab()
    color = robotArm.scan()
    if color == "white":
        robotArm.grab()
        print(color)
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()