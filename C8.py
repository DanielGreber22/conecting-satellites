import pgzrun
from random import randint
from time import time

WIDTH = 800
HEIGHT = 600

satellites = []
lines = []
next_sat = 0
start_time = 0
total_time = 0
end_time = 0
number_of_sat = 20

def creat_sat():
    global start_time
    for i in range(0,number_of_sat):
        sat = Actor("sat")
        sat.pos = randint(40,WIDTH-40),randint(40,HEIGHT-40)
        satellites.append(sat)
    start_time = time()

def draw():
     global total_time
     screen.blit("night",(0,0))
     number = 1
     for sat in satellites:
         screen.draw.text(str(number),(sat.pos[0],sat.pos[1]+20))
         sat.draw()
         number += 1
     for line in lines:
         screen.draw.line(line[0],line[1],(255,225,225))
     if next_sat < number_of_sat:
         total_time = time() - start_time
         screen.draw.text(str(round(total_time,1)),(10,10),fontsize = 30)
     else:
         screen.draw.text(str(round(total_time,1)),(10,10),fontsize = 30)
def update():
    pass

def on_mouse_down(pos):
    global next_sat,lines

    if next_sat < number_of_sat:
        if satellites[next_sat].collidepoint(pos):
            if next_sat:
                lines.append((satellites[next_sat - 1].pos,satellites[next_sat].pos))
            next_sat = next_sat + 1 
        else:
            lines = []
            next_sat = 0
creat_sat()
pgzrun.go()
