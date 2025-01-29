import pgzrun

WIDTH =500
HEIGHT =400
def draw():
    screen.fill("blue")
    r=Rect((0,0),(50,70))
    screen.draw.rect(r,"yellow")
    b=Rect((430,355),(70,50))
    screen.draw.filled_rect(b,"green")

pgzrun.go()

