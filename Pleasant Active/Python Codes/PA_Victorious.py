'''
Animation: Victorious
Category: Pleasant Active
This animation was created by Lilian Chan of the Oregon State University Share Lab
NOTE: Start this animation with Cozmo on its rear end
'''

import cozmo
import time
from cozmo.util import degrees, distance_mm, speed_mmps

def cozmo_program(robot: cozmo.robot.Robot):
    time.sleep(2)
    robot.play_anim_trigger(cozmo.anim.Triggers.FacePlantRollArmUp).wait_for_completed() #tries to get up, fails
    robot.play_anim_trigger(cozmo.anim.Triggers.FacePlantRollArmUp).wait_for_completed()    
    robot.drive_wheels(-1000, 1000, l_wheel_acc=250, r_wheel_acc=250, duration=2) #spin
    robot.set_lift_height(1.0, accel=100.0, max_speed=100.0).wait_for_completed() #slam lift
    robot.set_lift_height(0.0, accel=100.0, max_speed=100.0).wait_for_completed() 
    robot.drive_wheels(-200, -200, l_wheel_acc=9999, r_wheel_acc=9999, duration=0.5) #sucessfully gets up
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabCelebrate).wait_for_completed() #celebrate

cozmo.run_program(cozmo_program)