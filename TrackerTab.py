from tkinter import *
from TrackerArea import TrackerArea

class TrackerTab(Frame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # ------------------------------------------------------------------------------
        # setting widgets
        self.tracker_area = TrackerArea(self)

        self.tracker_area.grid(row=0, column=0)