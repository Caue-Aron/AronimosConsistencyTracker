import wx

class FileMenu(wx.Menu):

    def __init__(self, parent, open_function, save_function):
        super().__init__()

        self.parent = parent

        self.new  = wx.MenuItem(self, wx.ID_ANY, 'New')
        self.save = wx.MenuItem(self, wx.ID_ANY, 'Save')
        self.exit = wx.MenuItem(self, wx.ID_ANY, 'Exit')

        self.Bind(wx.EVT_MENU, lambda evt: wx.PostEvent(self.parent, evt), self.new)
        self.Bind(wx.EVT_MENU, save_function, self.save)
        self.Bind(wx.EVT_MENU, self.on_menu_Exit, self.exit)

        self.Append(self.new)
        self.Append(self.save)
        self.AppendSeparator()
        self.Append(self.exit)

    def on_menu_Exit(self, evt):
        wx.Exit()
