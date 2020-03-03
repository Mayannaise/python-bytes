#Written by: Owen Jeffreys

import pythonbytes

time = 0
alarm = 10


def init():
    global myText, alarm
    myText = Text(font='Tahoma', size=100, y=(SCREEN_HEIGHT/2)-70, colour=White, centre=True)
    
    Text(Day(), 'Tahoma', size=40, y=50, colour=Blue, centre=True)
    Text(Date(), 'Tahoma', size=20, y=270, colour=Blue, centre=True)

    
def loop():
    global time, myText
    time+=1

    scaledTime = time / 20      #scale down from FPS
    
    hours = int(scaledTime / 3600)
    minutes = (scaledTime % 3600) / 60
    seconds = (scaledTime % 3600) % 60

    myText.SetText(str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2))

    if scaledTime == alarm: myText.SetColour(Red)    
    
