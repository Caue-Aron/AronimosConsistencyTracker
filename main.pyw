import wx

from TrackerTab import TrackerTab
from Button import EVT_BUTTON
import psutil

class Main(wx.Frame):

    def __init__(self):
        super().__init__(None, wx.ID_ANY, "Arônimo's Consitency Tracker", style=wx.NO_BORDER)

        self.m_delta = wx.Point(0, 0)
        self.can_click = True
        self.clicked_button = False

        self.x = self.GetPosition()[0]
        self.y = self.GetPosition()[1]

        self.timer = wx.Timer(self, wx.ID_ANY)

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
        self.Bind(wx.EVT_TIMER, self.display_memory, self.timer)

        self.SetSizer(sizer)

        self.Fit()
        self.Show()
        self.timer.Start(1000)

    def display_memory(self, evt):
        print(f"RAM: {psutil.virtual_memory().percent}%")
        print(f"CPU: {psutil.cpu_percent()}%")

    def on_RightDown(self, evt):
        from PopupMenu import PopupMenu
        self.PopupMenu(PopupMenu(), wx.Point(wx.GetMousePosition()[0] - self.GetPosition()[0], wx.GetMousePosition()[1] - self.GetPosition()[1]))

    def on_Button(self, evt):
        if evt.value == 'press':
            self.clicked_button = True
            self.can_click = False
        elif evt.value == 'release':
            self.can_click = True
            self.clicked_button = False

    # Makes frame move
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
app.MainLoop()