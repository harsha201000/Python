from tkinter import *
import numpy as np
import cv2
import time
import pyautogui

# create a new_window function
def new_window():
    window = Tk()
    window.geometry("400x200+0+0")
    window.resizable(0,0)
    window.title("Take a screenshot")
    
    frame1 = Frame(window,bg="white")
    frame1.pack(side=TOP)
    
    def take_screenshot():
        window.destroy()
        time.sleep(0.5)
        image = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
        cv2.imwrite("image1.png",image)
        time.sleep(0.5)
        new_window()
        
        
    # create a button
    button = Button(frame1,padx=32,pady=8,bd=4,fg="black",font=("Arial",20,'bold'),text="Take Screenshot",bg="green",command=take_screenshot)
    button.grid(row=5,column=1)
    
    
    
    window.mainloop()
    
new_window()