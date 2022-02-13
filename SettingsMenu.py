from tkinter import *
from tkinter import ttk

class SettingsMenu(Menu):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        # ------------------------------------------------------------------------------
        # properties settings
        self.name = 'Settings'
        self.config(tearoff=False)

        # ------------------------------------------------------------------------------
        # adding menu cascade
        self.add_command(label='Layout', command=self.on_menu_Layout)
        self.add_command(label='HotKeys', command=self.on_menu_HotKeys)

    def on_menu_Layout(self):
        pass

    def on_menu_HotKeys(self):
        pass