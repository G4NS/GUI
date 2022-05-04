from tkinter import *

tk = Tk()

c = Canvas(tk, width=1000, height=500, bg="white")
c.pack()

c.create_oval(900, 50, 950, 100, width=2)

c.create_polygon((50, 250), (500, 50), (950, 250),fill="black", width=2, outline="black")
c.create_polygon((100, 250), (900, 250), (900, 450), (100, 450), fill="white", width=2, outline="black")

c.create_polygon((450, 450), (550, 450), (550, 300), (450, 300), fill="white", width=2, outline="black")

c.create_polygon((300, 400), (400, 400), (400, 300), (300, 300), fill="white", width=2, outline="black")
c.create_polygon((600, 400), (700, 400), (700, 300), (600, 300), fill="white", width=2, outline="black")


tk.mainloop()