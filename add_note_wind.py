# Импорт библиотек
import tkinter as tk
import notes


# Функция отмены добавления заметки
def cancel_cmd():
    global note_wind
    note_wind.destroy()

# Функция созранения заметки
def ok_cmd():
    global note_wind
    notes.add_note(note_date, editor.get("1.0", "end"))
    note_wind.destroy()

# Функция сохранения заметки
def add_note_window(d: str):
    global note_wind, editor, note_date
    note_date = d
    note_wind = tk.Tk()
    #note_wind.protocol("WM_DELETE_WINDOW", on_close)
    note_wind.title("Новая заметка")
    note_wind.geometry("800x800")
    note_wind.configure()


    # Область для кнопок
    button_frame = tk.Frame(note_wind, relief=tk.SOLID, height=50, borderwidth=1)
    button_frame.pack(anchor="s", fill=tk.X, side=tk.BOTTOM)

    # Область для ввода текста
    text_frame = tk.Frame(note_wind, relief=tk.SOLID, borderwidth=1)
    text_frame.pack(anchor="n", fill=tk.BOTH, side=tk.TOP, expand=True)

    # Создание кнопок и их расположение
    cancel_button = tk.Button(button_frame, text="Отмена", command=cancel_cmd)
    ok_button = tk.Button(button_frame, text="ОК", command=ok_cmd)
    cancel_button.grid(row=0, column=0)
    ok_button.grid(row=0, column=1, padx=20)

    # Полоса прокрутки
    scrollbar = tk.Scrollbar(text_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

    # Создание списка дел
    editor = tk.Text(text_frame)
    editor.pack(fill=tk.BOTH, expand=1)
    #lst.pack(anchor="e", fill=tk.BOTH, side=tk.RIGHT, expand=True)
    editor.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=editor.yview)

if __name__=="__main__":
    add_note_window()
