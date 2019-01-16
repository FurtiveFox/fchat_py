import tkinter as tk
from tkinter import ttk
from constants import AppInfo


# class MainUIWindow(tk.Tk):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.title(AppInfo.APPNAME + ' version: ' + str(AppInfo.APPVER))
#         self.resizable(width=False, height=False)
#         mainmenu = MainUIMenu(self)


class MainUIMenu(tk.Menu):
    def __init__(self, parent):
        super().__init__(parent)

        menubar = tk.Menu(self)
        parent.config(menu=menubar)
        # menubar.add_command(label="Quit!", command=quit)
        # menubar.add_separator()
        menubar.add_command(label="Quit", command=self.quit)
        menubar.add_command(label="Login", command=self.logmein)

    def quit(self):
        quit()

    def logmein(self):
        login = AddAccountWindow()
        login.mainloop()


class AddAccountWindow(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Add Account")
        self.resizable(width=False, height=False)
        account_frame = AddAccountFrame(self)
        account_frame.grid(padx=50, pady=50)


class AddAccountFrame(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.inputs = {}
        self.inputs['save_password'] = tk.BooleanVar()
        self.inputs['save_password'].set(False)

        self.inputframe = tk.LabelFrame(self, text="Account Information")

        tk.Label(self.inputframe, text="Username: ").grid(row=0, column=0)
        self.inputs['username'] = ttk.Entry(self.inputframe)
        self.inputs['username'].grid(row=0, column=1, padx=20, pady=20)

        ttk.Label(self.inputframe, text="Password: ").grid(row=1, column=0)
        self.inputs['password'] = ttk.Entry(self.inputframe, show="*")
        self.inputs['password'].grid(row=1, column=1, padx=20, pady=20)

        self.inputframe.grid(columnspan=2)

        self.save_password_box = ttk.Checkbutton(self, text="Save Password", variable=self.inputs['save_password'])
        self.save_password_box.grid(row=2, column=0)

        self.login_button = ttk.Button(self, text="Login", command=self.on_login)
        self.login_button.grid(row=2, column=1, pady=25)

    def get(self):

        data = {}
        for key, widget in self.inputs.items():
            data[key] = widget.get()
        return data

    def on_login(self):
        print(self.get())
        quit()


if __name__ == '__main__':
    pass
