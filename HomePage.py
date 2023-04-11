import tkinter as tk
from tkinter import messagebox
from coreFunctions import *


class HomePage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.geometry("900x900")
        self.master.title("Home Page")
        self.scrollbar=tk.Scrollbar(self)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.label_key = tk.Label(self, text="Enter the key:", font=("Arial", 20))
        self.label_key.pack(padx=30, pady=10)

        self.ketTXT = tk.Entry(self, width=30, background="Blue", font=("Arial", 20))
        self.ketTXT.pack(padx=30, pady=10)

        self.button_decrypt = tk.Button(self, text="Decrypt", command=self.decrypt_stuff)
        self.button_decrypt.pack(padx=30, pady=10)

        self.label = tk.Label(self, text="Field for your super secretive passwords and stuff yk!", font=("Arial", 25))
        self.label.pack(padx=30, pady=10)

        self.userText = tk.Text(self, height=10, width=30, font=("Arial", 20))
        self.userText.pack(padx=30, pady=10)

        self.button1 = tk.Button(self, text="Save", command=self.saveStuff)
        self.button2 = tk.Button(self, text="Logout", command=self.logout)
        self.button1.pack(padx=30, pady=10)
        self.button2.pack(padx=30, pady=10)

        self.pack()


    def set_adminKEY(self, adminKEY):
        self.adminKEY = adminKEY

    



    def logout(self):
        from LoginPage import LoginPage
        self.switch_frame(LoginPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self.master)
        self.destroy()
        new_frame.pack()

    def decrypt_stuff(self):
        try:
            self.keyInt = int(str(self.ketTXT.get()))
            decrypted_text = decrypt_string("encrypted.txt", self.keyInt,"usersKey.txt")
            self.userText.delete("1.0", tk.END)
            self.userText.insert(tk.END, decrypted_text)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer key.")

    def saveStuff(self):
        encrypted_text = self.userText.get("1.0", "end-1c")
        key1 = int(str(self.ketTXT.get()))
        if verify_key( "usersKey.txt",key1):

            encrypt_string(encrypted_text, "encrypted.txt", key1,'l.txt')
        messagebox.showinfo(title="remember da key ma guy", message=f"I saved and encrypted your stuff. The key is {key1}")