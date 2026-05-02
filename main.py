import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime

DATA_FILE = "data/trainings.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def add_training():
    date = entry_date.get()
    tr_type = entry_type.get()
    duration = entry_duration.get()

    # Проверка корректности ввода
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        messagebox.showerror("Ошибка", "Дата должна быть в формате ГГГГ-ММ-ДД")
        return

    try:
        duration = float(duration)
        if duration <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Ошибка", "Длительность должна быть положительным числом")
        return

    data = load_data()
    data.append({"date": date, "type": tr_type, "duration": duration})
    save_data(data)
    update_table()

def filter_trainings():
    selected_type = combo_filter_type.get()
    selected_date = combo_filter_date.get()
    data = load_data()
    filtered = data

    if selected_type != "Все":
        filtered = [x for x in filtered if x["type"] == selected_type]
    if selected_date != "Все":Вот пошаговая инструкция по созданию GUI-приложения **«Training Planner»** для планирования тренировок с фильтрацией, сохранением данных в **JSON** и использованием **Git**.

---

### 1. Структура проекта
