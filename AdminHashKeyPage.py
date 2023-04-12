import tkinter as tk
from tkinter import messagebox
from coreFunctions import store_key_hash


class AdminHashKeyPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.geometry("900x900")
        self.master.title("Admin Key Setup")

        self.label_key = tk.Label(self, text="Create the admin key(integer):", font=("Arial", 20))
        self.label_key.pack(padx=30, pady=10)

        self.key_txt = tk.Entry(self, width=30, font=("Arial", 20), show="*")
        self.key_txt.pack(padx=30, pady=10)

        self.submit_button = tk.Button(self, text="Submit", font=("Arial", 20), command=self.submit_admin_key)
        self.submit_button.pack(padx=30, pady=30)

        self.pack()

    def submit_admin_key(self):
        from SignUp import SignUp

        admin_key = self.key_txt.get()
        if admin_key:
            store_key_hash("admin_key_hash.txt", admin_key)
            messagebox.showinfo(title="Success", message="Admin key saved successfully.")
            self.switch_frame(SignUp)
        else:
            messagebox.showerror(title="Error", message="Admin key cannot be empty.")

    def switch_frame(self, frame_class):
        new_frame = frame_class(self.master)
        self.destroy()
        new_frame.pack()
