import pythonbytes

time = 0

def init():
    SetStage('world-map-continents.jpg')
    HideMouse()
    SetFPS(10)

    global destination
    destination = Text('Destination: DISNEYLAND', colour=White, size=35, centre=True)

    global timeText
    timeText = Text('TIME', colour=Red, y=370, centre=Yes)
    
    global myPlane
    myPlane = Sprite('ship.png')
    myPlane.Shrink(20)
    myPlane.SetLocation(420,80)
    #myPlane.FlipVertical()
    myPlane.Direction = Left


def loop():
    global time

    #if the plane has not arrived at DisneyLand
    if myPlane.Direction == Left and myPlane.x > 210:
        myPlane.MoveLeft(3)
        myPlane.MoveDown(1)

        time = time + 1
        timeText.SetText(time/10)
        timeText.AppendText(' seconds')
    else:
        if myPlane.Direction == Left:
            myPlane.Direction = Right
            myPlane.FlipVertical()
            Sprite('mickey.png').SetLocation(50,350)
            destination.SetText('Destination: HOME')
            

    if myPlane.Direction == Right and myPlane.x < 420:
        myPlane.MoveRight(3)
        myPlane.MoveUp(1)

        time = time - 1
        timeText.SetText(time/10)
        timeText.AppendText(' seconds')



def when_SPACE_key_pressed():
    ToggleFullScreen()
