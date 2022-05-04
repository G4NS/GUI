#не работает


import tkinter as tk

class trans:
    def __init__(self):
        self.window = tk.Tk()

        self.trans_frame = tk.Frame(self.window)
        self.buttons_frame = tk.Frame(self.window)

        self.btn_sinister = tk.Button(text="sinister", command=self.sinister)
        self.btn_dexter = tk.Button(text="dexter", command=self.dexter)
        self.btn_medium = tk.Button(text="medium", command=self.medium)

        self.btn_sinister.pack(side="left")
        self.btn_dexter.pack(side="left")
        self.btn_medium.pack(side="left")

        self.trans_frame.pack()
        self.buttons_frame.pack()

        #self.window.geometry('400x120') #Задаем своии размеры окна
        self.window.mainloop()

    def sinister(self):
        self.a = "Левый"
        Label = tk.Label(text=self.a, foreground="black", bg="white")
        Label.pack(side="top")

    def dexter(self):
        self.a = "Правый"
        Label = tk.Label(text=self.a, foreground="black")
        Label.pack(side="top")

    def medium(self):
        self.a = "Центральный"
        Label = tk.Label(text=self.a, foreground="black")
        Label.pack(side="top")


#trans = trans()




window = tk.Tk()
window.geometry("300x100")

tk.Button(text="sinister").grind(row=1, column=0)


window.mainloop()