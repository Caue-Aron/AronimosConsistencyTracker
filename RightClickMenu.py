from tkinter import *
from tkinter import ttk
from FileMenu import FileMenu
from SettingsMenu import SettingsMenu

class RightClickMenu(Menu):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        self.config(tearoff=False)

        # ------------------------------------------------------------------------------
        # adding menu cascade
        self.file_menu = FileMenu(self)
        self.settings_menu = SettingsMenu(self)

        self.add_cascade(label=self.file_menu.name, menu=self.file_menu)
        self.add_cascade(label=self.settings_menu.name, menu=self.settings_menu)
