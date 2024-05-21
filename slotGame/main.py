from tkinter import *
from tkinter import ttk





def main():
    root = Tk()
    root.title("Snake's Slots")
    """PhotoImages for labels"""
    slotMachineImage = PhotoImage(file="slotGame//res/slotmachine.png")
    cherryImage = PhotoImage(file="slotGame//res/cherry.png")
    cherryImage = PhotoImage(file="slotGame//res/seven.png")
    barImage = PhotoImage(file="slotGame//res/bar.png")
    
    frame  = ttk.Frame(root,height=500,width=1500,padding="0.5i")
    slotMachine = ttk.Label(frame, image=slotMachineImage)
    frame1 = ttk.Label(slotMachine, image = barImage)
    frame2 = ttk.Label(slotMachine, image = barImage)
    frame3 = ttk.Label(slotMachine, image = barImage)

    
    """Set Grid layout here"""
    frame.grid(column=0,row=0,sticky="N")
    slotMachine.grid(column=0,row=0,sticky="N")
    frame1.grid(column=0,row=0,sticky="W")
    frame2.grid(column=1,row=0,sticky="W")
    frame3.grid(column=2,row=0,sticky="W")
    """make the padding for loop"""
    root.mainloop()
main()



