# ----------------------------------------------------------------------------
# gswidgetkit Copyright 2021-2022 by Noah Rahm and contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ----------------------------------------------------------------------------

import wx
from wx.lib.newevent import NewCommandEvent

TEXT_COLOR = '#000000'

button_cmd_event, EVT_BUTTON = NewCommandEvent()

class Button(wx.Window):
    """ 
    Button with support for the following combinations:
    1. text
    2. icon + text
    3. icon

    :param wx.Window `parent`: parent window. Must not be ``None``.
    :param integer `id`: window identifier. A value of -1 indicates a default value.
    :param string `label`: the displayed button label.
    :param tuple `bmp`: the button icon as (wx.Bitmap, pos). pos can be one of 'top', 'left', 'right', 'bottom'.
    :param bool `center`: if True the contents of the button will be centered rather than left-aligned.
    :param bool `flat`: if True, the background will take on the color of the parent window.
    """
    def __init__(self, parent, id=wx.ID_ANY, label="", center=True,
                 pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.NO_BORDER, color="#f0f0f0",
                 font=None, name='DefaultButton'):
        super().__init__(parent, id, pos, size, style, name)

        self.parent = parent
        self.color = color

        if font:
            self.SetFont(font)
        else:
            self.SetFont(self.parent.GetFont())

        # Add spaces around a button with text
        if label != "":
            self.label = " {} ".format(label)
            self.padding = (10, 20, 10, 20)
        else:
            # Icon button
            self.label = label
            self.padding = (5, 6, 5, 6)

        self.buffer = None
        self.center = center
        self.outer_padding = 4
        self.size = None
        self.bmp = None

        self.mouse_in = False
        self.mouse_down = False

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_LEAVE_WINDOW, self.OnMouseLeave)
        self.Bind(wx.EVT_ENTER_WINDOW, self.OnMouseEnter)
        self.Bind(wx.EVT_LEFT_DOWN, self.OnMouseDown)
        self.Bind(wx.EVT_LEFT_UP, self.OnMouseUp)
        self.Bind(wx.EVT_SIZE, self.OnSize)

    def OnPaint(self, evt):
        wx.BufferedPaintDC(self, self.buffer)

    def OnSize(self, evt):
        size = self.GetClientSize()

        # Make sure size is at least 1px to avoid
        # strange "invalid bitmap size" errors.
        if size[0] < 1:
            size = (1, 1)
        self.buffer = wx.Bitmap(*size)
        self.UpdateDrawing()

    def UpdateDrawing(self):
        dc = wx.MemoryDC()
        dc.SelectObject(self.buffer)
        dc = wx.GCDC(dc)
        self.OnDrawBackground(dc)
        self.OnDrawWidget(dc)
        del dc  # need to get rid of the MemoryDC before Update() is called.
        self.Refresh()
        self.Update()

    def OnDrawBackground(self, dc):
        dc.SetBackground(wx.Brush(self.parent.GetBackgroundColour()))
        dc.Clear()

    def OnDrawWidget(self, dc):
        dc.SetFont(self.GetFont())

        w, h = self.GetSize()

        dc.SetBrush(wx.Brush(self.color))
        dc.SetPen(wx.TRANSPARENT_PEN)
        dc.DrawRectangle(0, 0, w-1, h-1)

        thickness = 2
        if self.mouse_down:
            dc.SetPen(wx.Pen('#a0a0a0', thickness))
            dc.DrawLine(0, 0, w-1, 0)
            dc.SetPen(wx.Pen(wx.Colour(self.color).ChangeLightness(45), thickness))
            dc.DrawLine(0, thickness, w-2, thickness)

            dc.SetPen(wx.Pen('#a0a0a0', thickness))
            dc.DrawLine(0, 0, 0, h-1)
            dc.SetPen(wx.Pen(wx.Colour(self.color).ChangeLightness(45), thickness))
            dc.DrawLine(thickness, thickness, thickness, h-2)

            dc.SetPen(wx.Pen('white', thickness))
            dc.DrawLine(w, thickness, w, h)
            dc.SetPen(wx.Pen("white", thickness))
            dc.DrawLine(2, h, w - thickness, h)

        elif self.mouse_in:
            dc.SetBrush(wx.Brush(wx.Colour(self.color).ChangeLightness(125)))

            dc.SetPen(wx.Pen(wx.Colour(self.color).ChangeLightness(125)))
            dc.DrawRectangle(1, 1, w - 3, h - 3)

            dc.SetPen(wx.Pen(wx.Colour(self.color).ChangeLightness(85)))
            dc.DrawRectangle(2, 2, w - 4, h - 4)

            dc.SetPen(wx.Pen("#a0a0a0", thickness))
            dc.DrawLine(w, 2, w, h)

            dc.SetPen(wx.Pen("#a0a0a0", thickness))
            dc.DrawLine(2, h, w, h)

        else:
            dc.SetPen(wx.Pen(wx.Colour(self.color).ChangeLightness(85)))
            dc.DrawRectangle(1, 1, w - 3, h - 3)

            dc.SetPen(wx.Pen(wx.Colour(self.color).ChangeLightness(125)))
            dc.DrawRectangle(2, 2, w - 5, h - 5)

            dc.SetPen(wx.Pen("#a0a0a0", thickness))
            dc.DrawLine(w, 2, w, h)

            dc.SetPen(wx.Pen("#a0a0a0", thickness))
            dc.DrawLine(2, h, w, h)

        txt_w, txt_h = dc.GetTextExtent(self.label)

        if self.center:
            txt_x = (w - txt_w) / 2
            txt_y = (h - txt_h) / 2
        else:
            txt_x = self.padding[3]
            txt_y = self.padding[0]

        if self.mouse_down:
            txt_x += thickness - (thickness/2)
            txt_y += thickness - (thickness/2)

        # Text color
        dc.SetTextForeground(wx.Colour(TEXT_COLOR))

        # Draw text
        dc.DrawText(self.label, int(txt_x), int(txt_y))

    def OnMouseEnter(self, evt):
        self.mouse_in = True
        self.UpdateDrawing()

    def OnMouseLeave(self, evt):
        self.mouse_in = False
        if self.mouse_down:
            self.mouse_down = False
            self.SendButtonEvent('leave')

        self.UpdateDrawing()

    def OnMouseDown(self, evt):
        self.mouse_down = True
        self.SendButtonEvent('press')
        self.UpdateDrawing()

    def OnMouseUp(self, evt):
        self.mouse_down = False
        self.SendButtonEvent('release')
        self.UpdateDrawing()

    def SendButtonEvent(self, value):
        wx.PostEvent(self, button_cmd_event(id=self.GetId(), value=value))

    def DoGetBestSize(self):
        font = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT)

        dc = wx.ClientDC(self)
        dc.SetFont(font)

        txt_w, txt_h = dc.GetTextExtent(self.label)

        size = (self.padding[3] + txt_w + self.padding[1],
                self.padding[0] + txt_h + self.padding[2])

        return wx.Size(size)