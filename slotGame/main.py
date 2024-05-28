from tkinter import *
from tkinter import ttk
from Pane import Pane
import time
from threading import Thread
import random as r

def updateImages(pane, slot):
    if(pane.getImage() == "cherry"):
        slot.config(image=cherryImage)
    elif(pane.getImage() == "bar"):
        slot.config(image=barImage)
    elif(pane.getImage() == "seven"):
        slot.config(image=sevenImage)
def checkVictory(window):
    print("Victory Checking")
    for pane in window:
        if pane != window[0]:
            return False
    return True
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
    updateImages(pane1,slot1)
    updateImages(pane2,slot2)
    updateImages(pane3,slot3)
    checkVictory(window)

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
window = (pane1, pane2, pane3)
"""PhotoImages for labels"""
slotMachineImage = PhotoImage(file="slotGame//res/slotmachine.png")
sevenImage = PhotoImage(file="slotGame//res/seven.png")
cherryImage = PhotoImage(file="slotGame//res/cherry.png")
barImage = PhotoImage(file="slotGame//res/bar.png")
scoreImage = PhotoImage(file="slotGame//res/score.png")
symbols = (sevenImage,cherryImage,barImage)
spinUnpressed = PhotoImage(file="slotGame\\res\spinUnpressed.png")
spinPressed = PhotoImage(file="slotGame\\res\spinPressed.png")
"""Widget Creation"""
frame  = ttk.Frame(root,height=500,width=1500,padding="0.5i") 
slotMachine = ttk.Label(frame, image = slotMachineImage)
slot1 = ttk.Label(slotMachine, image = barImage)
slot2 = ttk.Label(slotMachine, image = barImage)
slot3 = ttk.Label(slotMachine, image = barImage)
score = 0
canvas = Canvas(frame,width=scoreImage.width, height=scoreImage.height)
canvas.create_image(0, 0, anchor=NW, image=scoreImage)
score_text = canvas.create_text(scoreImage.width // 2, scoreImage.height // 2, text=str(score), fill="white", font=("Helvetica", 20))
spinButton = ttk.Button(frame, image = spinUnpressed)
canvas.pack()
"""Set Grid layout"""
frame.grid(column=0,row=0,sticky="N")
slotMachine.grid(column=0,row=0,sticky="N")
slot1.grid(column=0,row=0,sticky="W")
slot2.grid(column=1,row=0,sticky="W")
slot3.grid(column=2,row=0,sticky="W")

spinButton.grid(column=1,row=1,sticky="N")
"""Bind Button Function"""
spinButton.bind("<ButtonPress-1>", onSpinClick)
spinButton.bind("<ButtonRelease-1>", onSpinRelease)
"""make the padding for loop"""
children = frame.winfo_children()
for child in children:
    child.grid_configure(padx=10,pady=10)
root.mainloop()








