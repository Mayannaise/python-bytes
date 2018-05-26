#Written by: Owen Jeffreys

import pythonbytes


def init():
    SetFPS(200)
    HideMouse()
    
    SetStage('maze.gif')
    
    global ball
    ball = Sprite('ball.png')
    ball.Resize(16,16)
    ball.SetLocation(48,620)

    #locate right-hand wall to follow
    ball.Direction = Right
    while (not ball.TouchingColour(Black, Right)):
        ball.MoveSteps(1)



def loop():
    #choose direction depending on which side has contact
    if ball.TouchingColour(Black, Right) and ball.TouchingColour(Black, Bottom):
        ball.Direction = Up
    elif ball.TouchingColour(Black, Top) and ball.TouchingColour(Black, Right):
        ball.Direction = Left
    elif ball.TouchingColour(Black, Bottom) and ball.TouchingColour(Black, Left):
        ball.Direction = Right
    elif ball.TouchingColour(Black, Left) and ball.TouchingColour(Black, Top):
        ball.Direction = Down
        
    elif ball.TouchingColour(Black, Right):
        ball.Direction = Up
    elif ball.TouchingColour(Black, Top):
        ball.Direction = Left
    elif ball.TouchingColour(Black, Left):
        ball.Direction = Down
    elif ball.TouchingColour(Black, Bottom):
        ball.Direction = Right
        
    else:       #not touching any border colour
        ball.TurnRight()    


    if not ball.TouchingColour(Red):    #found the end
        ball.MoveSteps(1)

