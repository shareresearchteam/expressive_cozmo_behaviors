'''
Animation: Race
Category: Active 
This animation was created by Lilian Chan of the Oregon State University Share Lab
'''

import cozmo
import time
from cozmo.util import degrees, distance_mm, speed_mmps


def cozmo_program(robot: cozmo.robot.Robot):
    time.sleep(2)

    robot.drive_straight(distance_mm(145), speed_mmps(999)).wait_for_completed() #drive forward and back
    robot.drive_straight(distance_mm(-145), speed_mmps(999)).wait_for_completed()
    robot.drive_straight(distance_mm(145), speed_mmps(999)).wait_for_completed()
    robot.drive_straight(distance_mm(-145), speed_mmps(999)).wait_for_completed()
    robot.drive_straight(distance_mm(145), speed_mmps(999)).wait_for_completed()
    robot.drive_straight(distance_mm(-145), speed_mmps(999)).wait_for_completed()    

cozmo.run_program(cozmo_program)