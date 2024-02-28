from tkinter import *

class PageTurner:
    def __init__(self, root):
        self.root = root
        self.frame = Frame(self.root)
        self.frame.pack()

        # Создание страниц
        self.pages = [
            "Привет!",
            "Пока!",
        ]

        # Создание кнопок со стрелками
        self.left_arrow = Button(self.frame, text="<<", command=self.go_left)
        self.left_arrow.pack(side=LEFT)

        self.right_arrow = Button(self.frame, text=">>", command=self.go_right)
        self.right_arrow.pack(side=RIGHT)

        # Переменная для текущей страницы
        self.current_page = 0

        # Отображение первой страницы
        self.show_page(self.current_page)

    # Функция для перехода на previous page
    def go_left(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.show_page(self.current_page)

    # Функция для перехода на next page
    def go_right(self):
        if self.current_page < len(self.pages) - 1:
            self.current_page += 1
            self.show_page(self.current_page)

    # Функция для отображения страницы
    def show_page(self, page_number):
        # Очистка области отображения
        for widget in self.frame.winfo_children():
            if widget != self.left_arrow and widget != self.right_arrow:
                widget.destroy()

        # Отображение текста страницы
        label = Label(self.frame, text=self.pages[page_number], font=("Arial", 20))
        label.pack()


root = Tk()
page_turner = PageTurner(root)
root.mainloop()
