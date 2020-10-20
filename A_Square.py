'''
Animation: Square
Category: Active 
This animation was created by Lilian Chan of the Oregon State University Share Lab
'''

import cozmo
import time
from cozmo.util import degrees, distance_mm, speed_mmps

def cozmo_program(robot: cozmo.robot.Robot):
    time.sleep(2)

    for x in range(0,4): #goes in a square
        robot.turn_in_place(degrees(90)).wait_for_completed()
        robot.drive_straight(distance_mm(120), speed_mmps(200)).wait_for_completed()
        
cozmo.run_program(cozmo_program)