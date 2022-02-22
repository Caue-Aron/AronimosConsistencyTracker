import wx
from Button import Button
from Button import EVT_BUTTON
from NumbersPanel import NumbersPanel
from DefaultControlBehavior import DefaultPanelBehavior
from NewButton import NewButton

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

        self.add        = Button(self, wx.ID_ANY, label='+', size=buttons_size, font=wx.Font(wx.FontInfo(15)), color='#b5e61d')
        self.subtract   = Button(self, wx.ID_ANY, label='-', size=buttons_size, font=wx.Font(wx.FontInfo(15)), color='#ff7f27')
        self.panel      = NumbersPanel(self, wx.ID_ANY, size=(50, 30), font=wx.Font(wx.FontInfo(10)), style=wx.DOUBLE_BORDER)

        # -----------------------------------------------------------------------------------
        # Setting sizers
        self.box_sizer.Add(self.add,      0, wx.CENTER | wx.BOTTOM | wx.LEFT, 3)
        self.box_sizer.Add(self.subtract, 0, wx.CENTER | wx.BOTTOM | wx.RIGHT | wx.LEFT, 3)
        self.box_sizer.Add(self.panel,    0, wx.CENTER)

        border.Add(self.box_sizer, 1, wx.EXPAND | wx.ALL, 5)
        self.SetSizer(border)

        # -----------------------------------------------------------------------------------
        # Setting bindings
        self.add.Bind(EVT_BUTTON, self.add_function)
        self.subtract.Bind(EVT_BUTTON, self.subtract_function)

    def add_function(self, evt):
        if evt.value == 'press':
            self.count += 1
            self.panel.set_label(self.count)

        evt.Skip()

    def subtract_function(self, evt):
        if evt.value == 'press':
            if self.count - 1 >= 0:
                self.count -= 1
                self.panel.set_label(self.count)

        evt.Skip()

    def get_count(self):
        return self.count
