import wx
from FileMenu import FileMenu

class PopupMenu(wx.Menu):

    def __init__(self, parent, open_function, save_function):
        super().__init__()

        self.parent = parent

        self.file_menu = FileMenu(self, open_function, save_function)
        self.Bind(wx.EVT_MENU, lambda evt: wx.PostEvent(self.parent, evt))

        self.AppendSubMenu(self.file_menu, 'File')