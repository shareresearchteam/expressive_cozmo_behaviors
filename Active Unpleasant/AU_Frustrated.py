'''
Animation: Frustrated
Category: Active Unpleasant
This animation was created by Lilian Chan of the Oregon State University Share Lab
'''

import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps
import time
import math

def cozmo_program(robot: cozmo.robot.Robot):
   time.sleep(2)
   robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabUnhappy).wait_for_completed() #show frustration
   robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabFrustrated).wait_for_completed()

   robot.move_head(-100) #look down

   robot.turn_in_place(degrees(180)).wait_for_completed() #turn 180 degrees

   robot.move_lift(100) #slam lift
   time.sleep(.23)
   robot.move_lift(-100)
   time.sleep(.25)
   robot.move_lift(100)
   time.sleep(.25)
   robot.move_lift(-100)
   time.sleep(.25)   
   robot.move_lift(100)
   time.sleep(.25)
   robot.move_lift(-100)
   time.sleep(.25)     
   robot.move_lift(100)
   time.sleep(.25)
   robot.move_lift(-100)
   time.sleep(.25)     
   robot.move_lift(100)
   time.sleep(.25)
   robot.move_lift(-100)
   time.sleep(.25) 

   
cozmo.run_program(cozmo_program)
