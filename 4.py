import tkinter as tk
window = tk.Tk()
window.geometry("350x100")

def calc():
    buffer_c = int(c.get())
    result = 9 * buffer_c / 5 + 32
    return(tk.Label(text=result, fg="black").grid(row=1, column=1))

tk.Label(text="Введите температуру в градусах Цельсия: ", fg="black").grid(row=0, column=0)
c = tk.Entry(window)
c.grid(row=0, column=1)


tk.Label(text= "Температура по шкале Фаренгейта:", fg="black").grid(row=1, column=0)

tk.Button(text="Преобразовать в градусы Фаренгейта", command=calc).grid(row=2, column=0)
tk.Button(text="Выйти", command=window.destroy).grid(row=2, column=1)

window.mainloop()