'''
Animation: Sad
Category: Unpleasant
This animation was created by Lilian Chan of the Oregon State University Share Lab
'''

import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps
import time
import math

def cozmo_program(robot: cozmo.robot.Robot):
   time.sleep(2)

   robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabUnhappy).wait_for_completed() #sad
   time.sleep(.5)
   robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabDejected).wait_for_completed() #sad
   time.sleep(2)

cozmo.run_program(cozmo_program)
