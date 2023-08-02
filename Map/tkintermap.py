from tkinter import *
import tkintermapview

window = Tk()
window.geometry("1920x1080")
window.title("Map View")

map_image = PhotoImage(file='icons8-map-64.png')
window.iconphoto(True, map_image)

label = LabelFrame(window)
label.pack(pady=20)

map_widget = tkintermapview.TkinterMapView(label, width=1500, height=800)
map_widget.set_position(36.1699, -115.1396)
map_widget.set_zoom(20)

map_widget.pack()

window.mainloop()