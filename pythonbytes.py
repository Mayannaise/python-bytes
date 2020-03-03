from __future__ import print_function
import random, os.path, sys
import pygame
import math
from pygame.locals import *
from tkinter import Tk
import datetime
import __main__

__author__ = 'Owen Jeffreys'
__copyright__ = 'Copyright (c) 2020, Owen Jeffreys'
__license__ = 'GPL'
__version__ = '1.3.1'
__maintainer__ = 'Owen Jeffreys'
__status__ = 'Development'

# define global constants
TITLE = 'Python Bytes!'
SCREEN_HEIGHT = 360
SCREEN_WIDTH = 480
SCREENRECT = Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
FRAMES_PER_SEC = 20     #cap fps to save CPU
PROG_DIR = '.'          #program's directory

# define global flags
_fullscreen = False
_loaded = False
_loop = True

# define global colour definitions
Red = red = (255,0,0)
Green = green = (0,255,0)
Blue = blue = (0,100,255)
Yellow = yellow = (255, 255, 0)
Orange = orange = (255, 200, 0)
Pink = pink = (255, 128, 192)
Purple = purple = (210, 0, 210)
Black = black = (0, 0, 0)
Grey = grey = (50, 50, 50)
White = white = (255, 255, 255)

# define direction definitions
Left = left = West = west = 0
Right = right = East = east = 1
Up = up = Top = top = North = north = 2
Down = down = Bottom = bottom = South = south = 3

# define boolean definitions
false = no = No = False
true = yes = Yes = True

# define string constants
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

# create busy indicator
whirlygig = ['|', '/', '-', '\\']
wgIndex = 0

# create global objects
root = Tk()
dirtyRects = []         #list of rectangles which need redrawing to screen
ObjectList = []         #array of all the sprites in the program

# initialise global variables
curStage = ''           #current stage filename

# initialise global objects
class Images: pass     #container for images


class Sprite():
    def __init__(self, image, transparent=True):
        self.Costume = LoadSprite(image, transparent)
        self.rect = self.Costume.get_rect()
        self.Alive = True
        self.Direction = Right
        self.rect.centerx = SCREEN_WIDTH/2
        self.rect.centery = SCREEN_HEIGHT/2
        ObjectList.append(self)

    def draw(self, screen):
        r = screen.blit(self.Costume, self.rect)
        dirtyRects.append(r)
        
    def erase(self, screen, background):
        r = screen.blit(background, self.rect, self.rect)
        dirtyRects.append(r)

    @property
    def Width(self):
        return self.rect.width

    @property
    def width(self):
        return self.rect.width

    @property
    def Height(self):
        return self.rect.height

    @property
    def height(self):
        return self.rect.height
    
    @property
    def X(self):
        return self.rect.centerx

    @property
    def x(self):
        return self.rect.centerx

    @property
    def Y(self):
        return self.rect.centery

    @property
    def y(self):
        return self.rect.centery

    @property
    def Left(self):
        return self.rect.left

    @property
    def left(self):
        return self.rect.left

    @property
    def Right(self):
        return self.rect.right

    @property
    def right(self):
        return self.rect.right

    @property
    def Top(self):
        return self.rect.top

    @property
    def top(self):
        return self.rect.top

    @property
    def Bottom(self):
        return self.rect.bottom

    @property
    def bottom(self):
        return self.rect.bottom

    def SetLocation(self, x, y):
        self.rect.centerx = x
        self.rect.centery = y
        return self

    def SetRotation(self, degrees):
        self.angle = self.angle + degrees
        self.Costume = pygame.transform.rotate(self.Costume, -degrees)
        r = self.rect
        self.rect = self.image.get_rect()
        self.rect.centerx = r.centerx
        self.rect.centery = r.centery
        return self
        
    def MoveSteps(self, steps=1):
        if self.Alive:
            if self.Direction == Left or self.Direction == Right:
                if self.Direction == Left: steps = -steps
                self.rect.centerx = self.rect.centerx + steps
            else:
                if self.Direction == Up: steps = -steps
                self.rect.centery = self.rect.centery + steps

    def MoveDown(self, y=10):
        self.SetLocation(self.x, self.y + y)

    def MoveUp(self, y=10):
        self.SetLocation(self.x, self.y - y)

    def MoveRight(self, x=10):
        self.SetLocation(self.x + x, self.y)
        
    def MoveLeft(self, x=10):
        self.SetLocation(self.x - x, self.y)

    def TurnRight(self):
        if self.Direction == Up:
            self.Direction = Right
        elif self.Direction == Right:
            self.Direction = Down
        elif self.Direction == Down:
            self.Direction = Left
        elif self.Direction == Left:
            self.Direction = Up

    def Resize(self, w, h):
        self.Costume = pygame.transform.scale(self.Costume, (w, h))
        r = self.rect
        self.rect = self.Costume.get_rect()
        self.rect.centerx = r.centerx
        self.rect.centery = r.centery
        return self

    def Shrink(self, factor=60.0):
        factor/=100.0
        self.Resize(int(self.Width*factor), int(self.Height*factor))
        return self

    def FlipVertical(self):
        self.Costume = pygame.transform.flip(self.Costume, True, False)
        return self

    def FlipHorizontal(self):
        self.Costume = pygame.transform.flip(self.Costume, False, True)
        return self

    def TouchingColour(self, col, edge=None):
        margin = 1
        
        if edge == Top:
            x1 = self.rect.left
            x2 = self.rect.right
            y1 = self.rect.top - margin
            y2 = self.rect.top
        elif edge == Bottom:
            x1 = self.rect.left
            x2 = self.rect.right
            y1 = self.rect.bottom - margin
            y2 = self.rect.bottom
        elif edge == Left:
            x1 = self.rect.left - margin
            x2 = self.rect.left
            y1 = self.rect.top
            y2 = self.rect.bottom
        elif edge == Right:
            x1 = self.rect.right - margin
            x2 = self.rect.right
            y1 = self.rect.top
            y2 = self.rect.bottom
        elif edge == None:
            x1 = self.rect.left
            x2 = self.rect.right
            y1 = self.rect.top
            y2 = self.rect.bottom

        pixelsChecked = 0
        pixelsFlagged = 0
        
        for x in range(x1,x2):
            for y in range(y1,y2):
                pixelsChecked += 1
                try:
                    if curStage.get_at((x, y)) == col:
                        pixelsFlagged += 1
                        if (pixelsFlagged >= pixelsChecked/4 or edge == None):
                            return True
                except:
                    pass
        return False
        

