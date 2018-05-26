#Written by: Owen Jeffreys

import pythonbytes


def init():
    HideMouse()
    
    SetStage('stages/maze.gif')
    ResizeStage(560,500)
    
    global ball
    ball = Sprite('sprites/ball.png')
    ball.Resize(16,16)
    ball.SetLocation(36,460)



def when_LEFT_key_held():
    ball.MoveLeft(2)
    if ball.TouchingColour(Black):
        ball.MoveRight(2)

def when_RIGHT_key_held():
    ball.MoveRight(2)
    if ball.TouchingColour(Black):
        ball.MoveLeft(2)

def when_UP_key_held():
    ball.MoveUp(2)
    if ball.TouchingColour(Black):
        ball.MoveDown(2)

def when_DOWN_key_held():
    ball.MoveDown(2)
    if ball.TouchingColour(Black):
        ball.MoveUp(2)



def when_SPACE_key_pressed():   #toggle fullscreen
    if IsFullScreen():
        Windowed()
    else:
        FullScreen()


def when_ENTER_key_pressed():   #restart the game
    findWall()
