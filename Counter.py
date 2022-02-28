import wx
from Button import Button
from NumbersPanel import NumbersPanel
from DefaultPanelBehavior import DefaultPanelBehavior

class Counter(DefaultPanelBehavior):

    def __init__(self, parent, id, label=''):
        super().__init__(parent, id, style=wx.BORDER_DOUBLE)

        buttons_size = (45, 35)

        # -----------------------------------------------------------------------------------
        # Setting attributes
        self.count = 0

        border = wx.BoxSizer()

        box             = wx.StaticBox(self, wx.ID_ANY, label)
        self.box_sizer  = wx.StaticBoxSizer(box, wx.HORIZONTAL)

        self.add        = Button(self, wx.ID_ANY, label='+', size=buttons_size, font=wx.Font(wx.FontInfo(25)), color='#b5e61d')
        self.subtract   = Button(self, wx.ID_ANY, label='-', size=buttons_size, font=wx.Font(wx.FontInfo(25)), color='#ff7f27')
        self.panel      = NumbersPanel(self, wx.ID_ANY, size=(50, 30), font=wx.Font(wx.FontInfo(10)), style=wx.DOUBLE_BORDER)
        # self.btn        = wx.Button(self, wx.ID_ANY, size=buttons_size, label='Test')

        # -----------------------------------------------------------------------------------
        # Setting sizers
        self.box_sizer.Add(self.add,      0, wx.CENTER | wx.BOTTOM | wx.LEFT, 3)
        self.box_sizer.Add(self.subtract, 0, wx.CENTER | wx.BOTTOM | wx.RIGHT | wx.LEFT, 3)
        # self.box_sizer.Add(self.btn, 0, wx.CENTER | wx.BOTTOM | wx.RIGHT | wx.LEFT, 3)
        self.box_sizer.Add(self.panel,    0, wx.CENTER)

        border.Add(self.box_sizer, 1, wx.EXPAND | wx.ALL, 5)
        self.SetSizer(border)

        # -----------------------------------------------------------------------------------
        # Setting bindings
        self.add.set_function(self.add_function)
        self.subtract.set_function(self.subtract_function)

    def add_function(self):
        self.count += 1
        self.panel.set_label(self.count)

    def subtract_function(self):
        if self.count - 1 >= 0:
            self.count -= 1
            self.panel.set_label(self.count)

    def get_count(self):
        return self.count
