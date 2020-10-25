'''
Animation: Contemplating 
Category: Inactive Pleasant
This animation was created by Lilian Chan of the Oregon State University Share Lab
'''

import cozmo
import time
from cozmo.util import degrees, distance_mm, speed_mmps

def cozmo_program(robot: cozmo.robot.Robot):
    time.sleep(2)
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabThinking).wait_for_completed() #think
    time.sleep(2)  
    robot.play_anim_trigger(cozmo.anim.Triggers.VC_Alrighty).wait_for_completed() #happy
    
cozmo.run_program(cozmo_program)
