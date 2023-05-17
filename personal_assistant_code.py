import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from datetime import datetime
from tkinter import simpledialog

import add_note_wind
from tkcalendar import Calendar
import notes

# Константы и переменные
BG_WIND = "#00FFFF"
BG_BUT = "#F0FFFF"
lst_notes={}

#закрытие приложения
def on_close():
  if messagebox.askokcancel("Выйти?", "Хотите выйти?"):
    notes.write_note_dict("notes.json")
    application_window.destroy()

def on_change_date():
  update_note_list()
  update_calendar()

# Функция обновления списка
def update_note_list():
  global lst_notes
  lst.delete(0, tk.END)
  curr_date = cal.get_date()
  ind = 0
  for i in notes.note_dict.keys():
    if notes.note_dict[i]["date"] == curr_date:
      lst.insert(ind, notes.note_dict[i]["text"])
      if notes.note_dict[i]["state"] == "done":
        lst.itemconfig(ind, fg='#CCCCFF')
      lst_notes[ind] = i
      ind += 1

# Функция обновления календаря
def update_calendar():
  cal.calevent_remove("all")
  for i in notes.note_dict.values():
    if i["state"] == "new":
      cal.calevent_create(datetime.strptime(i['date'], "%Y-%m-%d"), "+", "new")

# Функция добавления заметки
def add_cmd():
  answer = simpledialog.askstring("Добавить", "Введите заметку:",
                                  parent=application_window)
  if answer is not None:
    notes.add_note(cal.get_date(), answer)
    update_note_list()

# Функция выполнения заметки
def cross_note():
  notes.note_dict[lst_notes[lst.curselection()[0]]]['state'] = "done"
  update_note_list()
  update_calendar()

# Функция отмены выполнения заметки
def uncross_note():
  notes.note_dict[lst_notes[lst.curselection()[0]]]['state'] = "new"
  update_note_list()
  update_calendar()



if __name__=="__main__":
  # Создание окна
  application_window = tk.Tk()
  application_window.protocol("WM_DELETE_WINDOW", on_close)
  application_window.title("Личный помощник")
  #application_window.wm_attributes("-topmost", 1)
  application_window.geometry("800x800")
  application_window.configure(bg=BG_WIND)

  button_frame = tk.Frame(application_window, relief=tk.SOLID, height=50, borderwidth=1)
  button_frame.pack(anchor="s", fill=tk.X, side=tk.BOTTOM)

  cal_frame = tk.Frame(application_window, relief=tk.SOLID, borderwidth=1)
  cal_frame.pack(anchor="n", fill=tk.BOTH, side=tk.TOP, expand=True)

  actual_datetime = datetime.now()
  cal = Calendar(cal_frame, selectmode="day", year=actual_datetime.year, month=actual_datetime.month,
                 day=actual_datetime.day, date_pattern="yyyy-mm-dd")

  cal.pack(anchor="w", fill=tk.Y, side=tk.LEFT)

  cal.bind("<<CalendarSelected>>", lambda x: on_change_date())
  cal.tag_config('new',background='red', foreground='yellow')

  # Прокрутка
  scrollbar = tk.Scrollbar(cal_frame)
  scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

  # Создание списка дел
  lst = tk.Listbox(cal_frame, bg="SystemButtonFace", bd=0, fg="#0000CC",
                   highlightthickness=0, selectbackground="#6699FF", activestyle="none", font="TkHeadingFont")
  lst.pack(anchor="e", fill=tk.BOTH, side=tk.RIGHT, expand=True)
  lst.config(yscrollcommand=scrollbar.set, bg=BG_BUT)
  scrollbar.config(command=lst.yview)

  # Создание кнопок
  add_button = tk.Button(button_frame, text="Добавить", command=add_cmd)
  add_button.pack(anchor="se")
  cross_button = tk.Button(button_frame, text="Выполнено", command=cross_note)
  cross_button.pack(anchor="se")
  uncross_button = tk.Button(button_frame, text="Отменить выполнение", command=uncross_note)
  uncross_button.pack(anchor="se")

  notes.read_note_dict("notes.json")
  update_note_list()
  update_calendar()

  application_window.mainloop()
