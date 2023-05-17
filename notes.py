# Импорт библиотек
from datetime import datetime, date, time
import json
import notes
import os.path

#Объявление переменных
note_dict = {}
note_counter = 1

# Функция добавления заметки
def add_note(d: str, text: str):
    global note_counter
    note_counter = note_counter + 1
    note_dict[str(note_counter)] = {"date": d, "text": text, "state": "new"}


# Сохранение заметки в памяти
def write_note_dict(file_name: str):
    output_file = open(file_name, "w+")
    json.dump(note_dict, output_file, default=str)
    output_file.close()

# Чтение заметки из памяти
def read_note_dict(file_name: str):
    global note_dict, note_counter
    if os.path.isfile(file_name):
        input_file = open(file_name, "r")
        note_dict = json.load(input_file)
        input_file.close()
        keys = [int(key) for key in note_dict]
        if len(keys) == 0:
            note_counter =1
        else:
            note_counter = max(keys)
    else:
        note_dict = {}
        note_counter = 1
