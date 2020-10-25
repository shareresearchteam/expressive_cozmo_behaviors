'''
Animation: Looking
Category: Inactive
This animation was created by Lilian Chan of the Oregon State University Share Lab
'''

import cozmo
import time
from cozmo.util import degrees, distance_mm, speed_mmps

def cozmo_program(robot: cozmo.robot.Robot):
    time.sleep(2)

    robot.move_head(.5) #look up and down slowly
    time.sleep(3)
    robot.move_head(-.5)
    time.sleep(6)
    robot.move_head(.5)
    time.sleep(4)
cozmo.run_program(cozmo_program)