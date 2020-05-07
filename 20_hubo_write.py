from cs1robots import *
import time
import random
width = random.randrange(5, 10)
height = int(width*1.5//2*2+1)

create_world(width, height)

hubo = Robot("blue", 'E', 100, 1, 1)

def turn_right():
    for i in range(3):
        hubo.turn_left()

def turn_back():
    hubo.turn_left()
    hubo.turn_left()

def move():
    hubo.move()
    time.sleep(0.07)

def draw_line():
    a = 0
    while hubo.front_is_clear():
        move()
        if not hubo.on_beeper():
            hubo.drop_beeper()
        a += 1
    return a

def erase_line():
    while hubo.front_is_clear():
        move()
        if hubo.on_beeper():
            hubo.pick_beeper()

def draw_H():
    hubo.drop_beeper()
    hubo.turn_left()
    h = draw_line()

    turn_back()
    for i in range(h//2):
        move()
    hubo.turn_left()
    draw_line()

    hubo.turn_left()
    for i in range(h//2):
        move()

    turn_back()
    hubo.drop_beeper()
    draw_line()


def draw_E():
    hubo.drop_beeper()
    hubo.turn_left()
    h = draw_line()
    turn_right()
    draw_line()

    turn_back()
    while hubo.front_is_clear():
        move()
    hubo.turn_left()
    for i in range(h//2):
        move()
    hubo.turn_left()
    draw_line()

    turn_back()
    while hubo.front_is_clear():
        move()

    hubo.turn_left()
    while hubo.front_is_clear():
        move()

    hubo.turn_left()
    draw_line()

def draw_L():
    hubo.drop_beeper()
    hubo.turn_left()
    draw_line()

    turn_back()
    while hubo.front_is_clear():
        move()

    hubo.turn_left()
    draw_line()


def draw_O():
    hubo.drop_beeper()
    draw_line()

    for i in range(3):
        hubo.turn_left()
        draw_line()

def pick_beeper():
    if hubo.on_beeper():
        hubo.pick_beeper()

def erase():
    while not hubo.facing_north():
        hubo.turn_left()
    turn_back()
    while hubo.front_is_clear():
        move()
    turn_right()
    while hubo.front_is_clear():
        move()
    turn_back()
    while True:
        while hubo.front_is_clear():
            pick_beeper()
            move()
        hubo.turn_left()
        pick_beeper()
        if hubo.front_is_clear():
            move()
        else:
            break

        hubo.turn_left()
        while hubo.front_is_clear():
            pick_beeper()
            move()
        turn_right()
        pick_beeper()
        if hubo.front_is_clear():
            move()
        else:
            break

        turn_right()
        while hubo.front_is_clear():
            pick_beeper()
            move()
        hubo.turn_left()
        pick_beeper()
        if hubo.front_is_clear():
            move()
        else:
            break

        hubo.turn_left()
        while hubo.front_is_clear():
            pick_beeper()
            move()
        turn_right()
        pick_beeper()
        if hubo.front_is_clear():
            move()
        else:
            break
        turn_right()

    while not hubo.facing_north():
        hubo.turn_left()
    turn_back()
    while hubo.front_is_clear():
        move()
    turn_right()
    while hubo.front_is_clear():
        move()
    turn_back()


draw_H()
time.sleep(0.3)
erase()

draw_E()
time.sleep(0.3)
erase()

draw_L()
time.sleep(0.3)
erase()

draw_L()
time.sleep(0.3)
erase()

draw_O()
time.sleep(0.3)
erase()


