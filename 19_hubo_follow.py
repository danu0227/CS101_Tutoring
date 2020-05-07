from cs1robots import *
import time

create_world()

hubo1 = Robot("yellow", 'E', 100, 2, 1)
hubo2 = Robot("blue", 'E', 0, 1, 1)
hubo1.move()
hubo1.move()
while hubo1.carries_beepers():
    time.sleep(0.5)
    if hubo1.front_is_clear():
        hubo1.drop_beeper()
        hubo1.move()
    else:
        hubo1.turn_left()
        hubo1.drop_beeper()
        hubo1.move()
    if hubo2.front_is_clear():
        if hubo2.on_beeper():
            hubo2.pick_beeper()
        hubo2.move()
    else:
        hubo2.turn_left()
        if hubo2.on_beeper():
            hubo2.pick_beeper()
        hubo2.move()
