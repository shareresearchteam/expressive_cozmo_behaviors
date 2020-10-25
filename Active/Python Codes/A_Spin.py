'''
Animation: Spin
Category: Active 
This animation was created by Lilian Chan of the Oregon State University Share Lab
'''

import cozmo
import time
from cozmo.util import degrees, distance_mm, speed_mmps


def cozmo_program(robot: cozmo.robot.Robot):
    time.sleep(2)

    robot.drive_wheels(-1000, 1000, l_wheel_acc=999, r_wheel_acc=999, duration=5) #spins
    time.sleep(1)
    robot.drive_wheels(1000, -1000, l_wheel_acc=999, r_wheel_acc=999, duration=5)

cozmo.run_program(cozmo_program)