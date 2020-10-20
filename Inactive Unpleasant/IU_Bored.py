'''
Animation: Bored
Category: Inactive Unpleasant
This animation was created by Lilian Chan of the Oregon State University Share Lab
'''

import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps
import time
import math

def bored_one(robot: cozmo.robot.Robot):
   time.sleep(2)

   robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabBored).wait_for_completed() #bored
   time.sleep(5)
   robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabSquint2).wait_for_completed() #squint
   time.sleep(5)

cozmo.run_program(bored_one)
