from tkinter import *
from tkinter import ttk
from Pane import Pane
import time
from threading import Thread
import random as r

def updateImages(pane, slot):
    if(pane.getImage() == "cherry"):
        print("cherry")

def spinning(label):
    for image in images:
        label.config(image = image)
        root.update()
def gameAction(*args):
    print("Spin method reached")
    pane1.generateSlot()
    pane2.generateSlot()
    pane3.generateSlot()
    target = (time.time() * 1000 ) + 2500
    while (time.time()*1000) < target:
        spinning(slot1)
        spinning(slot2)
        spinning(slot3)
    updateImages(pane1)
    updateImages(pane2)
    updateImages(pane3)
    spinButton.config(state=NORMAL)
def onSpinClick(event):
    print("Spin Button Click Reach")
    print(spinButton['state'])
    if spinButton['state'] == "normal":
        print("If statement reached")
        spinButton.config(state=DISABLED)
        spinButton.config(image=spinPressed)
        gameAction()
def onSpinRelease(event):
    spinButton.config(image=spinUnpressed)
root = Tk()
root.title("Snake's Slots")
"""Symbol Weights"""
cherryWeight = 50
sevenWeight = 30
barWeight = 20
"""Pane Creation"""
pane1 = Pane()
pane2 = Pane()
pane3 = Pane()
"""PhotoImages for labels"""
slotMachineImage = PhotoImage(file="slotGame//res/slotmachine.png")
sevenImage = PhotoImage(file="slotGame//res/seven.png")
cherryImage = PhotoImage(file="slotGame//res/cherry.png")
barImage = PhotoImage(file="slotGame//res/bar.png")
images = (sevenImage,cherryImage,barImage)
spinUnpressed = PhotoImage(file="slotGame\\res\spinUnpressed.png")
spinPressed = PhotoImage(file="slotGame\\res\spinPressed.png")
"""Widget Creation"""
frame  = ttk.Frame(root,height=500,width=1500,padding="0.5i") 
slotMachine = ttk.Label(frame, image = slotMachineImage)
slot1 = ttk.Label(slotMachine, image = barImage)
slot2 = ttk.Label(slotMachine, image = barImage)
slot3 = ttk.Label(slotMachine, image = barImage)
spinButton = ttk.Button(frame, image = spinUnpressed)
"""Set Grid layout"""
frame.grid(column=0,row=0,sticky="N")
slotMachine.grid(column=0,row=0,sticky="N")
slot1.grid(column=0,row=0,sticky="W")
slot2.grid(column=1,row=0,sticky="W")
slot3.grid(column=2,row=0,sticky="W")
spinButton.grid(column=1,row=0,sticky="W")
"""Bind Button Function"""
spinButton.bind("<ButtonPress-1>", onSpinClick)
spinButton.bind("<ButtonRelease-1>", onSpinRelease)
"""make the padding for loop"""
children = frame.winfo_children()
for child in children:
    child.grid_configure(padx=10,pady=10)
root.mainloop()






