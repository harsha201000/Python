from tkinter import *
from tkvideo import tkvideo

#create instance for window
window = Tk()

#set window title
window.title("Video Player")

#set window icon photo
play = PhotoImage(file='icons8-play-48.png')
window.iconphoto(True,play)

#creating label
video_label = Label(window)
video_label.pack()

#Root video to display on label
media_player = tkvideo("CruiseTrip2019.mp4", video_label, loop=1, size=(1360, 800))
media_player.play()

window.mainloop()