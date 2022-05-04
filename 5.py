import tkinter as tk
window = tk.Tk()
window.geometry("300x100")

def calc():
    buffer_price = int(price.get())

    a_result = buffer_price * 60 / 100
    b_result = 0.75 * a_result / 100


    return(tk.Label(text=a_result, fg="black").grid(row=1, column=1), tk.Label(text=b_result).grid(row=2, column=1))

tk.Label(text="Введите стоимость имущества: $", fg="black").grid(row=0, column=0)
price = tk.Entry(window)
price.grid(row=0, column=1)

tk.Label(text="Оценочная стоимость: $", fg="black").grid(row=1, column=0)
tk.Label(text="Налог на имущество: $", fg="black").grid(row=2, column=0)

tk.Button(text="Вычислить", command=calc).grid(row=3, column=0)
tk.Button(text="Выйти", command=window.destroy).grid(row=3, column=1)

window.mainloop()