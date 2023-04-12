import tkinter as tk
from tkinter import messagebox
from coreFunctions import *
import os

class LoginPage(tk.Frame):

    def __init__(self, master):
        super().__init__(master)

        self.master = master
        self.master.geometry("900x900")
        self.master.title("Password app")

        self.labelkey = tk.Label(self, text="Enter admin key:", font=("Arial", 20))
        self.labelkey.pack(padx=30, pady=10)

        self.adminKeytxt = tk.Entry(self, width=30, font=("Arial", 20), show="*")
        self.adminKeytxt.pack(padx=30, pady=10)

        self.submit_admin_key_button = tk.Button(self, text="Submit", font=("Arial", 20), command=self.check_admin_key)
        self.submit_admin_key_button.pack(padx=30, pady=10)

    def check_admin_key(self):
        adminKeyInt = int(self.adminKeytxt.get())
        if verify_key("admin_key_hash.txt", adminKeyInt):
            self.labelkey.pack_forget()
            self.adminKeytxt.pack_forget()
            self.submit_admin_key_button.pack_forget()
            self.create_Login_form()

    def create_Login_form(self):


        self.labelWelcome = tk.Label(self, text="Welcome!", font=("Arial", 25))
        self.labelWelcome.grid(row=0, column=0, columnspan=3, padx=30, pady=30)


        self.labelLoginname = tk.Label(self, text="Loginname:", font=("Arial", 20))
        self.labelLoginname.grid(row=2, column=0, padx=30, pady=10)

        self.loginTxt = tk.Entry(self, width=30, background="Blue", font=("Arial", 20), show="*")
        self.loginTxt.grid(row=2, column=1, columnspan=2, padx=30, pady=10)

        self.labelPassword = tk.Label(self, text="Password:", font=("Arial", 20))
        self.labelPassword.grid(row=3, column=0, padx=30, pady=10)

        self.passwordTxt = tk.Entry(self, width=30, font=("Arial", 20), show="*")
        self.passwordTxt.grid(row=3, column=1, columnspan=2, padx=30, pady=10)

        self.loginButton = tk.Button(self, text="Login", font=("Arial", 20), command=self.login)
        self.loginButton.grid(row=4, column=0, padx=30, pady=30)

        self.questionsNums = ["Question 1", "Question 2", "Question 3","question 4", "Question 5","question 6", "Question 7", "Question 8"]
        self.questions = []
        self.entries = []


        for i, question in enumerate(self.questionsNums):
            label = tk.Label(self, text=f"{question}:", font=("Arial", 20))
            label.grid(row=i+5, column=0, padx=30, pady=10)
            question = tk.Entry(self, width=30, font=("Arial", 20))
            question.grid(row=i+5, column=1, padx=30, pady=10)
            entry = tk.Entry(self, width=30, font=("Arial", 20), show='*')
            entry.grid(row=i+5,column=2, padx=30, pady=10)
            self.entries.append(entry)
            self.questions.append(question)
        self.pack()

    def switch_frame(self, frame_class):
        new_frame = frame_class(self.master)
        self.destroy()
        new_frame.pack()


    def login(self):
        # Get the text from each question and entry
        question_texts = [question.get() for question in self.questions]
        entry_texts = [entry.get() for entry in self.entries]

        # Pass the question and entry texts to combine_strings
        testString = combine_strings(str(self.loginTxt.get()), str(self.passwordTxt.get()), question_texts, entry_texts)

        adminKeyInt = int(self.adminKeytxt.get())
        actualString = decrypt_string("user.txt", adminKeyInt, "admin_key_hash.txt")
        from HomePage import HomePage

        if testString == actualString:
            self.switch_frame(HomePage)




    def switch_frame(self, frame_class):
        new_frame = frame_class(self.master)
        self.destroy()
        new_frame.pack()

