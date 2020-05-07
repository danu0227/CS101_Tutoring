from cs1robots import *
import random


def load_random_world(width, height):
    file_name = "tutor2"
    f = open("./venv/Lib/worlds/" + file_name + ".wld", 'w')
    f.write("avenues = %d \n" % width)
    f.write("streets = %d \n" % height)
    f.write("walls = [] \n")
    f.write("beepers = { \n")
    n = random.randrange(10, 20)
    for i in range(n - 1):
        a = random.randrange(1, width)
        b = random.randrange(1, height)
        c = random.randrange(1, 10)
        f.write("    (%d, %d): %d, \n" % (a, b, c))

    a = random.randrange(1, width)
    b = random.randrange(1, height)
    c = random.randrange(1, 10)
    f.write("    (%d, %d): %d\n}" % (a, b, c))
    f.close()

    load_world("./venv/Lib/worlds/" + file_name + ".wld")


def turn_right():
    for i in range(3):
        hubo.turn_left()


def turn_back():
    hubo.turn_left()
    hubo.turn_left()


def one_line(start_beeper):
    n_beep = start_beeper
    n = n_beep
    while n_beep > 0 :
        hubo.drop_beeper()
        n_beep -=1
    n_beep = start_beeper
    while hubo.front_is_clear():
        hubo.move()
        n_beep += start_beeper
        n = n_beep
        while n > 0:
            hubo.drop_beeper()
            n -= 1
    return start_beeper + 1


def come_back_and_go_up():
    turn_back()
    while hubo.front_is_clear():
        hubo.move()
    turn_right()
    hubo.move()
    turn_right()


if __name__ == "__main__":
    width = random.randrange(3, 10)
    height = random.randrange(3, 10)
    random_world = False
    if random_world:
        load_random_world(width, height)
    else:
        create_world(width, height)

    hubo = Robot("blue", 'E', width * (width + 1) * height * (height + 1) / 4, 1, 1)
    hubo.set_pause(0.05)
    n_beep = 1

    while True:
        n_beep = one_line(n_beep)
        if hubo.left_is_clear():
            come_back_and_go_up()
        else:
            break
