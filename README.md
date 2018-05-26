# python-bytes

Python module to make the designing of computer/video games much easier. It hides all the complicated pygame code in a module and provides an easy API to create games in minutes. To get started, see the examples directory.  

## Prerequisites

* Python 2.7.15 32bit  
[Python Download](https://www.python.org/downloads/release/python-2715/)  
* Pygame 32bit for Python 2.7  
[Pygame Download](http://pygame.org/ftp/pygame-1.9.2a0.win32-py2.7.msi)  
  

## Library

Can be copied to the python include directory or left alongside the python program  
  
Windows  C:\Python27\Lib  
Linux    /usr/lib/python2.7  

Use the compiled version to hide the source code (*.pyc)  

_NOTE: pygame must be installed for it to work correctly (Raspberry PI Python27 comes preloaded with pygame)_  

File | Description
---- | -----------
library/pythonbytes.py | source code for the library
library/pythonbytes.pyc | compiled version


## Examples

Some sample applications made using this library of varying levels of difficulty  
_NOTE: The examples directory contains folders of images used as sprites and stages and are copyright of Scratch (https://scratch.mit.edu/) and are not owned by the author of python-bytes._  

File | Description
---- | -----------
examples/maze.py | control a ball around the maze using the cursors
examples/automaze.py | Uses right-hand algorithm to automatically navigate around maze
examples/automaze-rpi.py | Same as above, but designed to run on the PiTFT touchscreen
examples/stopwatch.py | Digital clock with condition to check alarm time
examples/sharks.py | Visual game to practise moving sprites on a stage (e.g. Scratch)
examples/holiday-basic.py | This is what is achieved from the activity sheet
examples/holiday-full.py | The above - taken a bit further
examples/sprites | Images for sprites - mainly taken from scratch
examples/stages | Images for backgrounds - mainly taken from scratch