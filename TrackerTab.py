import wx
from Info import Info
from Counter import Counter
from DefaultPanelBehavior import DefaultPanelBehavior

class TrackerTab(DefaultPanelBehavior):

    def __init__(self, parent):
        super().__init__(parent, style=wx.DOUBLE_BORDER)

        # -----------------------------------------------------------------------------------
        # Setting attributes
        self.success_count = 0
        self.fail_count = 0
        self.tries = 0

        # -----------------------------------------------------------------------------------
        # Initializing GUI widgets
        self.success_counter = Counter(self, wx.ID_ANY, 'Success')
        self.fail_counter    = Counter(self, wx.ID_ANY, 'Fails')
        self.info            = Info(parent=self)

        # -----------------------------------------------------------------------------------
        # Setting sizers
        border = wx.BoxSizer(wx.VERTICAL)

        border.Add(self.success_counter, 0, wx.CENTER | wx.LEFT | wx.RIGHT | wx.TOP, 10)
        border.Add(self.fail_counter,    0, wx.CENTER | wx.BOTTOM | wx.TOP, 3)
        border.Add(self.info,            0, wx.CENTER | wx.BOTTOM | wx.TOP, 10)

        self.SetSizer(border)

        # -----------------------------------------------------------------------------------
        # Setting bindings
        self.Bind(wx.EVT_BUTTON, self.update_info)

    def update_info(self, evt):
        self.success_count = self.success_counter.get_count()
        self.fail_count = self.fail_counter.get_count()
        self.tries = self.success_count + self.fail_count

        self.info.update(self.success_count, self.tries)

        evt.Skip()

