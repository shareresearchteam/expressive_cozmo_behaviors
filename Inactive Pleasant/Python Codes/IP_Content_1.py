'''
Animation: Content 1
Category: Inactive Pleasant
This animation was created by Lilian Chan of the Oregon State University Share Lab
'''

import cozmo
import time
from cozmo.util import degrees, distance_mm, speed_mmps

def cozmo_program(robot: cozmo.robot.Robot):
    time.sleep(2)
    robot.move_head(10)
    time.sleep(2)    
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabTakaTaka).wait_for_completed() #chatty   
    time.sleep(4)
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabYes).wait_for_completed() #agree
    time.sleep(4)
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabYes).wait_for_completed()

cozmo.run_program(cozmo_program)