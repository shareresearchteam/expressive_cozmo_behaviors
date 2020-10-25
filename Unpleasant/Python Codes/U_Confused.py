'''
Animation: Confused
Category: Unpleasant
This animation was created by Lilian Chan of the Oregon State University Share Lab
'''

import cozmo
import time
from cozmo.util import degrees, distance_mm, speed_mmps

def cozmo_program(robot: cozmo.robot.Robot):
    time.sleep(2)

    robot.turn_in_place(degrees(30)).wait_for_completed() #turn one way
    time.sleep(2.5)
    robot.turn_in_place(degrees(-60)).wait_for_completed() #turn other way
    time.sleep(2.5)
    robot.turn_in_place(degrees(30)).wait_for_completed() #turn to middle
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabIDK).wait_for_completed() #confused

cozmo.run_program(cozmo_program)