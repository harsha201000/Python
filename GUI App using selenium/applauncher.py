from tkinter import *
from tkinter.ttk import *
from selenium import webdriver

window = Tk()
window.geometry("600x600")
window.title("Python Selenium App Launcher")

google = PhotoImage(file='google.png')
instagram = PhotoImage(file='instagram.png')
youtube = PhotoImage(file='youtube.png')
gmail = PhotoImage(file='gmail.png')

photo_gg = google.subsample(10,10)
photo_in = instagram.subsample(10,10)
photo_yt = youtube.subsample(10,10)
photo_gm = gmail.subsample(10,10)

def gg():
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=option)
    
    driver.get("https://google.com/")
    
def ins():
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=option)
    
    driver.get("https://instagram.com/")
    
def yt():
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=option)
    
    driver.get("https://youtube.com/")
    
def gm():
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=option)
    
    driver.get("https://mail.google.com/")

button_google = Button(window,image=photo_gg,width=10,command=gg)
button_google.pack()

button_instagram = Button(window,image=photo_in,width=10,command=ins)
button_instagram.pack()

button_youtube = Button(window,image=photo_yt,width=10,command=yt)
button_youtube.pack()

button_gmail = Button(window,image=photo_gm,width=10,command=gm)
button_gmail.pack()

window.mainloop()