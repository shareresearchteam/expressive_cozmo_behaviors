'''
Animation: Happy  
Category: Pleasant
This animation was created by Lilian Chan of the Oregon State University Share Lab
'''

import cozmo
import time
from cozmo.util import degrees, distance_mm, speed_mmps

def cozmo_program(robot: cozmo.robot.Robot):
    time.sleep(2)
    robot.play_anim_trigger(cozmo.anim.Triggers.SoftSparkUpgradeLift).wait_for_completed() #softsparkupgradelift sdk animation
    robot.move_head(5) #look up
    robot.play_anim_trigger(cozmo.anim.Triggers.ComeHere_AlreadyHere).wait_for_completed() #alreadyhere sdk animation
    time.sleep(1)

cozmo.run_program(cozmo_program)