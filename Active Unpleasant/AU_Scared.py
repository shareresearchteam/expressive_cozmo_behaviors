'''
Animation: Scared
Category: Active Unpleasant
This animation was created by Lilian Chan of the Oregon State University Share Lab
'''

import cozmo
import time
from cozmo.util import degrees, distance_mm, speed_mmps


def cozmo_program(robot: cozmo.robot.Robot):
   time.sleep(2)

   robot.drive_straight(distance_mm(120), speed_mmps(50)).wait_for_completed() #go forward
   robot.move_head(100) #look up
   time.sleep(1)
   robot.play_anim_trigger(cozmo.anim.Triggers.Shiver).wait_for_completed() #shiver animation
   robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabScaredCozmo).wait_for_completed() #scared 
   robot.drive_straight(distance_mm(-120), speed_mmps(999)).wait_for_completed()
   robot.play_anim_trigger(cozmo.anim.Triggers.Shiver).wait_for_completed()   
   robot.play_anim_trigger(cozmo.anim.Triggers.Shiver).wait_for_completed()
   robot.play_anim_trigger(cozmo.anim.Triggers.Shiver).wait_for_completed()   

cozmo.run_program(cozmo_program)