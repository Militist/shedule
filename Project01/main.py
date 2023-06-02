import tkinter as tk
from tkinter import ttk
from register import run_register_window, RegisterWindow
from login import run_login_window



def main():
    root = tk.Tk()
    root.title("Главное окно")
    root.geometry("250x250")

    label = ttk.Label(root, text="Добро пожаловать!")
    label.pack(pady=10)

    # register_button = ttk.Button(root, text="Зарегистрироваться", command=run_register_window)
    register_button = ttk.Button(root, text="Зарегистрироваться", command=lambda: RegisterWindow(root))
    login_button = ttk.Button(root, text="Войти", command=run_login_window)

    register_button.pack(side=tk.LEFT, padx=10, pady=10)
    login_button.pack(side=tk.RIGHT, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
