
from pygame import *

back = (200,255,255)
win_whith = 600
win_height = 500
window = display.set_mode((win_whith,win_height))

window.fill(back)

clock = time.Clock()
fps = 60
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False 

    display.update()
    clock.tick(fps)