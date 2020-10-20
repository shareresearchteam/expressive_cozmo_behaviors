'''
Animation: Attention
Category: Pleasant
This animation was created by Lilian Chan of the Oregon State University Share Lab
'''

import cozmo
import time
from cozmo.util import degrees, distance_mm, speed_mmps

def cozmo_program(robot: cozmo.robot.Robot):
    time.sleep(2) #go left and right
    robot.drive_wheels(100, -100, l_wheel_acc=999, r_wheel_acc=999, duration=0.3)
    robot.drive_wheels(-100, 100, l_wheel_acc=999, r_wheel_acc=999, duration=0.6)
    robot.drive_wheels(100, -100, l_wheel_acc=999, r_wheel_acc=999, duration=0.3)
    robot.move_head(1)
    time.sleep(1)
    robot.drive_wheels(100, -100, l_wheel_acc=999, r_wheel_acc=999, duration=0.3)
    robot.drive_wheels(-100, 100, l_wheel_acc=999, r_wheel_acc=999, duration=0.6)
    robot.drive_wheels(100, -100, l_wheel_acc=999, r_wheel_acc=999, duration=0.4)
    time.sleep(1)    
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabChatty).wait_for_completed() #chat
    robot.play_anim_trigger(cozmo.anim.Triggers.VC_Alrighty).wait_for_completed() #happy   
    time.sleep(2)    


cozmo.run_program(cozmo_program)