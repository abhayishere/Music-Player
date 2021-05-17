from tkinter import *
from tkinter import filedialog
from mutagen.mp3 import MP3
import pygame
import time
import tkinter.ttk as ttk

root = Tk()
root.title("Music Player")
root.geometry("550x400")

pygame.mixer.init()


master_frame=Frame(root)
master_frame.pack(pady=20)

songbox=Listbox(master_frame,bg="black",fg="white",width=70, selectbackground="grey", selectforeground="black")
songbox.grid(row=0,column=0)

# control frame
controlframe=Frame(master_frame)
controlframe.grid(row=1,column=0,pady=20)

status_bar=Label(root,text='',bd=1,relief=GROOVE,anchor=E)
status_bar.pack(fill=X,side=BOTTOM,ipady=2)

