from tkinter import *

tk = Tk()

c = Canvas(tk, width=500, height=500, bg="white")
c.pack()


c.create_oval(125, 250, 200, 325, width=2, fill="white")
c.create_oval(275, 250, 350, 325, width=2, fill="white")

c.create_polygon((50, 260), (100, 250), (120, 200), (200, 200),(200, 250), (400, 250), (400, 300),(350, 300), (325, 275), (300, 275),(275, 300),(200, 300),(175, 275),(150, 275), (125, 300), (50, 300), fill="black", width=2, outline="black")



tk.mainloop()