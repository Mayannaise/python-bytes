#Written by: Owen Jeffreys

import sys
sys.path.append('..')
import pythonbytes


#one-off function run at startup use to prepare the initial sprites
def init():

    #create the background image (stage)
    SetStage('stages/underwater.gif')

    #create new Sprite Objects (sharks)
    global myShark1, myShark2
    myShark1 = Sprite('sprites/shark.png')     
    myShark2 = Sprite('sprites/shark.png')

    #setup the sprites
    myShark1.Shrink(30)
    myShark1.SetLocation(80, 160)

    myShark2.Shrink(30)
    myShark2.SetLocation(110, 80)

    Text('Shark Invaders', size=36, colour=Orange, centre=True)


#this function is called over and over again at regular intervals
def loop():
    myShark1.MoveSteps(2)
    myShark2.MoveSteps(1)
    
    if myShark1.Right > SCREEN_WIDTH:
        myShark1.Direction = Left
        myShark1.MoveDown(20)
        myShark1.FlipVertical()
        
    if myShark1.Left < 0:
        myShark1.Direction = Right
        myShark1.MoveDown(20)
        myShark1.FlipVertical()


def when_LEFT_key_pressed():
    myShark1.Direction = Left
    
def when_RIGHT_key_pressed():
    myShark1.Direction = Right
