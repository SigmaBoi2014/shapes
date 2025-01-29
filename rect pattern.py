import pgzrun
WIDTH=500
HEIGHT=500

def draw():
    w=500
    h=150
    screen.fill("black")
    for i in range(35):
        b=Rect((0,175),(w,h))
        b.center=(250,250)
        screen.draw.rect(b,"white")
        w=w-10
        h=h+10
    screen.draw.text("wassssssuuup",(195,250),color="yellow")
pgzrun.go()
