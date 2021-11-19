from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:
# move = 8
# for grab in range(move):
#     robotArm.grab()
#     robotArm.moveRight()
#     robotArm.drop()
#     for left in range(8):
#         robotArm.moveLeft()
# for move2 in range(move):
#     robotArm.moveRight
#     move += 1

move = 1
base = True

for base in range(9):
    robotArm.grab()
    color = robotArm.scan()
    if color != "":
        for position_right in range(move):
            robotArm.moveRight()
        move += 1
        robotArm.drop()
        for position_left in range(move):
            robotArm.moveLeft()
            
        
    else:
        move,position_right,position_left,base = False

    



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()