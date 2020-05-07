from cs1robots import *

#################################################
############## DO NOT MODIFY ABOVE ##############
#################################################

## Do not call 'detour_obstacle' function in this section.
## Instead, modifly the variable below to test your code.
city_name_to_load = 'detour.wld'

def turn_right(hubo):
    for i in range(3):
        hubo.turn_left()


def detour_obstacle(hubo):
    while hubo.front_is_clear():
        hubo.move()
    turn_right(hubo)
    m = 0
    while not hubo.left_is_clear():
        m = m + 1
        hubo.move()
        if not hubo.front_is_clear() and not hubo.left_is_clear():
            turn_right(hubo)
            turn_right(hubo)
            for i in range(m):
                hubo.move()
            m = 0
            while not hubo.right_is_clear():
                m = m + 1
                hubo.move()
            turn_right(hubo)
            hubo.move()
            turn_right(hubo)
            for i in range(m):
                hubo.move()
            hubo.turn_left()

            return (int(1))
    hubo.turn_left()
    hubo.move()
    hubo.turn_left()
    if not hubo.front_is_clear():
        hubo.turn_left()
        hubo.move()
        turn_right(hubo)
        for i in range(m):
            hubo.move()
        m = 0
        while not hubo.right_is_clear():
            m = m + 1
            hubo.move()
        turn_right(hubo)
        hubo.move()
        turn_right(hubo)
        if not hubo.front_is_clear():
            hubo.turn_left()
            n = 1
            while not hubo.right_is_clear():
                n = n + 1
                hubo.move()
            turn_right(hubo)
            for i in range(m):
                hubo.move()
            hubo.turn_left()
            return (n)

        for i in range(m):
            hubo.move()
        hubo.turn_left()
        return (int(1))

    for i in range(m):
        hubo.move()
    turn_right(hubo)
    return (int(1))

    pass


#################################################
############## DO NOT MODIFY BELOW ##############
#################################################

create_world()
edit_world()
save_world('detour.wld')
hubo = Robot(orientation='N', avenue=5, street=2)
hubo.set_trace('blue');
if __name__ == "__main__":
    detour_obstacle(hubo)
