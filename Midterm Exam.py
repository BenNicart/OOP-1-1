from tkinter import *
window = Tk()

window.geometry("600x500+30+20")
window.title("Midterms in OOP")




def text_sample():
    name = fullname.get()

    namedisplay.insert(0,f'{name}')

fullname = Entry(window, bd = 3, font = ("verdana",12))
fullname.place(x=300,y=100)


EnterName = Label(window, text = "Enter your Fullname",  fg="red")
EnterName.place(x=80, y=100)


click = Button(window,text = "Click to display your Fullname",  fg="red", command=text_sample)
click.place(x=80,y=150)


namedisplay = Entry(window, bd = 3, font = ("verdana",12))
namedisplay.place(x=300,y=150)

window.mainloop()