class Frame():	
    def __init__(self, *tex):
        self.textures = []
        for t in tex:
            self.textures.append(Sprite(t,tx=20))		#image w. transparent pixels
    
    def SetLocation(self,x,y):
        self.textures = [t.SetLocation(x,y) for t in self.textures]
        return self
            
    def Scale(self, factor):
        self.textures = [t.Shrink(factor) for t in self.textures]
        return self
        
    def Shrink(self, factor):
        self.Scale(factor)
        return self
        
    def Rotate(self, i, deg):
        self.textures[i-1].SetRotation(deg)
        return self
        
    def moveX(self, i, diff):	# pixel difference to move object (+ right, - left)
        return self
        
    def moveY(self, i, diff):	# pixel difference to move object (+ up, - down)
        return self
               

class Text:
    def __init__(self, text='', font='Arial', size=20, x=None, y=None, colour=(0,0,0), centre=False):
        self.colour = colour
        self.size = size
        self.text = ' '.join(text)  #join multiple args together with spaces
        self.font = pygame.font.SysFont(font, size)
        self.x = x
        self.y = y
        self.center = centre
        if self.x == None: self.x = 0; self.center = centre
        if self.y == None: self.y = 0; self.center = centre
        self.textRender = self.font.render(text, 1, colour)
        if centre: self.x = (SCREEN_WIDTH/2)-(self.textRender.get_width()/2)
        self.rect = self.textRender.get_rect(x=self.x, y=self.y)
        ObjectList.append(self)
        
    @property
    def Width(self):
        return self.rect.get_width()

    @property
    def Height(self):
        return self.rect.get_height()

    @property
    def Text(self):
        return self.text
    
    def SetText(self, val):
        self.text = str(val)
        self.textRender = self.font.render(self.text, 1, self.colour)
        if self.center: self.x = (SCREEN_WIDTH/2)-(self.textRender.get_width()/2)
        self.rect = self.textRender.get_rect(x=self.x, y=self.y)

    def AddText(self, val):
        self.text = self.text + str(val)
        self.SetText(self.text)

    def AppendText(self, val):
        self.AddText(val)

    def SetColour(self, col):
        self.colour = col
        self.textRender = self.font.render(self.text, 1, self.colour)
        self.rect = self.textRender.get_rect(x=self.x, y=self.y)
        
    def draw(self, screen):
        r = screen.blit(self.textRender, self.rect)
        dirtyRects.append(r)

    def erase(self, screen, background):
        r = screen.blit(background, self.rect, self.rect)
        dirtyRects.append(r)


