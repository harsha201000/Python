from tkinter import *
import random

# List of possible colors
colors = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple', 'Indigo', 'Violet', 'Pink', 'Black', 'Gray', 'Brown'
          , 'Gold', 'Silver', 'Black']
score = 0

# time game left -- 60 seconds
time_left = 60

# start_game function
def start_game(event):
    
    if time_left == 60:
        
        # start the countdown timer
        countdown()
    
    # run the function to choose the next color
    next_color()
    
# Function to choose and display the next color
def next_color():
    
    # use the globally declared score variable
    global score
    global time_left
    
    # if a game is currently in play
    if time_left > 0:
        entry.focus_set()
        
        # if the color typed is equal
        # to the color of the text
        if entry.get().lower() == colors[1].lower():
            
            score += 1
            
        # clear the text entry box
        entry.delete(0, END)
        
        random.shuffle(colors)
        # change the color to type by changing the text and the color to a random color
        label.config(fg = str(colors[1]), text = str(colors[0]))
        
        # update the score
        score_label.config(text = "Score: "+ str(score))
        
# Countdow timer function
def countdown():
    
    global time_left
    
    # if game is in play
    if time_left > 0:
        
        # decrease the timer
        time_left -= 1
        
        #update the timer label
        timer_label.config(text = "Time Left: " + str(time_left))
        
        timer_label.after(1000, countdown)
        
        
        
# code

#Create a window
window = Tk()
window.title("Color Test Game")
window.geometry("400x200")

colors_icon = PhotoImage(file='icons8-color-swatch-48.png')
window.iconphoto(True, colors_icon)

instructions_label = Label(window, text="Enter a color of the words, and not in the word text!", font=("Helvetica", 12))
instructions_label.pack()

# add a score_label
score_label = Label(window, text = "Press enter to start", font=("Helvetica", 12))
score_label.pack()

# add a time left label
timer_label = Label(window, text="Time Left: " + str(time_left), font=("Helvetica", 12))
timer_label.pack()

# add a label for displaying the colors
label = Label(window, font=('Helvetica', 60))
label.pack()

# add a text entry box for typing in the colors
entry = Entry(window)

# run the startgame function when enter key is pressed
window.bind('<Return>', start_game)
entry.pack()

# set focus on the entry box
entry.focus_set()

window.mainloop()
        
        