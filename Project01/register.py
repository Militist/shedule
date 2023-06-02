import tkinter as tk
from tkinter import ttk, messagebox
import csv


class RegisterWindow(tk.Toplevel):
    # def __init__(self, master):
    #     super().__init__(master)
    #     self.title("Регистрация нового пользователя")
    #     self.geometry("400x150")
    #     self.resizable(False, False)
    #
    #     self.label_username = ttk.Label(self, text="Имя пользователя")
    #     self.label_password = ttk.Label(self, text="Пароль")
    #
    #     self.username_entry = ttk.Entry(self, width=30)
    #     self.password_entry = ttk.Entry(self, width=30, show="*")
    #
    #     self.button_register = ttk.Button(self, text="Зарегистрировать", command=self.register)
    #     self.button_cancel = ttk.Button(self, text="Отмена", command=self.destroy)
    #
    #     self.label_username.pack(side=tk.TOP, pady=(10, 0))
    #     self.username_entry.pack(side=tk.TOP, padx=10, pady=5)
    #     self.label_password.pack(side=tk.TOP, pady=(5, 0))
    #     self.password_entry.pack(side=tk.TOP, padx=10, pady=5)
    #     self.button_register.pack(side=tk.LEFT, padx=10, pady=10)
    #     self.button_cancel.pack(side=tk.RIGHT, padx=10, pady=10)

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.top = tk.Toplevel(self.parent)
        self.top.title("Регистрация")
        self.top.geometry("400x250")

        self.label_username = ttk.Label(self.top, text="Имя пользователя")
        self.label_password = ttk.Label(self.top, text="Пароль")

        self.entry_username = ttk.Entry(self.top)
        self.entry_password = ttk.Entry(self.top, show="*")

        self.label_username.grid(row=0, column=0, padx=5, pady=5)
        self.label_password.grid(row=1, column=0, padx=5, pady=5)
        self.entry_username.grid(row=0, column=1, padx=5, pady=5)
        self.entry_password.grid(row=1, column=1, padx=5, pady=5)

        self.button_register = ttk.Button(self.top, text="Зарегистрироваться", command=self.register)
        self.button_register.grid(row=2, column=1, padx=5, pady=5)

    def register(self, **kwargs):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if not username or not password:
            tk.messagebox.showinfo("Ошибка", "Не заполнены все поля")
            return

        with open("users.csv", "r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["username"] == username:
                    tk.messagebox.showinfo("Ошибка", "Пользователь с таким именем ужже существует")
                    return
                elif row["password"] == password:
                    tk.messagebox.showinfo("Ошибка", "Пользовательь с таким паролем уже существует")
                    return
                elif row["username"] == username and row["password"] == password:
                    tk.messagebox.showinfo("Ошибка", "Пользователь с таким именем и паролем ужже существует")
                    return

        with open("users.csv", "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([username, password])
        tk.messagebox.showinfo("Успех", "Новый пользователь зарегистрирован")

def run_register_window():
    root = tk.Tk()
    root.withdraw()
    register_window = RegisterWindow(root)
    register_window.mainloop()
