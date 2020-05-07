from cs1robots import *
import random

width = 10
height = 10
n = 20
# create_world(width, height)
# edit_world()
# save_world()
#
# load_world()
#
file_name = input("file name: ")
f = open("./venv/Lib/worlds/"+file_name+".wld", 'w')
f.write("avenues = %d \n"%width)
f.write("streets = %d \n"%height)
f.write("walls = [] \n")
f.write("beepers = { \n")

for i in range(n-1):
    a = random.randrange(1, width)
    b = random.randrange(1, height)
    c = random.randrange(1, 10)
    f.write("    (%d, %d): %d, \n"%(a, b, c))

a = random.randrange(0, width)
b = random.randrange(0, height)
c = random.randrange(1, 10)
f.write("    (%d, %d): %d\n}"%(a, b, c))
f.close()

load_world("./venv/Lib/worlds/"+file_name+".wld")