'''
Animation: Grumpy
Category: Inactive Unpleasant
This animation was created by Lilian Chan of the Oregon State University Share Lab
'''

import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps
import time
import math

def cozmo_program(robot: cozmo.robot.Robot):
    time.sleep(2)

    robot.play_anim_trigger(cozmo.anim.Triggers.NothingToDoBoredIntro).wait_for_completed() #bored, grumpy
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabSquint2).wait_for_completed() #squint
    time.sleep(1)
    robot.move_head(.5)
    time.sleep(3)
    robot.move_head(-50)
    time.sleep(1)

cozmo.run_program(cozmo_program)
