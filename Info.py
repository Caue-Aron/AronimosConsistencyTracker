import wx
from DefaultPanelBehavior import DefaultPanelBehavior

class Info(DefaultPanelBehavior):

    def __init__(self, parent):
        super().__init__(parent=parent, style=wx.BORDER_DOUBLE)

        # -----------------------------------------------------------------------------------
        # initialize Info properties
        border                  = wx.BoxSizer()

        box                     = wx.StaticBox(self, wx.ID_ANY, "Info")
        self.box_sizer          = wx.StaticBoxSizer(box, wx.VERTICAL)

        self.st_success_rate    = wx.StaticText(self, wx.ID_ANY, 'Success rate: 0 out of 0')
        self.st_percentage      = wx.StaticText(self, wx.ID_ANY, 'Percentage: 0%')

        # -----------------------------------------------------------------------------------
        # building sizers
        self.box_sizer.Add(self.st_success_rate, 0, wx.TOP | wx.LEFT | wx.RIGHT, 5)
        self.box_sizer.Add(self.st_percentage,   0, wx.TOP | wx.LEFT, 5)

        border.Add(self.box_sizer, 1, wx.EXPAND | wx.ALL, 5)
        self.SetSizer(border)

        # -----------------------------------------------------------------------------------
        # Setting bindings
        self.set_bindings()

    def update(self, rate, tries):
        if rate > 0:
            self.st_success_rate.SetLabel(f'Success rate: {rate} out of {tries}')

            if tries > 0:
                self.st_percentage.SetLabel(f'Percentage: {round((rate / tries) * 100, 2)}%')

        self.GetContainingSizer().Layout()

    def set_bindings(self):
        self.box_sizer.GetStaticBox().Bind(wx.EVT_RIGHT_UP, self.on_RigtUp)
        self.box_sizer.GetStaticBox().Bind(wx.EVT_LEFT_DOWN, self.on_LeftDown)
        self.box_sizer.GetStaticBox().Bind(wx.EVT_LEFT_UP, self.on_LeftUp)
        self.box_sizer.GetStaticBox().Bind(wx.EVT_MOTION, self.on_MouseMotion)

        self.st_percentage.Bind(wx.EVT_RIGHT_UP, self.on_RigtUp)
        self.st_percentage.Bind(wx.EVT_LEFT_DOWN, self.on_LeftDown)
        self.st_percentage.Bind(wx.EVT_LEFT_UP, self.on_LeftUp)
        self.st_percentage.Bind(wx.EVT_MOTION, self.on_MouseMotion)

        self.st_success_rate.Bind(wx.EVT_RIGHT_UP, self.on_RigtUp)
        self.st_success_rate.Bind(wx.EVT_LEFT_DOWN, self.on_LeftDown)
        self.st_success_rate.Bind(wx.EVT_LEFT_UP, self.on_LeftUp)
        self.st_success_rate.Bind(wx.EVT_MOTION, self.on_MouseMotion)