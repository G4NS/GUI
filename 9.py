from tkinter import *

tk = Tk()
c = Canvas(tk, width=1010, height=610, bg="white")
c.pack()

c.create_oval(70, 10, 1000, 600, width=2, fill="white")
c.create_oval(90, 50, 900, 550, width=2, fill="white")
c.create_oval(110, 100, 800, 500, width=2, fill="white")
c.create_oval(130, 150, 700, 450, width=2, fill="white")
c.create_oval(150, 200, 600, 400, width=2, fill="white")

c.create_text(950, 305, text="5 лет")
c.create_text(850, 305, text="4 года")
c.create_text(750, 305, text="3 года")
c.create_text(650, 305, text="2 года")
c.create_text(550, 305, text="1 год")

tk.mainloop()