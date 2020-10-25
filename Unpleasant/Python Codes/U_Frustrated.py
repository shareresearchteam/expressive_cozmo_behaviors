'''
Animation: Frustrated 
Category: Unpleasant
This animation was created by Lilian Chan of the Oregon State University Share Lab
'''

import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps
import math
import time


def cozmo_program(robot: cozmo.robot.Robot):
    time.sleep(2)

    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabStaring).wait_for_completed() #angry squint  
    robot.turn_in_place(degrees(180)).wait_for_completed() #turn
    robot.move_lift(100) #slam lift 
    robot.move_lift(-100)
    time.sleep(1)
    robot.move_lift(100)
    time.sleep(1)
    robot.move_lift(-100)
    time.sleep(1)

cozmo.run_program(cozmo_program)
