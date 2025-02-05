import pgzrun
import random
WIDTH=500
HEIGHT=500

def draw():
    w=500
    h=150
    screen.fill("black")
    for i in range(100):
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        z=Rect((0,175),(w,h))
        z.center=(250,250)
        screen.draw.filled_rect(z,(r,g,b))
        w=w-10
        h=h+10
    screen.draw.text("wassssssuuup",(195,250),color="#99FFFF")
pgzrun.go()