'''
Animation: Excited
Category: Active Pleasant
This animation was created by Lilian Chan of the Oregon State University Share Lab
'''

import cozmo
import time
from cozmo.util import degrees, distance_mm, speed_mmps

def cozmo_program(robot: cozmo.robot.Robot):
    time.sleep(2)
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabChatty).wait_for_completed() #chatty
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabDuck).wait_for_completed() #dance around 
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabChatty).wait_for_completed()

cozmo.run_program(cozmo_program)
