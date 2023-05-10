#импорт библиотек
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import font
from datetime import datetime
from tkcalendar import Calendar

import pickle

# Константы

BG_WIND = ('#00FFFF')
BG_BUT = '#F0FFFF'

#закрытие приложения
def on_close():
  if messagebox.askokcancel("Выйти", "Хотите выйти?"):
    wind1.destroy()

#Создание окна
wind1 = tk.Tk()
wind1.protocol("WM_DELETE_WINDOW", on_close)
wind1.title('Личный помощник')
wind1.wm_attributes("-topmost", 1)
wind1.geometry("500x500")
wind1.configure(bg=BG_WIND)

#шрифты
my_font = font.Font(family="Arial", size=30, weight="bold")

frame = tk.Frame(wind1)
frame.pack(pady=10)


# Создание списка дел
list = tk.Listbox(frame, font=my_font, width=25, height=5, bg="SystemButtonFace", bd=0, fg="#0000CC",
               highlightthickness=0, selectbackground="#6699FF", activestyle="none")
list.pack(side=tk.LEFT, fill=tk.BOTH)

# Прокрутка
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

list.config(yscrollcommand=scrollbar.set, bg=BG_BUT)
scrollbar.config(command=list.yview)

# Поле ввода заметки
entry = tk.Entry(wind1, font=my_font, bg=BG_BUT)
entry.pack(pady=20)

button_frame = tk.Frame(wind1, bg=BG_WIND)
button_frame.pack(pady=20)

# Функция удаления записи
def delete_item():
    if len(list.curselection())==0:
        messagebox.showerror('ошибка', 'Вы не выбрали заметку ')
    else:
        list.delete(tk.ANCHOR)


# Функция добавления записи
def add_item():
    list.insert(tk.END, entry.get())
    entry.delete(0, tk.END)

# Функция вычеркивания записи
def cross_of_item():
    if len(list.curselection()) == 0:
        messagebox.showerror('ошибка', 'Вы не выбрали заметку ')
    else:
        list.itemconfig(list.curselection(), fg='#CCCCFF')
        list.select_clear(0, tk.END)

# Функция отмены зачеркивания записи
def uncross_item():
    if len(list.curselection()) == 0:
        messagebox.showerror('ошибка', 'Вы не выбрали заметку ')
    else:
        list.itemconfig(list.curselection(), fg='#0000CC')
        list.select_clear(0, tk.END)


# Функция удаления зачеркнутого
def delete_crossed():
    if list.size() == 0:
        messagebox.showerror('ошибка', 'Список дел пуст')
    else:
        cnt=0
        while cnt<list.size():
            if list.itemcget(cnt, "fg") == "#CCCCFF":
                list.delete(list.index(cnt))
            cnt += 1




# Создание кнопок
delete_button = tk.Button(button_frame, text="Удалить", command=delete_item, bg=BG_BUT)
add_button = tk.Button(button_frame, text="Добавить", command=add_item, bg=BG_BUT)
#add_button.grid(row=0, column=0)
#add_button.bind('<Button-1>', add_item)
cross_off_button = tk.Button(button_frame, text="Выполнено", command=cross_of_item, bg=BG_BUT)
uncross_button = tk.Button(button_frame, text="Невыполнено", command=uncross_item, bg=BG_BUT)
delete_crossed_button = tk.Button(button_frame, text="Удалить выполненное", command=delete_crossed, bg=BG_BUT)


# Расположение кнопок
add_button.grid(row=0, column=0)
delete_button.grid(row=0, column=1, padx=20)
cross_off_button.grid(row=0, column=2)
uncross_button.grid(row=0, column=3, padx=20)
delete_crossed_button.grid(row=0, column=4)


# Работа с календарем
# Получаем актуальную дату и время
actual_datetime = datetime.now()

