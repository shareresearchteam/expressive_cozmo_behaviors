'''
Animation: Twitch
Category: Active 
This animation was created by Lilian Chan of the Oregon State University Share Lab
'''

import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps
import time
import math

def attention_one(robot: cozmo.robot.Robot):
    time.sleep(2)

    for x in range(0,2): #go side to side
        robot.drive_wheels(100, -100, l_wheel_acc=999, r_wheel_acc=999, duration=0.3)
        robot.drive_wheels(-100, 100, l_wheel_acc=999, r_wheel_acc=999, duration=0.6)
        robot.drive_wheels(100, -100, l_wheel_acc=999, r_wheel_acc=999, duration=0.3)
        robot.turn_in_place(degrees(180)).wait_for_completed()
   
        robot.drive_wheels(100, -100, l_wheel_acc=999, r_wheel_acc=999, duration=0.3) #repeat after turning
        robot.drive_wheels(-100, 100, l_wheel_acc=999, r_wheel_acc=999, duration=0.6)
        robot.drive_wheels(100, -100, l_wheel_acc=999, r_wheel_acc=999, duration=0.3)
        robot.turn_in_place(degrees(180)).wait_for_completed()

cozmo.run_program(attention_one)
