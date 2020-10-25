'''
Animation: Angry_2
Category: Active Unpleasant
This animation was created by Lilian Chan of the Oregon State University Share Lab
'''

import cozmo
import time
from cozmo.util import degrees, distance_mm, speed_mmps

def cozmo_program(robot: cozmo.robot.Robot):
    time.sleep(2)

    robot.move_head(-50) #look down
    for x in range(0,1):
        robot.move_lift(50) #slam lift
        time.sleep(1)
        robot.move_lift(-50)
        time.sleep(1)
    robot.move_head(50) #look up
    robot.play_anim_trigger(cozmo.anim.Triggers.GuardDogBusted).wait_for_completed() #frustrated

cozmo.run_program(cozmo_program)
