from tkinter import *
from tkinter import ttk

class Info(Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.lbf_frame = LabelFrame(self, text='Info')
        self.lb_success_rate = Label(self.lbf_frame, text='Success rate: 0 out of 0')
        self.lb_percentage = Label(self.lbf_frame, text='Percentage: 0%')

        self.lbf_frame.grid(row=0, column=0, padx=(5, 5), pady=(1, 5))
        self.lb_success_rate.grid(row=0, column=0, padx=(5, 5))
        self.lb_percentage.grid(row=1, column=0)