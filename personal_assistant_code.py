import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from datetime import datetime
from tkcalendar import Calendar
import notes

# Константы
BG_WIND = '#00FFFF'
BG_BUT = '#F0FFFF'
lst_notes={}

#закрытие приложения
def on_close():
  if messagebox.askokcancel("Выйти?", "Хотите выйти?"):
    wind1.destroy()

def on_change_date():
  global lst_notes
  lst.delete(0, tk.END)
  curr_date = cal.get_date()
  ind = 1
  for i in notes.note_dict.keys():
    if notes.note_dict[i]['date'] == curr_date:
      lst.insert(ind, notes.note_dict[i]['text'])
      lst_notes[ind] = i
      ind += 1


#Создание окна
wind1 = tk.Tk()
wind1.protocol("WM_DELETE_WINDOW", on_close)
wind1.title('Личный помощник')
wind1.wm_attributes("-topmost", 1)
wind1.geometry("800x800")
wind1.configure(bg=BG_WIND)

frame1 = tk.Frame(wind1, relief=tk.SOLID, height=50, borderwidth=1)
frame1.pack(anchor='s', fill=tk.X, side=tk.BOTTOM)

frame2 = tk.Frame(wind1, relief=tk.SOLID, borderwidth=1)
frame2.pack(anchor='n', fill=tk.BOTH, side=tk.TOP, expand=True)

actual_datetime = datetime.now()
cal = Calendar(frame2, selectmode='day', year=actual_datetime.year, month=actual_datetime.month,
                   day=actual_datetime.day, date_pattern='yyyy-mm-dd')
cal.pack(anchor='w', fill=tk.Y, side=tk.LEFT)

cal.bind("<<CalendarSelected>>", lambda x: on_change_date())

# Прокрутка
scrollbar = tk.Scrollbar(frame2)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

# Создание списка дел
lst = tk.Listbox(frame2, bg="SystemButtonFace", bd=0, fg="#0000CC",
               highlightthickness=0, selectbackground="#6699FF", activestyle="none")
lst.pack(anchor='e', fill=tk.BOTH, side=tk.RIGHT, expand=True)
lst.config(yscrollcommand=scrollbar.set, bg=BG_BUT)
scrollbar.config(command=lst.yview)

if __name__=='__main__':
  notes.read_note_dict('C:\\temp\\1.json')
  print(notes.note_counter)
  print(notes.note_dict)
  print(notes.note_dict.values())
  for i in notes.note_dict.values():
    a = datetime.strptime(i['date'], '%Y-%m-%d')
    print(a, type(a))


  wind1.mainloop()
