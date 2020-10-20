'''
Animation: Impressed
Category: Pleasant
This animation was created by Lilian Chan of the Oregon State University Share Lab
'''

import cozmo
import time
from cozmo.util import degrees, distance_mm, speed_mmps

def cozmo_program(robot: cozmo.robot.Robot):
    time.sleep(2)
    robot.drive_straight(distance_mm(50), speed_mmps(50)).wait_for_completed() #go forward

    time.sleep(1) 
    for x in range(0,1): #lift head
        robot.move_head(1)

    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabAmazed).wait_for_completed() #amazed

cozmo.run_program(cozmo_program)