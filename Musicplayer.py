from tkinter import *
from tkinter import filedialog
from mutagen.mp3 import MP3
import pygame
import time
import tkinter.ttk as ttk
from body import *
from functions import *
from display import *
from buttons import *

music_menu=Menu(root)
root.config(menu=music_menu)


add_song_menu=Menu(music_menu)
music_menu.add_cascade(label="Add",menu=add_song_menu)
add_song_menu.add_command(label="Add a song to the playlist",command=add_song)
add_song_menu.add_command(label="Add many songs to the playlist",command=add_many_songs)


root.mainloop()
