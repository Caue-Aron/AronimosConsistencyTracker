import wx

class FileMenu(wx.Menu):

    def __init__(self):
        super().__init__()

        self.open = wx.MenuItem(self, wx.ID_ANY, 'Open')
        self.save = wx.MenuItem(self, wx.ID_ANY, 'Save')
        self.exit = wx.MenuItem(self, wx.ID_ANY, 'Exit')

        self.Bind(wx.EVT_MENU, self.on_menu_Open, self.open)
        self.Bind(wx.EVT_MENU, self.on_menu_Save, self.save)
        self.Bind(wx.EVT_MENU, self.on_menu_Exit, self.exit)

        self.Append(self.open)
        self.Append(self.save)
        self.AppendSeparator()
        self.Append(self.exit)

    def on_menu_Open(self, evt):
        pass

    def on_menu_Save(self, evt):
        pass

    def on_menu_Exit(self, evt):
        wx.Exit()
