"""Требуется для своего варианта второй части л.р. №6 (усложненной программы) или ее объектно-ориентированной
реализации (л.р. №7) разработать реализацию с использованием графического интерфейса. Допускается использовать любую
графическую библиотеку питона. Рекомендуется использовать внутреннюю библиотеку питона tkinter.
В программе должны быть реализованы минимум одно окно ввода, одно окно вывода, текстовое поле, кнопка."""

from random import choice, randrange
from tkinter import messagebox
from tkinter import *
from tkinter import ttk


def product(*args, repeat=1):
    # если нет аргументов, возвращаем пустой список
    pools = list(map(tuple, args)) * repeat
    result = [[]]
    for pool in pools:
        result = [x + [y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)


class buying_laptops:
    def __init__(self, main):
        self.first_click = True

        self.main = main
        self.main_label = Label(main,
                                text='Усложнением будет являться качество производителя.\nЕсли качество производителя '
                                     'низкое, то данный\nпроизводитель не будет учитываться в рассмотрении его к'
                                     ' покупке.\nТак же у каждого компьютера есть своя стоимость.\nВывести вариант'
                                     ' покупки с максимальной суммарной стоимостью.')
        self.label1 = Label(text='\nВведите кол-во покупаемых компьютеров:')
        self.entry1 = ttk.Entry(width=30, justify='center')

        self.label2 = ttk.Label(text='Введите кол-во типов компьютеров:')
        self.entry2 = ttk.Entry(width=30, justify='center')

        self.main_button = ttk.Button(text='Рассчитать', command=self.result)

        self.main_label.pack()
        self.label1.pack()
        self.entry1.pack()
        self.label2.pack()
        self.entry2.pack()
        self.main_button.pack(expand=True)

    def result(self):
        self.combr = []
        self.maxstr = []
        self.exception = []
        self.purchases = []
        self.combinations = []
        self.maxs = self.cntcomps = self.cnttips = 0
        self.BRANDS = ['Apple', 'Asus', 'Dell', 'HP', 'Lenovo', 'Acer', 'MSI', 'Samsung']

        try:
            self.conditions = True
            self.cntcomps = int(self.entry1.get())
            self.cnttips = int(self.entry2.get())

            if self.cntcomps < 1 or self.cnttips < 1:
                messagebox.showwarning(title='Ошибка', message='Принимаются только положительные числа.')
                self.conditions = False

            if self.conditions:
                self.calculations()

                if self.first_click:
                    self.result_window()
                    self.first_click = False
                else:
                    self.conclusion.destroy()
                    self.purchases_window.destroy()
                    self.result_window()

        except ValueError:
            messagebox.showwarning(title='Ошибка', message='Введено не число.')

    def calculations(self):
        self.computers = [f'{choice(self.BRANDS)} ({randrange(10999, 99999, 1000)} р.)' for i in
                          range(1, self.cnttips + 1)]

        self.сomp1 = str(self.computers)[2:-1].replace("'", '')

        self.d = 0
        if len(self.computers) > 1:
            b = len(self.computers)
            while (b - len(self.computers)) <= (b // 2 - 1):
                r = choice(self.BRANDS)
                if r not in self.exception:
                    self.exception.append(r)

                for i, varu in enumerate(self.computers):
                    for j in self.exception:
                        if j in varu:
                            self.computers.pop(i)
            else:
                for i in self.exception:
                    self.d = f'{self.d}, {i}'

        else:
            while len(self.exception) < 3:
                r = choice(self.BRANDS)
                if r not in self.exception:
                    self.exception.append(r)

            for i, varu in enumerate(self.computers):
                for j in self.exception:
                    if j in varu:
                        self.computers.pop(i)
            for i in self.exception:
                self.d = f'{self.d} {i}'

        if self.computers:
            self.comp2 = str(self.computers)[2:-1].replace("'", '')
        else:
            messagebox.showwarning(title='Жаль', message='Сегодня мы осталисть без покупок.')

        for i, varu in enumerate(product(self.computers, repeat=self.cntcomps)):
            s = 0
            b = {}

            for j in sorted(varu):
                if j in b:
                    b[j] = b[j] + 1
                else:
                    b[j] = 1
                s += int(j[-9:-4])
            if b not in self.combr:
                self.combinations.append(varu)

            if s >= self.maxs:
                self.maxs = s
                self.maxstr = varu
            self.combr.append(b)

        self.purchases = []
        for i, varu in enumerate(sorted(self.combinations, key=len)):
            self.h = str(varu)[1:-2].replace("'", '').replace(', ', ' | ')
            self.purchases.append(f'{i + 1}. {self.h}')

        self.result = str(self.maxstr[::-1])[2:-2].replace("'", '').replace(', ', ' | ')

    def result_window(self):
        self.conclusion = Toplevel()
        self.conclusion.title('Вывод')
        self.conclusion.geometry('720x240')

        self.label5 = Label(self.conclusion, text=f'\nКомпьютеры в магазине:\n{self.сomp1}')
        self.label5.pack()

        self.label6 = Label(self.conclusion, text=f'\nНекачественные производители:\n{self.d[2::]}')
        self.label6.pack()

        self.label7 = Label(self.conclusion, text=f'\nКомпьютеры подлежащие выбору:\n {self.comp2}')
        self.label7.pack()

        self.label8 = Label(self.conclusion, text=f'\nВариант самой дорогой покупки:\n'
                                                  f'{self.result} - Сумма покупки: {self.maxs} руб.')
        self.label8.pack()

        self.purchases_window = Toplevel()
        self.purchases_window.title('Покупки')
        self.purchases_window.geometry('720x480')

        self.purchases_list = Listbox(self.purchases_window)
        self.purchases_list.pack(side='left', fill='both', expand=1)

        for i in self.purchases:
            self.purchases_list.insert('end', i)

        self.scrollbar = Scrollbar(self.purchases_window, command=self.purchases_list.yview)
        self.scrollbar.pack(side='right', fill='y')
        self.purchases_list.config(yscrollcommand=self.scrollbar.set)


root = Tk()
root.title('Лабораторная № 8')
root.geometry('720x320')
root.resizable(False, False)

buying_laptops(root)

root.mainloop()