# Функция создания календаря
def create_calendar():
    # Создаем новое окно
    wind2 = tk.Toplevel(wind1)
    wind2.title('Календарь')
    wind2.wm_attributes("-topmost", 1)
    wind2.geometry('400x400')
    wind2.configure(bg=BG_WIND)
    cal = Calendar(wind2, selectmode='day', year=actual_datetime.year, month=actual_datetime.month,
                   day=actual_datetime.day)
    cal.pack()

    # Выбор даты
    def take_date():
        date = cal.get_date()
        label.config(text=date,  bg=BG_WIND)


    label = tk.Label(wind2, text='', bg=BG_WIND)
    label.pack(pady=20)

    def note():
        wind3 = tk.Toplevel(wind1)
        wind3.title("")
        wind3.wm_attributes("-topmost", 1)
        wind3.geometry("500x500")
        wind3.configure(bg=BG_WIND)

        frame = tk.Frame(wind3)
        frame.pack(pady=10)

        # Создание списка дел
        list = tk.Listbox(frame, font=my_font, width=25, height=5, bg="SystemButtonFace", bd=0, fg="#0000CC",
                       highlightthickness=0, selectbackground="#6699FF", activestyle="none")
        list.pack(side=tk.LEFT, fill=tk.BOTH)

        # Прокрутка
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        list.config(yscrollcommand=scrollbar.set, bg=BG_BUT)
        scrollbar.config(command=list.yview)

        # Поле ввода заметки
        entry = tk.Entry(wind3, font=my_font, bg=BG_BUT)
        entry.pack(pady=20)

        button_frame = tk.Frame(wind3, bg=BG_WIND)
        button_frame.pack(pady=20)

        # Функция удаления записи
        def delete_item():
            if len(list.curselection()) == 0:
                messagebox.showerror('ошибка', 'Вы не выбрали заметку ')
            else:
                list.delete(tk.ANCHOR)

        # Функция добавления записи
        def add_item():
            list.insert(tk.END, entry.get())
            entry.delete(0, tk.END)

        # Функция вычеркивания записи
        def cross_of_item():
            if len(list.curselection()) == 0:
                messagebox.showerror('ошибка', 'Вы не выбрали заметку ')
            else:
                list.itemconfig(list.curselection(), fg='#CCCCFF')
                list.select_clear(0, tk.END)

        # Функция отмены зачеркивания записи
        def uncross_item():
            if len(list.curselection()) == 0:
                messagebox.showerror('ошибка', 'Вы не выбрали заметку ')
            else:
                list.itemconfig(list.curselection(), fg='#0000CC')
                list.select_clear(0, tk.END)

        # Функция удаления зачеркнутого
        def delete_crossed():
            if list.size() == 0:
                messagebox.showerror('ошибка', 'Список дел пуст')
            else:
                cnt = 0
                while cnt < list.size():
                    if list.itemcget(cnt, "fg") == "#CCCCFF":
                        list.delete(list.index(cnt))
                    cnt += 1

        # Создание кнопок
        delete_button = tk.Button(button_frame, text="Удалить", command=delete_item, bg=BG_BUT)
        add_button = tk.Button(button_frame, text="Добавить", command=add_item, bg=BG_BUT)
        cross_off_button = tk.Button(button_frame, text="Выполнено", command=cross_of_item, bg=BG_BUT)
        uncross_button = tk.Button(button_frame, text="Невыполнено", command=uncross_item, bg=BG_BUT)
        delete_crossed_button = tk.Button(button_frame, text="Удалить выполненное", command=delete_crossed, bg=BG_BUT)

        # Расположение кнопок
        add_button.grid(row=0, column=0)
        delete_button.grid(row=0, column=1, padx=20)
        cross_off_button.grid(row=0, column=2)
        uncross_button.grid(row=0, column=3, padx=20)
        delete_crossed_button.grid(row=0, column=4)

    def call_func():
        note()
        take_date()

    # Кнопка выбора даты
    take_date_button = tk.Button(wind2, text='Выбрать дату', command=call_func, bg=BG_BUT)
    take_date_button.pack(pady=20)


# Кнопка создания вкладки календаря
button_cal = tk.Button(wind1, text="Календарь",command=create_calendar, bg=BG_BUT)
button_cal.pack()

# Создание меню
my_menu = tk.Menu(wind1)
wind1.config(menu=my_menu)

# Функция сохранения файла
def save_file():
    file_name = filedialog.asksaveasfilename(initialdir="C:/", title="Save file",
                                             filetypes=(("Dat Files", "*.dat"),
                                             ("All Files", "*.*")))
    if file_name:
        if file_name.endswith(".dat"):
            pass
        else:
            file_name = f"{file_name}.dat"
    all_list = list.get(0, tk.END)

    output_file = open(file_name, 'wb')

    pickle.dump(all_list, output_file)

# Функция открытия файла
def open_file():
    file_name = filedialog.askopenfilename(initialdir="C:/Users/Sima", title="Open file",
                                             filetypes=(("Dat Files", "*.dat"),
                                             ("All Files", "*.*")))
    if file_name:
        list.delete(0, tk.END)

        input_file = open(file_name, 'rb')

    my_list = pickle.load(input_file)

    for i in my_list:
        list.insert(tk.END, i)

# Функция удаления файла
def delete_file():
    list.delete(0, tk.END)

file_menu = tk.Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='Файл', menu=file_menu)
file_menu.add_command(label='Сохранить файл', command=save_file)
file_menu.add_command(label='Открыть файл', command=open_file)
file_menu.add_command(label='Удалить расписание', command=delete_file)


wind1.mainloop()
