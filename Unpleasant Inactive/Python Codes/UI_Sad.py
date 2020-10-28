'''
Animation: Sad
Category: Unpleasant Inactive
This animation was created by Lilian Chan of the Oregon State University Share Lab
'''

import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps
import time
import math

def cozmo_program(robot: cozmo.robot.Robot):
    time.sleep(2)

    robot.move_lift(-5)
    robot.move_head(-5)
    time.sleep(5)
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabSquint1).wait_for_completed() #squint
    robot.play_anim_trigger(cozmo.anim.Triggers.FeedingInterrupted_Severe).wait_for_completed() #sad
    time.sleep(5)

cozmo.run_program(cozmo_program)
