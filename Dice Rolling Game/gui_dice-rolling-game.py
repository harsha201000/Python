from tkinter import *
import random
import winsound

window = Tk()
window.geometry("500x500")
window.title("Rolling the Dice App")

def get_number(x):
     if x == '\u2680':
         return(1)
     elif x == '\u2681':
         return(2)
     elif x == '\u2682':
         return(3)
     elif x == '\u2683':
         return(4)
     elif x == '\u2684':
         return(5)
     elif x == '\u2685':
         return(6)

def roll_dice():
    dice1 = random.choice(dice)
    winsound.PlaySound("dice_roll.wav",winsound.SND_ASYNC)
    dice2 = random.choice(dice)
    winsound.PlaySound("dice_roll.wav",winsound.SND_ASYNC)
    
    sd1 = get_number(dice1)
    sd2 = get_number(dice2)
    
    dice_label.config(text=dice1)
    dice_label2.config(text=dice2)
    
    sub_dice_label.config(text=sd1)
    sub_dice_label2.config(text=sd2)
    
    total = sd1 + sd2
    
    total_label.config(text="You rolled: {}".format(total))

dice_logo = PhotoImage(file='icons8-dice-80.png')
window.iconphoto(True, dice_logo)

dice = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']

frame = Frame(window)
frame.pack(pady=20)

dice_label = Label(frame, text=dice[0], font=('comisans',50), fg="black")
dice_label.grid(row=0, column=0, padx=5)

sub_dice_label = Label(frame, text="")
sub_dice_label.grid(row=1, column=0)

dice_label2 = Label(frame, text=dice[0], font=('comisans',50), fg="black")
dice_label2.grid(row=0, column=1, padx=5)

sub_dice_label2 = Label(frame, text="")
sub_dice_label2.grid(row=1, column=1)

button = Button(window, text="Roll Dice", command= roll_dice, font= ('comisans',24))
button.pack(pady=20)

total_label = Label(window, text="Dice", font=('comisans',24), fg="darkgrey")
total_label.pack(pady=40)

roll_dice()

window.mainloop()