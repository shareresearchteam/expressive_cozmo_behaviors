'''
Animation: Pleased 2
Category: Pleasant
This animation was created by Lilian Chan of the Oregon State University Share Lab
'''

import cozmo
import time
from cozmo.util import degrees, distance_mm, speed_mmps


def cozmo_program(robot: cozmo.robot.Robot):
    time.sleep(2)
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabYes).wait_for_completed() #agree
    for x in range(0,2): #nod
        robot.move_head(3)
        time.sleep(.6)
        robot.move_head(-3)
        time.sleep(.6)
    robot.move_head(3)
    time.sleep(1)
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabHappy).wait_for_completed() #happy

cozmo.run_program(cozmo_program)
