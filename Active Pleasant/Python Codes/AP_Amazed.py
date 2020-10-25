'''
Animation: Amazed
Category: Active Pleasant
This animation was created by Lilian Chan of the Oregon State University Share Lab
'''

import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps
import time
import math

def attention_one(robot: cozmo.robot.Robot):
    time.sleep(2)
    robot.move_head(10)
    robot.turn_in_place(degrees(10)).wait_for_completed() #turn one side
    robot.play_anim_trigger(cozmo.anim.Triggers.PopAWheelieInitial).wait_for_completed() #happy
    robot.turn_in_place(degrees(-20)).wait_for_completed() #turn another
    robot.play_anim_trigger(cozmo.anim.Triggers.PopAWheelieInitial).wait_for_completed() 
    robot.turn_in_place(degrees(10)).wait_for_completed() #back to middle
    robot.play_anim_trigger(cozmo.anim.Triggers.SuccessfulWheelie).wait_for_completed() #excited

cozmo.run_program(attention_one)
