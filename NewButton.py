import wx
from DefaultControlBehavior import DefaultPanelBehavior

class NewButton(wx.Panel):

    def __init__(self, parent, id=wx.ID_ANY, color="#f0f0f0", font=None, label='', *args, **kwargs):
        super().__init__(parent, id, *args, **kwargs)

        self.down = False
        self.focus = False
        self.color = color

        if not font:
            self.SetFont(self.GetParent().GetFont())
        else:
            self.SetFont(font)

        border = wx.BoxSizer()
        self.label = wx.StaticText(self, wx.ID_ANY, label=label)

        border.Add(self.label, 0, wx.ALL, 6)
        self.SetSizer(border)

        self.Bind(wx.EVT_LEFT_DOWN, self.on_LeftDown)
        self.Bind(wx.EVT_LEFT_UP, self.on_LeftUp)
        self.Bind(wx.EVT_PAINT, self.on_Paint)

    def on_Paint(self, evt):
        thickness = 1
        dc = wx.PaintDC(self)
        w, h = self.GetSize()

        if self.down:
            dc.SetPen(wx.TRANSPARENT_PEN)
            dc.SetBrush(wx.Brush(wx.Colour(self.color).ChangeLightness(85)))
            dc.DrawRectangle(2, 2, w - 4, h - 4)

        else:
            dc.SetPen(wx.Pen('white', thickness))
            dc.SetBrush(wx.TRANSPARENT_BRUSH)
            dc.DrawRectangle(0, 0, w - 4, h - 4)

    def on_LeftDown(self, evt):
        print('down')
        self.down = True

    def on_LeftUp(self, evt):
        print('up')
        self.down = False