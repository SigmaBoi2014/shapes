import pgzrun

WIDTH =500
HEIGHT =400
def draw():
    screen.fill("blue")
    r=Rect((0,0),(50,60))
    screen.draw.rect(r,"red")
    b=Rect((250,200),(60,50))
    b.center=250,200
    screen.draw.filled_rect(b,"yellow")
    screen.draw.filled_circle((450,350),45,"orange")
pgzrun.go()
