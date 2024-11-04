from tkinter import *
import googletrans
import textblob
from tkinter import ttk, messagebox

def translate():
    translated_text.delete(1.0,END)
    try:
        for key, value in languages.items():
            if (value == original_combo.get()):
                from_language_key = key
        
        for key, value in languages.items():
            if (value == translated_combo.get()):
                to_language_key = key
                
        words = textblob.TextBlob(original_text.get(1.0, END))
        words = words.translate(from_lang=from_language_key, to=to_language_key)
        translated_text.insert(1.0, words)
    except Exception as e:
        messagebox.showerror("Translator", e)
        
def clear():
    original_text.delete(1.0, END)
    translated_text.delete(1.0, END)
    
    
application = Tk()
application.geometry("880x300")
application.title("Translate")

translate_logo = PhotoImage(file='icons8-google-translate-48.png')
application.iconphoto(True, translate_logo)

languages = googletrans.LANGUAGES
language_list = list(languages.values())

original_text = Text(application, height=10, width=40)
original_text.grid(row=0, column=0, pady=20, padx=10)

translate_button = Button(application, text="Translate", font=("Arial",25), command=translate)
translate_button.grid(row=0, column=1, padx=10)

translated_text = Text(application, height=10, width=40)
translated_text.grid(row=0, column=2, pady=20, padx=10)

original_combo = ttk.Combobox(application, width=50, value=language_list)
original_combo.current(21)
original_combo.grid(row=1, column=0)


translated_combo = ttk.Combobox(application, width=50, value=language_list)
translated_combo.current(26)
translated_combo.grid(row=1, column=2)

clear_button = Button(application, text="clear", command=clear)
clear_button.grid(row=2, column=1)


application.mainloop()