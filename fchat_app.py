import tkinter as tk
from tkinter import ttk
from constants import AppInfo
import fchat_gui as g



class MainUIWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title(AppInfo.APPNAME + ' version: ' + str(AppInfo.APPVER))
        self.resizable(width=True, height=True)
        mainmenu = g.MainUIMenu(self)


if __name__ == '__main__':

    fchat_app = MainUIWindow()
    fchat_app.mainloop()
