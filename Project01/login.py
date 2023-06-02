import tkinter as tk
from tkinter import ttk, messagebox
import csv



class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Вход")
        self.geometry("400x250")
        self.resizable(False, False)

        self.label_username = ttk.Label(self, text="Имя пользователя")
        self.label_password = ttk.Label(self, text="Пароль")

        self.username_entry = ttk.Entry(self, width=30)
        self.password_entry = ttk.Entry(self, width=30, show="*")

        self.button_login = ttk.Button(self, text="Войти", command=self.check_password)
        self.button_cancel = ttk.Button(self, text="Отмена", command=self.destroy)

        self.label_username.pack(side=tk.TOP, pady=(10, 0))
        self.username_entry.pack(side=tk.TOP, padx=10, pady=5)
        self.label_password.pack(side=tk.TOP, pady=(5, 0))
        self.password_entry.pack(side=tk.TOP, padx=10, pady=5)
        self.button_login.pack(side=tk.LEFT, padx=10, pady=10)
        self.button_cancel.pack(side=tk.RIGHT, padx=10, pady=10)

    def check_password(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        registered_users = {}
        with open("users.csv", "r", newline="") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                registered_users[row[0]] = row[1]

        if username in registered_users and registered_users[username] == password:
            messagebox.showinfo("Успех", "Добро пожаловать, {}".format(username))
            self.quit()
        else:
            messagebox.showinfo("Ошибка", "Неправильное имя пользователя или парооль")

def run_login_window():
    login_window = LoginWindow()
    login_window.mainloop()
