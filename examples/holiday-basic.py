#Written by: Owen Jeffreys

import pythonbytes

def init():
    SetStage('world-map-continents.jpg')
    SetFPS(10)

    global title
    title = Text('Destination: DISNEYLAND', colour=Yellow, size=35, centre=True)

    global myPlane
    myPlane = Sprite('fly.png').Shrink(20)
    myPlane.SetLocation(420,80)



def loop():
    if myPlane.x > 220 and myPlane.x <= 420:
        myPlane.MoveLeft(3)
        myPlane.MoveDown(1)
    else:
        title.SetText('ARRIVED!!')
        Sprite('mickey.png').SetLocation(50,350)
        EndLoop()
