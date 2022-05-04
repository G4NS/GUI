from tkinter import *

tk = Tk()

c = Canvas(tk, width=835, height=220, bg="white")
c.pack()

c.create_oval(20, 20, 200, 200, width=2)
c.create_text(110, 210, text="Солнце")

c.create_oval(210,90, 250, 130,  width=2, fill="#c8c7c8")
c.create_text(230, 140, text="Меркурий")

c.create_oval(260,80, 320, 140,  width=2, fill="#e1e1e1")
c.create_text(290, 150, text="Венера")

c.create_oval(330,90, 370, 130,  width=2, fill="#2f2f2f")
c.create_text(349, 140, text="Земля")

c.create_oval(380,95, 410, 125,  width=2, fill="#4a4a4a")
c.create_text(395, 135, text="Марс")

c.create_oval(420,60, 510, 150,  width=2, fill="#747474")
c.create_text(465, 160, text="Юпитер")

c.create_oval(515,80, 635, 130,  width=2)
c.create_oval(530,60, 620, 150,  width=2, fill="white")
c.create_text(575, 160, text="Сатурн")

c.create_oval(640,70, 715, 145,  width=2, fill="#b4b4b4")
c.create_text(675, 155, text="Уран")

c.create_oval(725,80, 785, 140,  width=2, fill="#e2e2e2")
c.create_text(755, 150, text="Нептун")

c.create_oval(795,100, 815, 120,  width=2, fill="#848484")
c.create_text(805, 130, text="Плутон")

tk.mainloop()