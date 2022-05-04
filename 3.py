import tkinter as tk
window = tk.Tk()
window.geometry("300x100")

def calc():
    buffer_gallon = int(gallon.get())
    buffer_miles = int(miles.get())
    result = buffer_miles / buffer_gallon
    return(tk.Label(text=result, fg="black").grid(row=2, column=1))

tk.Label(text="Введите количество галлонов:", fg="black").grid(row=0, column=0)
gallon = tk.Entry(window)
gallon.grid(row=0, column=1)

tk.Label(text="Введите количество миль:", fg="black").grid(row=1, column=0)
miles = tk.Entry()
miles.grid(row=1, column=1)

tk.Label(text="Мили на галлон (MPG) = ", fg="black").grid(row=2, column=0)

tk.Button(text="Вычислить MPG", command=calc).grid(row=3, column=0)
tk.Button(text="Выйти", command=window.destroy).grid(row=3, column=1)

window.mainloop()