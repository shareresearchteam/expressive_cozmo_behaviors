'''
Animation: Sleepy
Category: Inactive
This animation was created by Lilian Chan of the Oregon State University Share Lab
'''

import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps
import time

def cozmo_program(robot: cozmo.robot.Robot):
   time.sleep(2)

   robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabSleep).wait_for_completed() #sleeping sdk emotions
   robot.play_anim_trigger(cozmo.anim.Triggers.Sleeping).wait_for_completed()

cozmo.run_program(cozmo_program)