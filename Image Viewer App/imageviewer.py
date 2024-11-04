from tkinter import *
from PIL import ImageTk, Image

def forward(img_no):
 
    # GLobal variable so that we can have
    # access and change the variable
    # whenever needed
    global label
    global button_forward
    global button_back
    global button_exit
    label.grid_forget()
 
    # This is for clearing the screen so that
    # our next image can pop up
    label = Label(image=images[img_no-1])
 
    # as the list starts from 0 so we are
    # subtracting one
    label.grid(row=1,column=0,columnspan=3)
    button_for = Button(app,text="Forward",command=lambda:forward(img_no+1))
 
    # img_no+1 as we want the next image to pop up
    if img_no == 24:
        button_forward = Button(app,text="Forward",state=DISABLED)
 
    # img_no-1 as we want previous image when we click
    # back button
    button_back = Button(app,text="Back",command=lambda:back(img_no-1))
 
    # Placing the button in new grid
    button_back.grid(row=5,column=0)
    button_exit.grid(row=5,column=1)
    button_for.grid(row=5,column=2)
    
def back(img_no):
 
    # We will have global variable to access these
    # variable and change whenever needed
    global label
    global button_forward
    global button_back
    global button_exit
    label.grid_forget()
 
    # for clearing the image for new image to pop up
    label = Label(image=images[img_no - 1])
    label.grid(row=1,column=0,columnspan=3)
    button_forward = Button(app,text="Forward",command=lambda: forward(img_no + 1))
    button_back = Button(app,text="Back",command=lambda: back(img_no - 1))
    print(img_no)
 
    # whenever the first image will be there we will
    # have the back button disabled
    if img_no == 1:
        button_back = Button(app,text="Back",state=DISABLED)
 
    label.grid(row=1, column=0, columnspan=3)
    button_back.grid(row=5, column=0)
    button_exit.grid(row=5, column=1)
    button_forward.grid(row=5, column=2)


app = Tk()
app.title("Image Viewer")
app.geometry("700x700")

photo = PhotoImage(file="photo.png")
app.iconphoto(True,photo)

image_no_1 = ImageTk.PhotoImage(Image.open("images/backpackman.jpg"))
image_no_2 = ImageTk.PhotoImage(Image.open("images/baseball.jpg"))
image_no_3 = ImageTk.PhotoImage(Image.open("images/boy_doughnut.jpg"))
image_no_4 = ImageTk.PhotoImage(Image.open("images/fire_hydrant.jpg"))
image_no_5 = ImageTk.PhotoImage(Image.open("images/frisbee_2.jpg"))
image_no_6 = ImageTk.PhotoImage(Image.open("images/frisbee.jpg"))
image_no_7 = ImageTk.PhotoImage(Image.open("images/kyte.jpg"))
image_no_8 = ImageTk.PhotoImage(Image.open("images/looking_at_computer.jpg"))
image_no_9 = ImageTk.PhotoImage(Image.open("images/multi_skiing.jpg"))
image_no_10 = ImageTk.PhotoImage(Image.open("images/on_bus.jpg"))
image_no_11 = ImageTk.PhotoImage(Image.open("images/person_bench.jpg"))
image_no_12 = ImageTk.PhotoImage(Image.open("images/riding_elephant.jpg"))
image_no_13 = ImageTk.PhotoImage(Image.open("images/skate_park_venice.jpg"))
image_no_14 = ImageTk.PhotoImage(Image.open("images/skate_park.jpg"))
image_no_15 = ImageTk.PhotoImage(Image.open("images/skiing.jpg"))
image_no_16 = ImageTk.PhotoImage(Image.open("images/tennis_in_crowd.jpg"))
image_no_17 = ImageTk.PhotoImage(Image.open("images/tennis_standing.jpg"))
image_no_18 = ImageTk.PhotoImage(Image.open("images/tennis.jpg"))
image_no_19 = ImageTk.PhotoImage(Image.open("images/tie_with_beer.jpg"))
image_no_20 = ImageTk.PhotoImage(Image.open("images/truck.jpg"))
image_no_21 = ImageTk.PhotoImage(Image.open("images/two_on_bench.jpg"))
image_no_22 = ImageTk.PhotoImage(Image.open("images/with_computer.jpg"))
image_no_23 = ImageTk.PhotoImage(Image.open("images/soccer.png"))
image_no_24 = ImageTk.PhotoImage(Image.open("images/snowboard.jpg"))

images = [image_no_1,image_no_2,image_no_3,image_no_4,image_no_5,image_no_6,image_no_7,image_no_8,image_no_9,image_no_10,image_no_11,image_no_12,image_no_13,image_no_14,image_no_15,image_no_16,image_no_17,image_no_18,image_no_19,image_no_20,image_no_21,image_no_22,image_no_23,image_no_24]

label = Label(image=image_no_1)
 
# We have to show the box so this below line is needed
label.grid(row=1, column=0, columnspan=3)
 
# We will have three button back ,forward and exit
button_back = Button(app, text="Back", command=back,state=DISABLED)
 
# app.quit for closing the app
button_exit = Button(app, text="Exit",command=app.quit)
 
button_forward = Button(app, text="Forward",command=lambda: forward(1))
 
# grid function is for placing the buttons in the frame
button_back.grid(row=5, column=0)
button_exit.grid(row=5, column=1)
button_forward.grid(row=5, column=2)
 
app.mainloop()