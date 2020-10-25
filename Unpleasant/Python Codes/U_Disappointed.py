'''
Animation: Disappointed
Category: Unpleasant
This animation was created by Lilian Chan of the Oregon State University Share Lab
'''

import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps
import time
import math

def cozmo_program(robot: cozmo.robot.Robot):
    time.sleep(2)

    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabStaring).wait_for_completed() #angry stare
    robot.move_lift(1) #move lift up
    time.sleep(2) 
    robot.move_lift(-100) #slam down quickly
    time.sleep(1)
    robot.move_head(3)
    time.sleep(2)
    robot.move_lift(0.25) 
    time.sleep(2) 
    robot.move_lift(-100)

    time.sleep(1)

cozmo.run_program(cozmo_program)
