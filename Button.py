import wx
from wx.lib.buttons import GenButton
from wx.lib.newevent import NewCommandEvent

button_event, EVT_BUTTON = NewCommandEvent()

class Button(GenButton):

    def __init__(self, parent, id, label='', size=wx.DefaultSize, font=None, color='#a0a0a0'):
        super().__init__(parent, id, label='', size=size, style=wx.NO_BORDER)

        self.mouse_down = False
        self.mouse_in = False
        self.buffer = None
        self.label = label
        self.color = color

        self.SetBackgroundColour(self.GetParent().GetBackgroundColour())

        if type(font) != wx.Font:
            self.font = self.GetParent().GetFont()
        else:
            self.font = font

        self.Bind(wx.EVT_LEAVE_WINDOW, self.OnMouseLeave)
        self.Bind(wx.EVT_ENTER_WINDOW, self.OnMouseEnter)

    def OnPaint(self, evt):
        wx.BufferedPaintDC(self, self.buffer)

    def OnSize(self, event):
        size = self.GetClientSize()

        # Make sure size is at least 1px to avoid
        # strange "invalid bitmap size" errors.
        if size[0] < 1:
            size = (1, 1)
        self.buffer = wx.Bitmap(*size)
        self.update()

    def update(self):
        dc = wx.MemoryDC()
        dc.SelectObject(self.buffer)
        dc = wx.GCDC(dc)

        self.draw_background(dc)
        self.draw_widget(dc)

        del dc

        self.Refresh()
        self.Update()

    def draw_background(self, dc):
        dc.SetBackground(wx.Brush(self.GetParent().GetBackgroundColour()))
        dc.Clear()

    def draw_widget(self, dc):
        thickness = 1
        w, h = self.GetSize()

        thickness = 2
        if self.mouse_down:
            dc.SetBrush(wx.Brush(wx.Colour(self.color).ChangeLightness(85)))
            dc.SetPen(wx.TRANSPARENT_PEN)
            dc.DrawRectangle(1, 1, w - 2, h - 2)

            dc.SetPen(wx.Pen(wx.Colour(self.color).ChangeLightness(45), thickness))
            dc.DrawLine(0, thickness, w - 2, thickness)
            dc.DrawLine(thickness, thickness, thickness, h - 2)

            dc.SetPen(wx.Pen('#a0a0a0', thickness))
            dc.DrawLine(0, 0, 0, h)
            dc.DrawLine(0, 0, w, 0)

            dc.SetPen(wx.Pen('white', thickness))
            dc.DrawLine(w - 1, thickness, w - 1, h)
            dc.DrawLine(thickness, h - 1, w - thickness, h - 1)

        elif self.mouse_in:
            dc.SetBrush(wx.Brush(wx.Colour(self.color)))
            dc.SetPen(wx.Pen(wx.Colour(self.color).ChangeLightness(85)))
            dc.DrawRectangle(1, 1, w - 2, h - 2)

            dc.SetBrush(wx.Brush(wx.Colour(self.color).ChangeLightness(125)))
            dc.DrawRectangle(3, 3, w - 6, h - 6)

            dc.SetPen(wx.Pen("#a0a0a0", thickness))
            dc.DrawLine(w, 2, w, h)
            dc.DrawLine(2, h, w, h)

        else:
            dc.SetBrush(wx.Brush(wx.Colour(self.color)))
            dc.SetPen(wx.Pen(wx.Colour(self.color).ChangeLightness(85)))
            dc.DrawRectangle(1, 1, w - 2, h - 2)

            dc.SetPen(wx.Pen(wx.Colour(self.color).ChangeLightness(125)))
            dc.DrawRectangle(3, 3, w - 6, h - 6)

            dc.SetPen(wx.Pen("#a0a0a0", thickness))
            dc.DrawLine(w, 2, w, h)
            dc.DrawLine(2, h, w, h)

        dc.SetFont(self.font)
        txt_w, txt_h = dc.GetTextExtent(self.label)
        txt_x = (w - txt_w) / 2
        txt_y = (h - txt_h) / 2

        if self.mouse_down:
            txt_x += thickness / 2
            txt_y += thickness / 2

        # Draw text
        dc.DrawText(self.label, int(txt_x), int(txt_y))

    def button_function(self):
        print('no function for button')

    def set_function(self, function):
        self.button_function = function

    def OnLeftDown(self, evt):
        self.mouse_down = True
        self.update()
        self.button_function()
        self.send_event(True)

    def OnLeftUp(self, evt):
        self.mouse_down = False
        self.update()
        self.send_event(False)

    def OnMouseEnter(self, evt):
        self.mouse_in = True
        self.update()

    def OnMouseLeave(self, evt):
        if self.mouse_down:
            self.mouse_down = False

        self.mouse_in = False

        self.update()

    def send_event(self, pressed):
        wx.PostEvent(self, button_event(id=self.GetId(), value=pressed))