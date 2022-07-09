from tkinter import * 
import random 
from tkinter.messagebox import showerror
from tkinter import messagebox

root = Tk()
inputFieldOne = None
inputFieldTwo = None
errorTitle = None

#команды
def btn_click():
    inputFieldOneValue = inputFieldOne.get()
    inputFieldTwoValue = inputFieldTwo.get()
    try:
        randomNum = random.randint(int(inputFieldOneValue), int(inputFieldTwoValue))
        info["text"] = randomNum
        errorTitle["text"] = ""
    except ValueError:
        errorTitle["text"] = "Entered values are not valid!"

#оболочка
root["bg"] = "black"
root.title("Generator v2.0 DarkBlue Edition")
root.geometry("370x450")
root.resizable(width=False, height=False)

frame = Frame(root, bg="black")
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)

title = Label(frame, text="Generator v2.0 DarkBlue Edition", bg="black", fg="White", font=400)
title.pack()

title = Label(frame, text="Original by Mr.Ertor,\nhacked by NobootRecord", bg="black", fg="White", font=40)
title.pack()

title = Label(frame, text="-----------------------------------------------------------------------------------------------------", bg="Black", fg="Blue", font=40)
title.pack()

title = Label(frame, text="Enter the minimal value:", bg="Black", fg="White", font=400)
title.pack()

inputFieldOne = Entry(frame, bg="#000040", fg="yellow")
inputFieldOne.pack()

title = Label(frame, text="Enter the maximal value:", bg="Black", fg="White", font=400)
title.pack()

inputFieldTwo = Entry(frame, bg="#000040", fg="yellow")
inputFieldTwo.pack()

errorTitle = Label(frame, text="", bg="Black", fg="Red", font=20)
errorTitle.pack()

frame_bottom = Frame(root, bg="#000040", bd=5)
frame_bottom.place(relx=0.15, rely=0.70, relwidth=0.7, relheight=0.1)

info = Label(frame_bottom, text="Result will appear here", bg="#000040", fg="Yellow", font=40)
info.pack()

btn = Button(frame, text="Generate the number", bg="#000040", fg="Yellow", command=btn_click)
btn.pack()

root.mainloop() 