def HideMouse():
    pygame.mouse.set_visible(0)

def ShowMouse():
    pygame.mouse.set_visible(1)

def FullScreen():
    if curStage != '':
        SetStage(curStage, True)

def Windowed():
    if curStage != '':
        SetStage(curStage, False)

def IsFullScreen():
    return _fullscreen

def ToggleFullScreen():
    if not IsFullScreen():
        FullScreen()
    else:
        Windowed()

def Day():
    now = datetime.datetime.now()
    return now.strftime('%A')

def Date():
    now = datetime.datetime.now()
    return now.strftime('%d') + ' ' + now.strftime('%B') + ' ' + now.strftime('%Y')

def Time():
    now = datetime.datetime.now()
    return now.strftime('%H') + ':' + now.strftime('%M') + ':' + now.strftime('%S')

## @brief Method to load sprite (movable image with transparent bg)
def LoadSprite(f, transparent=True):
    try:
        surface = pygame.image.load(f)
        if transparent:                                   #if remove bg
            corner = surface.get_at((0, 0))         #get transparent pixel
            surface.set_colorkey(corner, RLEACCEL)
            
        return surface.convert()
    except pygame.error:
        pass

    try:
        surface = pygame.image.load('sprites/' + f)
        if transparent:                                   #if remove bg
            corner = surface.get_at((0, 0))         #get transparent pixel
            surface.set_colorkey(corner, RLEACCEL)
            
        return surface.convert()
    except pygame.error:
        print ('\n[ERROR] ' + pygame.get_error())
        EndGame()

## @brief Method to load image for bg (no transparent)
def LoadStage(f):
    try:
        surface = pygame.image.load(f)
        return surface.convert()
    except pygame.error:
        pass

    try:
        surface = pygame.image.load('stages/' + f)
        return surface.convert()
    except pygame.error:
        print ('\n[ERROR] ' + pygame.get_error())
        EndGame()
    
## @brief Method to set the background image
def SetStage(stage, fullscreen=False):
    global surf, curStage

    if type(stage) is str:
        stageSurf = LoadStage(stage)
    else:
        stageSurf = stage

    curStage = stageSurf

    #if the picture is wider than the screen, shrink to fit
    if curStage.get_width() > curStage.get_height():
        if curStage.get_width() > root.winfo_screenwidth():
            r = curStage.get_height() / float(curStage.get_width())
            w = float(root.winfo_screenwidth()) - 10.0
            h = w * r
            ResizeStage(w,h,False)
    
    #resive the window so it fits the picture properly
    SetStageSize(curStage.get_width(), curStage.get_height(), fullscreen)
    
    for x in range(0, SCREENRECT.width, curStage.get_width()):
        surf.blit(curStage, (x, 0))
        
    screen.blit(curStage, (0,0))


def ResizeStage(w, h, update=True):
    global _fullscreen, curStage
    
    curStage = pygame.transform.scale(curStage, (int(w), int(h)))
    if update: SetStage(curStage, _fullscreen)

## @brief Clear screen of actors
def ClearScreen():
    global ObjectList
    
    for obj in ObjectList:
        obj.erase(screen, surf)

## @brief Update actors' positions etc, then display
def RefreshScreen():
    global dirtyRects, ObjectList

    ClearScreen()

    for obj in ObjectList:
        obj.draw(screen)

    pygame.display.flip()

    #only update areas which need to be
    pygame.display.update(dirtyRects)
    dirtyRects = []


def PrintWhirlygig():
    global whirlygig, wgIndex

    if not 'idlelib.run' in sys.modules:
        print('Running: ' + whirlygig[wgIndex], end='\r')
        wgIndex+=1
        if wgIndex >= len(whirlygig): wgIndex=0


def SetStageSize(x, y, fullscreen=False):
    global SCREEN_WIDTH, SCREEN_HEIGHT, SCREENRECT, _fullscreen
    global screen, surf
    
    SCREEN_WIDTH = x
    SCREEN_HEIGHT = y
    SCREENRECT = Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)

    if fullscreen:
        flag = pygame.FULLSCREEN | pygame.NOFRAME
        _fullscreen = True
    else:
        flag = 0
        _fullscreen = False
    
    screen = pygame.display.set_mode((SCREENRECT.width, SCREENRECT.height), flag)
   
    # remember new dims as this step changes the size slightly
    SCREEN_HEIGHT = screen.get_height()
    SCREEN_WIDTH = screen.get_width()
    SCREENRECT = Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)

    surf = pygame.Surface(SCREENRECT.size)

