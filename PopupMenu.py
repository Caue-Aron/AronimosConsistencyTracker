import wx
from FileMenu import FileMenu

class PopupMenu(wx.Menu):

    def __init__(self):
        super().__init__()

        self.file_menu = FileMenu()

        self.AppendSubMenu(self.file_menu, 'File')