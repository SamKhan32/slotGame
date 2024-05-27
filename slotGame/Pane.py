from tkinter import *
from tkinter import ttk
import random as r
cherryPath ="slotGame\\res\cherry.png"
sevenPath = "slotGame\\res\seven.png"
barPath = "slotGame\\res\\bar.png"
cherryWeight = 50
sevenWeight = 30
barWeight = 20
class Pane():
    """A window is an object that contains an image represented by a string"""
    image = "bar"
    def setImage(self,image):
        self.image = image
    def getImage(self):
        return self.image
    def generateSlot(self):
        randNumber = int( r.random() *100)
        print(randNumber)
        if randNumber <= barWeight:
            self.image = "bar"
        elif randNumber > barWeight and randNumber <= cherryWeight:
            self.image = "seven"
        elif randNumber > cherryWeight and randNumber <=100:
            self.image = "cherry"
