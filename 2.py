import tkinter as tk
window = tk.Tk()
window.geometry("190x50")

tk.Label(text="                          ", foreground="black").grid(row=0, column=1)

def sinister():
    a = "Левый"
    tk.Label(text="                          ", foreground="black").grid(row=0, column=1)
    tk.Label(text=a, foreground="black").grid(row=0, column=1)

def dexter():
    a = "Правый"
    tk.Label(text="                          ", foreground="black").grid(row=0, column=1)
    tk.Label(text=a, foreground="black").grid(row=0, column=1)

def medium():
    a = "Центральный"
    tk.Label(text="                          ", foreground="black").grid(row=0, column=1)
    tk.Label(text=a, foreground="black").grid(row=0, column=1)

tk.Button(text="sinister", command=sinister).grid(row=2, column=0, stick='wens')
tk.Button(text="dexter", command=dexter).grid(row=2, column=1, stick='wens')
tk.Button(text="medium", command=medium).grid(row=2, column=2, stick='wens')

window.mainloop()