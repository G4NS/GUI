import tkinter as tk

class infoGUI:
    def __init__(self):
        self.window = tk.Tk() #Открываем окно

        self.info_frame = tk.Frame(self.window) #Задаем рамку
        self.button_frame = tk.Frame(self.window)

        self.info_button = tk.Button(text="Показать инфо", command=self.print_info) #в рамке объявляем кнопку который при нажатии переходит в функцию
        self.quit_button = tk.Button(text="Выйти", command=self.window.destroy) #Кнопка для закрывание

        self.info_button.place(x=40, y =70) #Даем координаты кнопке
        self.quit_button.place(x=300, y=70)

        self.info_frame.pack() #Пакуем рамку
        self.button_frame.pack()

        self.window.geometry('400x120') #Задаем своии размеры окна
        self.window.mainloop()

    def print_info(self):
        self.info = "081156, Казахстан. Жамбылская область, \nг. Чу,\nПочта Граф Графа"
        Label = tk.Label(text=self.info, foreground="black") #Печатаем
        Label.pack(side="top")

infoGUI =infoGUI()