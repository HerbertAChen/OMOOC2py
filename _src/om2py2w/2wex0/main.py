#!/usr/bin/python
# -*- coding: utf-8 -*-
# easyNote 桌面版 v0

from Tkinter import *
import easynote as EZ

class EasyNote(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent # save a reference to the parent widget
        self.initUI()
        
    def initUI(self):
        self.parent.title("EasyNote Desktop")
        self.pack(fill=BOTH, expand=1)
                
        self.entry = Entry(self)
        self.entry.bind('<Return>', self.newnote) # 有没有更好的方法?
        self.entry.pack()
        self.entry.focus_set()

        self.var = StringVar()
        self.initLabelText()
        self.label = Label(self, textvariable=self.var, justify=LEFT)
        self.label.pack()

    def initLabelText(self):
        allnotes = EZ.GetNotes('all')
        if allnotes == '':
            self.notes = allnotes
        else:
            self.notes = ''.join(allnotes['notes'])
        self.var.set(self.notes)

    def newnote(self, event):
        note = self.entry.get()
        EZ.NewNote(note)
        self.entry.delete(0, END)
        self.notes = ''.join(EZ.GetNotes('all')['notes'])
        self.var.set(self.notes)

def main():
  
    root = Tk()
    root.geometry("500x300+200+200")
    app = EasyNote(root)
    root.mainloop()  

if __name__ == '__main__':
    main() 