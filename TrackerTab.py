import wx
from DefaultPanelBehavior import DefaultPanelBehavior
from Info import Info
from Counter import Counter
from Button import EVT_BUTTON
from Stage import Stage
from pickle import dump, load
from ComboBox import ComboBox
from ComboBox import EVT_DROPDOWN

class TrackerTab(DefaultPanelBehavior):
    def __init__(self, parent):
        super().__init__(parent, style=wx.DOUBLE_BORDER)
        from os import listdir
        from os import getcwd

        # -----------------------------------------------------------------------------------
        # Initializing GUI widgets
        self.success_counter = Counter(self, wx.ID_ANY, 'Success')
        self.fail_counter    = Counter(self, wx.ID_ANY, 'Fails')
        self.info            = Info(parent=self)

        dir = getcwd()
        dir_files = listdir(dir)
        stages_list = list()
        names_list = list()
        for i in dir_files:
            if i.endswith(".txt"):
                stages_list.append(self.deserialise(i))
                names_list.append(self.deserialise(i).get_name())

        if not stages_list:
            self.stage = Stage('Unnamed Stage')
            self.cb              = ComboBox(self, items=['Unamed Stage',], default='Unamed Stage')
        else:
            self.stage           = stages_list[0]
            self.cb              = ComboBox(self, items=names_list, default=names_list[0])

        # -----------------------------------------------------------------------------------
        # Setting sizers
        border = wx.BoxSizer(wx.VERTICAL)

        border.Add(self.cb, 0, wx.CENTER | wx.LEFT | wx.RIGHT | wx.TOP, 15)
        border.Add(self.success_counter, 0, wx.CENTER | wx.LEFT | wx.RIGHT | wx.TOP, 10)
        border.Add(self.fail_counter,    0, wx.CENTER | wx.BOTTOM | wx.TOP, 3)
        border.Add(self.info,            0, wx.CENTER | wx.BOTTOM | wx.TOP, 10)

        self.load()
        self.SetSizer(border)

        # -----------------------------------------------------------------------------------
        # Setting bindings
        self.Bind(EVT_BUTTON, self.update)
        self.Bind(EVT_DROPDOWN, self.change_stage)
        self.Fit()

    def change_stage(self, evt):
        from os import listdir
        from os import getcwd
        dir = getcwd()
        dir_files = listdir(dir)
        for i in dir_files:
            if i.endswith(".txt"):
                stage = self.deserialise(i)
                if stage.get_name() == evt.value:
                    self.stage = stage
                    break

        self.load()

    def update(self, evt):
        success_count = self.success_counter.get_count()
        fail_count = self.fail_counter.get_count()
        tries = success_count + fail_count

        self.stage.set_fails(fail_count)
        self.stage.set_success(success_count)
        self.info.update(success_count, tries)
        evt.Skip()

    def serialise(self, evt):
        if self.stage.get_name() != '':
            file = open(f'{self.stage.get_name()}.txt', 'wb')
            dump(self.stage, file)
            file.close()

    def deserialise(self, name):
        file = open(name, 'rb')
        stage = load(file)
        file.close()
        return stage

    def load(self):
        success = self.stage.get_success()
        fails = self.stage.get_fails()

        self.success_counter.set_count(success)
        self.success_counter.update_label()

        self.fail_counter.set_count(fails)
        self.fail_counter.update_label()

        tries = success + fails
        self.info.update(success, tries)

    def create_stage(self, name):
        print(name)
        if self.stage.get_name() != 'Unnamed Stage':
            self.serialise(0)

        if name:
            new_stage = Stage(name)
            self.stage = new_stage
            self.load()
            self.cb.items.append(new_stage.get_name())
            self.cb.CreateMenu()
            self.cb.set_value(new_stage.get_name())
