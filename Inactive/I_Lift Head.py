'''
Animation: Lift Head
Category: Inactive
This animation was created by Lilian Chan of the Oregon State University Share Lab
'''

import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps
import time
import math

def cozmo_program(robot: cozmo.robot.Robot):
   time.sleep(1)
   robot.move_head(.5) #lift
   time.sleep(5)

cozmo.run_program(cozmo_program)