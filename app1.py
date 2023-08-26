import pyshorteners
from tkinter import*

# Create a window
win = Tk()
win.geometry("500x300")
win.configure(bg="light blue")

# Function

def shortener():
    url = entry1.get()
    s = pyshorteners.Shortener().tinyurl.short(url)
    entry2.insert(END,s)


# Create a label
Label(win,text="Enter the URL:", font="impack 16 bold", bg="black",fg="white").pack(fill="x")

# Create a Entry box
entry1 = Entry(win, font="12" , bd=2, width=45)
entry1.pack(pady=35)

# Create a button
Button(win,text="Click" , font="impack 10 bold", bg="pink",fg= "black",command=shortener).pack()

# For shortened URL
entry2 = Entry(win,font="impack 14", bg="light blue", width=30,bd=0)
entry2.pack(pady=35)




mainloop()
