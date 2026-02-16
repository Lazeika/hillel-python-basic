import tkinter as tk
import math
from tkinter import messagebox

def ask_name():
    input_window = tk.Toplevel(root)
    input_window.title("Введи своє ім'я")

    width = 600
    height = 300
    screen_width = input_window.winfo_screenwidth()
    screen_height = input_window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    input_window.geometry(f"{width}x{height}+{x}+{y}")

    # Дозволяю зміну розміру (щоб працював fullscreen)
    input_window.resizable(True, True)

    # Надпис
    label = tk.Label(input_window, text="Введи свій приклад:", font=("Arial", 14))
    label.pack(pady=20)

    # Поле вводу
    name_entry = tk.Entry(input_window, font=("Arial", 14))
    name_entry.pack(pady=10)
    name_entry.focus()

    def submit_name(event=None):
        name = name_entry.get()
        if name.strip() == "":
            return
        messagebox.showinfo("Результат", f"Радий познайомитись, {name}!")
        input_window.destroy()
        root.destroy()

    submit_btn = tk.Button(input_window, text="OK", font=("Arial", 12), command=submit_name)
    submit_btn.pack(pady=20)

    input_window.bind("<Return>", submit_name)

    # F11 - переключити fullscreen
    def toggle_fullscreen(event=None):
        input_window.attributes("-fullscreen", not input_window.attributes("-fullscreen"))
    input_window.bind("<F11>", toggle_fullscreen)

# Головне вікно
root = tk.Tk()
root.withdraw()
ask_name()
root.mainloop()
