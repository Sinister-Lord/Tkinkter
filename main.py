from tkinter import *

window = Tk()
window.title("Tinkter Sample")

window.geometry("500x300")

greeting = Label(text = "I am Mahdi", fg= "blue", bg="white")

button = Button (text = "Name" , fg = "pink" , bg = "yellow")

entry = Entry(fg = "pink" , bg = "green" , width = 50)

greeting.pack()
button.pack()
entry.pack()

frame = Frame(master = window , relief = RAISED , borderwidth=3)

frame.pack()


label = Label(master= frame, text="HELLO")

label.pack()

textbook = Text ( fg = "orange" , bg="black")

textbook.pack()


window.mainloop()
