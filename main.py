from tkinter import *
import tkinter as tk
import random

root = Tk()
mass = []
k = ["V1", "V2", "V3", "V4", "V5"]
krd = [["55", "135"], ["145", "55"], ["265", "55"], ["355", "135"], ["210", "235"]]
vag = [[999, 999, 999, 999, 999], [999, 999, 999, 999, 999], [999, 999, 999, 999, 999], [999, 999, 999, 999, 999],
       [999, 999, 999, 999, 999]]
Li = [[0, 0, 0, 0, 0], [999, 0, 0, 0, 0], [999, 0, 0, 0, 0], [999, 0, 0, 0, 0], [999, 0, 0, 0, 0]]


class mainwindow:
    def __init__(self, main):
        self.F1 = 1
        self.F2 = 1
        self.c = Canvas(main, width=400, height=400, bg="blue")
        self.c.grid(rowspan=10, column=1)
        self.Label1 = Label(main, text="Створення графа", font=15)
        self.Label1.grid(row=0, column=0)
        self.Entry1 = Entry(main)
        self.Entry1.grid(row=4, column=0)
        self.Label4 = Label(main, text="Задати вагу", font=15)
        self.Label4.grid(row=3, column=0)
        self.Label2 = Label(main, text="Вибрана вершина 1:", font=15)
        self.Label3 = Label(main, text="Вибрана вершина 2:", font=15)
        self.Label2.grid(row=6, column=0)
        self.Label3.grid(row=7, column=0)
        self.listbox1 = Listbox(main)
        self.listbox1.grid(row=1, column=0)
        for i in k:
            self.listbox1.insert(END, i)
        self.But1 = Button(main, text="Вибрати вершину", font=15)
        self.But1.grid(row=2, column=0)
        self.But2 = Button(main, text="З'єднати вершини")
        self.But2.grid(row=5, column=0)
        self.c.create_oval(40, 120, 70, 150, outline="Black", width=2, fill="red")
        self.c.create_text(30, 110, text="V1", font=15)
        self.c.create_oval(130, 40, 160, 70, outline="Black", width=2, fill="red")
        self.c.create_text(130, 20, text="V2", font=15)
        self.c.create_oval(250, 40, 280, 70, outline="Black", width=2, fill="red")
        self.c.create_text(250, 20, text="V3", font=15)
        self.c.create_oval(340, 120, 370, 150, outline="Black", width=2, fill="red")
        self.c.create_text(385, 150, text="V4", font=15)
        self.c.create_oval(195, 220, 225, 250, outline="Black", width=2, fill="red")
        self.c.create_text(210, 275, text="V5", font=15)
        self.But1.bind("<Button-1>", self.func1)
        self.But2.bind("<Button-1>", self.func2)
        self.But3 = Button(main, text="Показати шлях", font=15)
        self.But4 = Button(main, text="Розрахувати найкоротший шлях", font=15)
        self.Lab5 = Label(main, text="Обрахування найкоротшого шляху", font=15)
        self.Lab5.grid(row=8, column=0)
        self.But3.grid(row=9, column=0)
        self.But4.grid(row=10, column=0)
        self.But5 = Button(main, text="Показати матрицю ваг")
        self.But5.grid(row=0, column=2)
        self.But5.bind("<Button-1>", self.show)
        self.Labshow = Label(main, text='', font=15, fg="red")
        self.Labshow.grid(row=1, column=2)
        self.But4.bind("<Button-1>", self.shlax)
        self.But3.bind("<Button-1>", self.final)
        self.But6 = Button(main, text="Задати випадково", font=15)
        self.But6.grid(row=10, column=1)
        self.But6.bind("<Button-1>", self.rand)

    def rand(self, event):
        for i in range(5):
            for j in range(5):
                if random.randint(1, 4) == 2:
                    vag[i][j] = random.randint(-20, 20)
                    xz1 = int(krd[i][0])
                    yz1 = int(krd[i][1])
                    xz2 = int(krd[j][0])
                    yz2 = int(krd[j][1])
                    self.c.create_line(xz1, yz1, xz2, yz2, arrow=tk.LAST)
                    self.c.create_text(((xz1 + xz2) / 2) + 5, ((yz1 + yz2) / 2) + 5, text=str(vag[i][j]), font=15)

    def final(self, event):
        g = len(mass)
        print(mass)
        if mass[-1] == 0:
            for i in range(1, g):
                xl1 = krd[mass[i]][0]
                yl1 = krd[mass[i]][1]
                xl2 = krd[mass[i - 1]][0]
                yl2 = krd[mass[i - 1]][1]
                self.c.create_line(xl1, yl1, xl2, yl2, arrow=tk.LAST, fill="violet")
        else:
            self.Labshow["text"] = "Шляху не існує"

    def func1(self, event):
        if self.F1 == 1:
            self.F1 = str(self.listbox1.curselection())
            self.F1 = self.F1.replace(",", "")
            self.F1 = self.F1.replace("(", "")
            self.F1 = self.F1.replace(")", "")
            self.Label2['text'] = 'Вибрана вершина 1: ' + k[int(self.F1)]
        elif self.F2 == 1:
            self.F2 = str(self.listbox1.curselection())
            self.F2 = self.F2.replace(",", "")
            self.F2 = self.F2.replace("(", "")
            self.F2 = self.F2.replace(")", "")
            self.Label3['text'] = 'Вибрана вершина 2: ' + k[int(self.F2)]

    def func2(self, event):
        self.x1 = int(krd[int(self.F1)][0])
        self.y1 = int(krd[int(self.F1)][1])
        self.x2 = int(krd[int(self.F2)][0])
        self.y2 = int(krd[int(self.F2)][1])
        self.c.create_line(self.x1, self.y1, self.x2, self.y2, arrow=tk.LAST)
        self.vsvag = self.Entry1.get()
        vag[int(self.F1)][int(self.F2)] = int(self.vsvag)
        self.c.create_text(((self.x1 + self.x2) / 2), (((self.y1 + self.y2) / 2) - 15), text=self.vsvag, font=15)
        self.F1 = 1
        self.F2 = 1
        self.Label2['text'] = 'Вибрана вершина 1:'
        self.Label3['text'] = 'Вибрана вершина 2:'

    def show(self, event):
        self.h = ''
        for i in range(5):
            for j in range(5):
                self.h += str(vag[i][j]) + " "
                if len(str(vag[i][j])) < 3:
                    self.h += " "
            self.h += '\n'
        self.Labshow['text'] = self.h

    def shlax(self, event):
        for i in range(1, 5):
            for j in range(1, 5):
                J = []
                for j1 in range(5):
                    J.append((Li[j1][i - 1] + vag[j1][j]))
                Li[j][i] = min(J)

        self.h1 = ''
        for i in range(5):
            for j in range(5):
                self.h1 += str(Li[i][j]) + " "
                if len(str(Li[i][j])) < 3:
                    self.h1 += " "
            self.h1 += '\n'
        print(self.h1)

        self.Fn = str(self.listbox1.curselection())
        self.Fn = self.Fn.replace(",", "")
        self.Fn = self.Fn.replace("(", "")
        self.Fn = self.Fn.replace(")", "")
        self.Fn = int(self.Fn)  # номер вершини у масиві
        n = 5
        mass.append(self.Fn)
        self.kill = 0
        while (self.Fn != 0):
            if self.kill > 15:
                break
            Pr = []  # прообрази вершини(їхні номери якщо точніше)
            for i in range(5):
                if vag[i][self.Fn] < 500:
                    Pr.append(i)
                    print(str(i) + " елемент прообраз вершини " + str(self.Fn))
            for i in Pr:
                if Li[i][3] + vag[i][self.Fn] == Li[self.Fn][4]:
                    mass.append(i)
                    print(Pr)
                    print("умова виконалась для r= " + str(i))
                    self.Fn = i
                    self.xf1 = krd[i][0]
                    self.yf1 = krd[i][1]
                    self.xf2 = krd[self.Fn][0]
                    self.yf2 = krd[self.Fn][1]
                    self.c.create_line(int(self.xf1), int(self.yf1), int(self.xf2), int(self.yf2), arrow=tk.LAST,
                                       fill="red", width=5)
                    self.c.create_text(int(self.xf1 + self.xf2) / 2, int(self.yf1 + self.yf2) / 2, text="Єсть", font=15)
            print("End")
            print(self.Fn)
            self.kill += 1


q = mainwindow(root)
root.mainloop()