def EndLoop():
    global _loop
    _loop = False

def EndGame():
    pygame.quit()
    try:
        sys.exit()
    except SystemExit:
        os._exit(1)

def SetFPS(fps):
    global FRAMES_PER_SEC
    FRAMES_PER_SEC = fps
    print('@ ' + str(fps) + 'fps')

def print_header():
    print ('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    print ('$$                                           $$')
    print ('$$         --------------------------        $$')
    print ('$$         P Y T H O N    B Y T E S !        $$')
    print ('$$         --------------------------        $$')
    print ('$$                                           $$')
    print ('$$  Designed By: Owen Jeffreys               $$')
    print ('$$  %s        $$' % __copyright__)
    print ('$$  Contact: osjeffreys.uk@gmail.com         $$')
    print ('$$  Version: %s                           $$' % __version__)
    print ('$$                                           $$')
    print ('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    print ('')

## @brief Start function which initialises everything and calls the user code
def main():
    global screen, surf
    global dirtyRects, ObjectList
    global SCREENRECT
    global _loaded, _loop

    if not _loaded:
        print_header()
    
    #initialise game
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    clock = pygame.time.Clock()
    random.seed()
    
    #setup console (small mode)
    pygame.display.set_caption(TITLE)
    pygame.key.set_repeat(1, 20)
    SetStageSize(SCREEN_WIDTH, SCREEN_HEIGHT)

    # methods from imported program
    if 'init' in globals() and not _loaded:
        _loaded = True
        init()
        RefreshScreen()
 
    while 1:
        clock.tick(FRAMES_PER_SEC)      #don't run too fast
        ClearScreen()                   #clear sprites from screen
        PrintWhirlygig()                #display wirlygig if running in console window

        #read inputs and check for exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                EndGame()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 'when_mouse_clicked' in globals(): when_mouse_clicked()
                
            elif event.type == pygame.KEYUP:
                if event.key == K_ESCAPE:
                    EndGame()
                elif event.key == K_LEFT:
                    if 'when_LEFT_key_pressed' in globals(): when_LEFT_key_pressed()
                elif event.key == K_RIGHT:
                    if 'when_RIGHT_key_pressed' in globals(): when_RIGHT_key_pressed()
                elif event.key == K_UP:
                    if 'when_UP_key_pressed' in globals(): when_UP_key_pressed()
                elif event.key == K_DOWN:
                    if 'when_DOWN_key_pressed' in globals(): when_DOWN_key_pressed()
                elif event.key == K_SPACE:
                    if 'when_SPACE_key_pressed' in globals(): when_SPACE_key_pressed()
                elif event.key == K_RETURN:
                    if 'when_ENTER_key_pressed' in globals(): when_ENTER_key_pressed()
                    if 'when_RETURN_key_pressed' in globals(): when_RETURN_key_pressed()

            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    EndGame()
                elif event.key == K_LEFT:
                    if 'when_LEFT_key_held' in globals(): when_LEFT_key_held()
                elif event.key == K_RIGHT:
                    if 'when_RIGHT_key_held' in globals(): when_RIGHT_key_held()
                elif event.key == K_UP:
                    if 'when_UP_key_held' in globals(): when_UP_key_held()
                elif event.key == K_DOWN:
                    if 'when_DOWN_key_held' in globals(): when_DOWN_key_held()
                elif event.key == K_SPACE:
                    if 'when_SPACE_key_held' in globals(): when_SPACE_key_held()
                elif event.key == K_RETURN:
                    if 'when_ENTER_key_held' in globals(): when_ENTER_key_held()
                    if 'when_RETURN_key_held' in globals(): when_RETURN_key_held()
        
        #execute user code over and over if loop() exists in their file
        if 'loop' in globals() and _loop: loop()
        #place sprites back on screen
        RefreshScreen()

if __name__ == '__main__':
    #user attemping to run pythonbytes file manually
    #does not work, must be imported from another file
    print ('This file cannot be run - try importing it:')
    print ('import pythonbytes')
else:
    #user is including this module
    #import the user functions as this module calls them
    # loop() is called periodically
    # main() is called at startup
    try:
        src = __main__.__file__
    except:
        src = sys.argv[0]

    #read in file run by user and execute it
    exec(open(src).read())
    main()

# EOF
