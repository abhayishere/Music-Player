from tkinter import *
from tkinter import filedialog
from mutagen.mp3 import MP3
import pygame
import time
import tkinter.ttk as ttk
from body import *

def play_time():
	if stopped:
		return
	current_time=pygame.mixer.music.get_pos()/1000
	good_time=time.strftime('%M:%S',time.gmtime(current_time))

	# slider_label.config(text=f'Slider: {int(my_slider.get())} and Song Pos:{int(current_time)}')
	current_one=songbox.curselection()
	song=songbox.get(current_one)
	song="C:/Users/Abhay Yadav/Downloads/tkinter/Tkinter/songs/"+song+".mp3"

	song_mut=MP3(song)
	global full_length
	full_length=song_mut.info.length

	full_time=time.strftime('%M:%S',time.gmtime(full_length))
	current_time+=1

	if(int(my_slider.get())==int(full_length)):
		status_bar.config(text="Time elapsed "+full_time+" of "+full_time)
	elif paused:
		pass
	elif int(my_slider.get())==int((current_time)):
		slider_position=int(full_length)
		my_slider.config(to=slider_position,value=int(current_time))
	else:
		slider_position=int(full_length)
		my_slider.config(to=slider_position,value=int(my_slider.get()))
		good_time=time.strftime('%M:%S',time.gmtime(int(my_slider.get())))
		status_bar.config(text="Time elapsed "+good_time+" of "+full_time)
		next_time=int(my_slider.get())+1
		my_slider.config(value=next_time)

	status_bar.after(1000,play_time)


# Add song
def add_song():
	song=filedialog.askopenfilename(initialdir='songs/',title="Choose a file",filetypes=(("mp3 Files","*.mp3"),))
	song=song.replace("C:/Users/Abhay Yadav/Downloads/tkinter/Tkinter/songs/","")
	song=song.replace(".mp3","")
	songbox.insert(END,song)

def add_many_songs():
	songs=filedialog.askopenfilenames(initialdir='songs/',title="Choose a file",filetypes=(("mp3 Files","*.mp3"),))
	for song in songs:
		song=song.replace("C:/Users/Abhay Yadav/Downloads/tkinter/Tkinter/songs/","")
		song=song.replace(".mp3","")
		songbox.insert(END,song)

# play the song
def play():
	global stopped
	stopped=False
	song=songbox.get(ACTIVE)
	song="C:/Users/Abhay Yadav/Downloads/tkinter/Tkinter/songs/"+song+".mp3"
	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0)

	play_time()
global stopped
stopped=False
def stop():
	status_bar.config(text='')
	my_slider.config(value=0)
	pygame.mixer.music.stop()
	songbox.selection_clear(ACTIVE)
	status_bar.config(text='')
	global stopped
	stopped=True

def nextsong():
	status_bar.config(text='')
	my_slider.config(value=0)
	next_one=songbox.curselection()
	next_one=next_one[0]+1;
	if next_one==songbox.size():
		next_one=0;
	song=songbox.get(next_one)
	
	# print(song)

	song="C:/Users/Abhay Yadav/Downloads/tkinter/Tkinter/songs/"+song+".mp3"
	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0)

	songbox.selection_clear(0,END)
	songbox.activate(next_one)
	songbox.selection_set(next_one,last=None)

def previoussong():
	status_bar.config(text='')
	my_slider.config(value=0)
	next_one=songbox.curselection()
	next_one=next_one[0]-1;
	if next_one==-1:
		next_one=songbox.size()-1
	song=songbox.get(next_one)
	
	# print(song
	song="C:/Users/Abhay Yadav/Downloads/tkinter/Tkinter/songs/"+song+".mp3"
	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0)

	songbox.selection_clear(0,END)
	songbox.activate(next_one)
	songbox.selection_set(next_one,last=None)

global paused
paused=False
def pause(ispaused):
	global paused
	paused=ispaused

	if paused:
		pygame.mixer.music.unpause()
		paused=False
	else:
		pygame.mixer.music.pause()
		paused=True
	
def slide(x):
	# slider_label.config(text=f'{int(my_slider.get())} of {int(full_length)}')
	song=songbox.get(ACTIVE)
	song="C:/Users/Abhay Yadav/Downloads/tkinter/Tkinter/songs/"+song+".mp3"
	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0,start=int(my_slider.get()))

def volume(x):
	pygame.mixer.music.set_volume(volume_slider.get())

my_slider=ttk.Scale(master_frame,from_=0,to=100,orient=HORIZONTAL,value=0,command=slide,length=360)
my_slider.grid(padx=10,row=2,column=0,pady=10)

volume_frame=LabelFrame(master_frame,text="Volume")
volume_frame.grid(row=0,column=1,padx=20)
volume_slider=ttk.Scale(volume_frame,from_=0,to=1,orient=VERTICAL,value=1,command=volume,length=150)
volume_slider.pack(padx=10,pady=10,ipady=10)