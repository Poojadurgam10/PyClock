from tkinter import Label, Tk
import time
app_window = Tk()
app_window.title("Digital Clock")
app_window.geometry("420x150")
app_window.resizable(1,1)

text_font = ("FF Mark", 70, 'bold')
background = "#253342"
foreground = "#cbd6e2"
border_width = 30

label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=0, column=1)

def digital_clock():
    time_live = time.strftime("%I:%M:%S %p")
    label.config(text=time_live)
    label.after(200, digital_clock)
digital_clock()
app_window.mainloop()



