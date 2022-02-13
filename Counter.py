from tkinter import *
from tkinter import ttk
from Config import main_window

button_width = main_window['button_width']
button_height = main_window['button_height']
button_add_color = main_window['button_add_color']
button_subtract_color = main_window['button_subtract_color']
button_pady = main_window['button_pady']

entry_width = main_window['entry_width']

class Counter(Frame):
    def __init__(self, parent, text, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.lbf_frame = LabelFrame(self, text=text)

        self.btn_add =      Button(self.lbf_frame, text='+', bg=button_add_color, relief='groove', width=button_width, height=button_height)
        self.btn_subtract = Button(self.lbf_frame, text='-', bg=button_subtract_color, relief='groove', width=button_width, height=button_height)
        self.e_entry = ttk.Entry(self.lbf_frame, width=entry_width)

        self.e_entry.insert(0, f'{0}')
        self.e_entry.config(state='disabled')

        self.lbf_frame.grid     (row=0, column=0, padx=(6, 5))
        self.btn_add.grid       (row=0, column=0, padx=(5, 1), pady=button_pady)
        self.btn_subtract.grid  (row=0, column=1, padx=(1, 1), pady=button_pady)
        self.e_entry.grid       (row=0, column=2, padx=(1, 5), pady=button_pady)

    def set_buttons_command(self, function):
        self.btn_add.config(command=lambda: function(+1))
        self.btn_subtract.config(command=lambda: function(-1))

