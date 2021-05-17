from tkinter import *
from tkinter import filedialog
from mutagen.mp3 import MP3
import pygame
import time
import tkinter.ttk as ttk
from body import *
from functions import *
from display import *

backbtn=Button(controlframe,image=backwardimg,borderwidth=0,command=previoussong)
forwardbtn=Button(controlframe,image=forwardimg,borderwidth=0,command=nextsong)
playbtn=Button(controlframe,image=playimg,borderwidth=0,command=play)
pausebtn=Button(controlframe,image=pauseimg,borderwidth=0,command=lambda: pause(paused))
stopbtn=Button(controlframe,image=stopimg,borderwidth=0,command=stop)

backbtn.grid(row=0,column=0,padx=10)
forwardbtn.grid(row=0,column=1,padx=10)
playbtn.grid(row=0,column=2,padx=10)
pausebtn.grid(row=0,column=3,padx=10)
stopbtn.grid(row=0,column=4,padx=10)
