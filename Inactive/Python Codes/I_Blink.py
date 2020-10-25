'''
Animation: Blink
Category: Inactive
This animation was created by Lilian Chan of the Oregon State University Share Lab
'''

import cozmo
import time
from cozmo.util import degrees, distance_mm, speed_mmps

def cozmo_program(robot: cozmo.robot.Robot):
    time.sleep(2)

    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabBlink).wait_for_completed() #blink
    time.sleep(3.5)
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabBlink).wait_for_completed()
    time.sleep(3.5)
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabBlink).wait_for_completed()
    time.sleep(3.5)
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabBlink).wait_for_completed()

cozmo.run_program(cozmo_program)