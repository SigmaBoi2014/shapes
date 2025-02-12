import pgzrun
import random
WIDTH=500
HEIGHT=500

def draw():
    r1=180
    screen.fill("white")
    pgzrun.center=(250,250)
    for i in range(6):
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        screen.draw.filled_circle((250,250),(r1),(r,g,b))
        r1=r1-30
        pgzrun.center=(250,250)
pgzrun.go()