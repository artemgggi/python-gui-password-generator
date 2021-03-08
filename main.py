from tkinter import *
import random

'''Data'''
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '~', '`']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
words = ['a', 'b', 'c', 'd', 'e''f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
capital_words = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']


def clicked():
    result = (str(random.choice(numbers)) +
              random.choice(capital_words) +
              random.choice(symbols) +
              str(random.choice(numbers)) +
              random.choice(words) +
              random.choice(words) +
              str(random.choice(numbers)) +
              random.choice(words) +
              random.choice(words)
              )

    ent.delete(0, END)
    ent.insert(1, result)


'''Creating window'''
window = Tk()
window.title("PASSWORD-GENERATOR")
window.geometry('400x100')
window.resizable(width=False, height=False)
x = (window.winfo_screenwidth() - window.winfo_reqwidth()) / 2
y = (window.winfo_screenheight() - window.winfo_reqheight()) / 2
window.wm_geometry("+%d+%d" % (x, y))
window.iconbitmap('images/windowicon.ico')

'''Background image '''
C = Canvas(window, bg="white", height=50, width=300)
filename = PhotoImage(file="images/back.png")
background_label = Label(window, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

'''Button Generate'''
btn = Button(window, borderwidth=0, text='GENERATE', background='black', foreground="white", command=clicked)
btn.pack(side=TOP)
btn.place(x=158, y=25)

'''Password Entry'''
ent = Entry(window, justify=CENTER)
ent.pack(side=TOP)
ent.place(x=120, y=70)
ent.insert(0, 'click on the button')

window.mainloop()
