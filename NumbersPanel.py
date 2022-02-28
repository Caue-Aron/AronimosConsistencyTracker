import wx
from DefaultPanelBehavior import DefaultPanelBehavior

class NumbersPanel(DefaultPanelBehavior):

    def __init__(self, parent, id=wx.ID_ANY, label="0",
                 pos=wx.DefaultPosition, size=wx.DefaultSize, font=None, *args, **kwargs):
        super().__init__(parent, id, pos, size, *args, **kwargs)

        self.label = label

        if font:
            self.SetFont(font)
        else:
            self.SetFont(self.GetParent().GetFont())

        # -----------------------------------------------------------------------------------
        # initialize Counter properties
        border = wx.BoxSizer()
        self.number = wx.StaticText(self, wx.ID_ANY, label=self.label)
        # self.number.SetFont()
        border.Add(self.number, 0, wx.ALL, 6)
        self.SetSizer(border)

    def set_label(self, label):
        self.number.SetLabel(str(label))

    def on_LeftDown(self, evt):
        print('Numbers')