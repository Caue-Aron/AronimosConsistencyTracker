import wx
from TrackerTab import TrackerTab
from Button import EVT_BUTTON

class Main(wx.Frame):
    def __init__(self):
        super().__init__(None, wx.ID_ANY, "Arônimo's Consitency Tracker", style=wx.NO_BORDER)

        self.m_delta = wx.Point(0, 0)
        self.can_click = True
        self.clicked_button = False

        self.x = self.GetPosition()[0]
        self.y = self.GetPosition()[1]

        # -----------------------------------------------------------------------------------
        # Initializing GUI widgets
        self.tracker_tab = TrackerTab(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.tracker_tab, wx.ALL, 5)

        # -----------------------------------------------------------------------------------
        # Setting bindings
        self.Bind(wx.EVT_RIGHT_UP, self.on_RightDown)
        self.Bind(wx.EVT_LEFT_DOWN, self.on_LeftDown)
        self.Bind(wx.EVT_LEFT_UP, self.on_LeftRelease)
        self.Bind(wx.EVT_MOTION, self.on_MouseMotion)
        self.Bind(EVT_BUTTON, self.on_Button)
        self.Bind(wx.EVT_MENU, self.ask)

        self.SetSizer(sizer)

        self.Fit()
        self.Show()

    def key_down(self, evt):
        keycode = evt.GetKeyCode()

        if keycode == wx.WXK_NUMPAD0:
            self.tracker_tab.fail_counter.add.OnLeftDown(0)

        elif keycode == wx.WXK_NUMPAD3:
            self.tracker_tab.fail_counter.subtract.OnLeftDown(0)

        elif keycode == wx.WXK_NUMPAD1:
            self.tracker_tab.success_counter.add.OnLeftDown(0)

        elif keycode == wx.WXK_NUMPAD2:
            self.tracker_tab.success_counter.subtract.OnLeftDown(0)

        elif keycode == wx.WXK_NUMPAD5:
            self.tracker_tab.serialise(0)
            
        evt.Skip()

    def key_up(self, evt):
        keycode = evt.GetKeyCode()

        if keycode == wx.WXK_NUMPAD0:
            self.tracker_tab.fail_counter.add.OnLeftUp(0)

        elif keycode == wx.WXK_NUMPAD3:
            self.tracker_tab.fail_counter.subtract.OnLeftUp(0)

        elif keycode == wx.WXK_NUMPAD1:
            self.tracker_tab.success_counter.add.OnLeftUp(0)

        elif keycode == wx.WXK_NUMPAD2:
            self.tracker_tab.success_counter.subtract.OnLeftUp(0)

        evt.Skip()

    def ask(self, evt):
        print('asked')
        dlg = wx.TextEntryDialog(None, 'Enter the stage/mission/trick name:')
        dlg.ShowModal()
        result = dlg.GetValue()
        dlg.Destroy()

        self.tracker_tab.create_stage(result)

    # Popup Menu
    def on_RightDown(self, evt):
        from PopupMenu import PopupMenu
        pos = wx.Point(wx.GetMousePosition()[0] - self.GetPosition()[0], wx.GetMousePosition()[1] - self.GetPosition()[1])
        self.PopupMenu(PopupMenu(self, None, self.tracker_tab.serialise), pos)

    # Makes frame move
    def on_Button(self, evt):
        if evt.value:
            self.clicked_button = True
            self.can_click = False
        else:
            self.can_click = True
            self.clicked_button = False

    def on_LeftDown(self, evt):
        self.CaptureMouse()
        pos = wx.GetMousePosition()
        origin = self.GetPosition()
        dx = pos.x - origin.x
        dy = pos.y - origin.y
        self.m_delta = wx.Point(dx, dy)

    def on_LeftRelease(self, evt):
        if self.clicked_button:
            self.clicked_button = False
            self.can_click = True

        if self.HasCapture():
            self.ReleaseMouse()

    def on_MouseMotion(self, evt):
        if evt.LeftIsDown() and self.can_click:
            pos = wx.GetMousePosition()
            self.Move(wx.Point(pos.x - self.m_delta.x, pos.y - self.m_delta.y))

app = wx.App()
frame = Main()
app.Bind(wx.EVT_KEY_DOWN, frame.key_down)
app.Bind(wx.EVT_KEY_UP, frame.key_up)
app.MainLoop()