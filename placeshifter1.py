from ttk import Tkinter as tk
from Tkinter import *
class Shifter:
    
    def shiftforward(self): 
        shiftlist=[]
        shiftsource=self.stuff.get(1.0,'end-1c')
        shiftlist = list(shiftsource)
        spacelocations=[]
        for i in range(0,len(shiftsource)):
            if shiftsource[i]==' ':
                spacelocations.append(i)
                print(i)   
        for x in range(0,len(spacelocations)):
            if spacelocations[x]!=0:
               shiftlist[spacelocations[x]]=shiftlist[spacelocations[x]-1]
               shiftlist[spacelocations[x]-1]=' '
        shiftsource="".join(shiftlist)
        self.stuff.delete(1.0,END)
        self.stuff.insert(END, shiftsource)


    def shiftbackward(self):
        shiftlist=[]
        shiftsource=self.stuff.get(1.0,'end-1c')
        shiftlist= list(shiftsource)
        spacelocations=[]
        for i in range(0,len(shiftsource)):
            if shiftsource[i]==' ':
                spacelocations.append(i)
                print(i)
        for x in range(0,len(spacelocations)):
            if spacelocations[x]!=len(shiftlist)-1:
                shiftlist[spacelocations[x]]=shiftlist[spacelocations[x]+1]
                shiftlist[spacelocations[x]+1]=' '
        shiftsource="".join(shiftlist)
        self.stuff.delete(1.0,END)
        self.stuff.insert(END, shiftsource)


    def __init__(self, master):
        self.master = master
        master.title("Place Shifter")
        self.sourcelabel = Label(master, text="Source: ", bg='#545FF0')
        self.sourcelabel.grid(column = 0, row=0, padx=(10,0), pady=(10,10), sticky = 'w')
        
        self.stuff = Text(master, height=10, width=60)
        self.stuff.grid(rowspan=4, column=0, row=1, padx=(10,0), pady=(10,10), sticky = 'nsew')
        self.scrollstuff = Scrollbar(master)
        self.scrollstuff.config(command=self.stuff.yview)
        self.stuff.config(yscrollcommand=self.scrollstuff.set)
        self.scrollstuff.grid(rowspan=4, row = 1, column=1, padx=(0,30), pady=(10,10), sticky='n' + 's' + 'w')
        
        self.rightshift = Button(master, text = "Shift Forward", command = self.shiftforward, bg='#545FF0')
        self.rightshift.grid(row=5, column=0, padx=(10,10), pady=(20,20), sticky='w')

        self.leftshift = Button(master, text = "Shift Backward", command = self.shiftbackward, bg='#545FF0')
        self.leftshift.grid(row=5, column=0, sticky='e', pady=(20,20), padx=(10,10))

root=Tk()
my_gui=Shifter(root)
root.configure(background='grey')
root.mainloop()

