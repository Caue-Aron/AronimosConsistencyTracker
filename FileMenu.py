from tkinter import *
from tkinter import ttk

class FileMenu(Menu):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        # ------------------------------------------------------------------------------
        # properties settings
        self.name = 'File'
        self.config(tearoff=False)

        # ------------------------------------------------------------------------------
        # adding menu cascade
        self.add_command(label='Open', command=self.on_menu_Open)
        self.add_command(label='Save', command=self.on_menu_Save)
        self.add_separator()
        self.add_command(label='Exit', command=self.on_menu_Exit)

    def on_menu_Open(self):
        pass

    def on_menu_Save(self):
        pass

    def on_menu_Exit(self):
        self.parent.parent.parent.destroy()