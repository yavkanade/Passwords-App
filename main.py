import tkinter as tk
import os
from HomePage import *
from LoginPage import *
from AdminHashKeyPage import *
from SignUp import *



if __name__ == "__main__":
    root = tk.Tk()
    if not os.path.exists("admin_key_hash.txt"):
        app = AdminHashKeyPage(root)
    else:
        if not os.path.exists("user.txt"):
            app=SignUp(root)
        else:
            app = LoginPage(root)
    app.pack()
    root.mainloop()