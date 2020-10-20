'''
Animation: Grossed Out
Category: Active Unpleasant
This animation was created by Lilian Chan of the Oregon State University Share Lab
'''

import cozmo
import time
from cozmo.util import degrees, distance_mm, speed_mmps


def cozmo_program(robot: cozmo.robot.Robot):
    time.sleep(2)

    robot.move_lift(50)
    robot.drive_straight(distance_mm(-50), speed_mmps(150)).wait_for_completed() #drive forward
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabVampire).wait_for_completed() #grossed out
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabSquint1).wait_for_completed() #squint
    robot.move_lift(-50) #put arms down
    robot.drive_wheels(-1000, 1000, l_wheel_acc=-250, r_wheel_acc=250, duration=1) #drive away
    time.sleep(.5)
    robot.drive_straight(distance_mm(200), speed_mmps(150)).wait_for_completed()



cozmo.run_program(cozmo_program)