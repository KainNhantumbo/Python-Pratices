#  GUI in python
from tkinter import *
from fuctions import run_click

# creates a window
main_window = Tk()
main_window.geometry('480x320') #sets a window size
main_window.title('Main Window')
main_window.config(background='#f3f4dc')

# sets a icon for the window
icon = PhotoImage(file='.\\Exercise 06\\icone.png')
main_window.iconphoto(True, icon)

#  sets label for text or images 
label = Label(main_window,text='Hello Python Window',
              font=('Inter', 12, 'normal'), background='#f3f4dc')
label.place(x=0, y=0)

# sets a button
btn = Button(main_window, text='Click me', command=run_click, padx=10, pady=10,
             state=ACTIVE, activebackground='#05c3c4', activeforeground='#fcfcfc', 
             font=('Inter', 10, 'bold'))

btn.place(x=5, y=25)

#starts the window
main_window.mainloop()
