import wx

class DefaultPanelBehavior(wx.Panel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.Bind(wx.EVT_LEFT_DOWN, self.on_LeftDown)
        self.Bind(wx.EVT_LEFT_UP, self.on_LeftUp)
        self.Bind(wx.EVT_RIGHT_UP, self.on_RigtUp)
        self.Bind(wx.EVT_MOTION, self.on_MouseMotion)
        self.Bind(wx.EVT_PAINT, self.on_Paint)

    def on_Paint(self, evt):
        thickness = 1
        dc = wx.PaintDC(self)
        w, h = self.GetSize()

        dc.SetPen(wx.Pen('white', thickness))
        dc.SetBrush(wx.TRANSPARENT_BRUSH)
        dc.DrawRectangle(0, 0, w - 4, h - 4)

    def on_LeftDown(self, evt):
        wx.PostEvent(self.GetParent(), evt)

    def on_LeftUp(self, evt):
        wx.PostEvent(self.GetParent(), evt)

    def on_RigtUp(self, evt):
        wx.PostEvent(self.GetParent(), evt)

    def on_MouseMotion(self, evt):
        wx.PostEvent(self.GetParent(), evt)
