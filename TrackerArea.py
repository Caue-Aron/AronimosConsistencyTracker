from tkinter import *
from Info import Info
from Counter import Counter

class TrackerArea(Frame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # ------------------------------------------------------------------------------
        # variables used to calculate consistency
        self.success_count = 0
        self.fail_count = 0
        self.tries = 0

        # ------------------------------------------------------------------------------
        # setting widgets
        self.f_success_counter =    Counter(self, text='Success')
        self.f_fail_counter =       Counter(self, text='Fail')
        self.f_info =               Info(self)

        self.f_success_counter. grid(row=0, column=0, sticky='W')
        self.f_fail_counter.    grid(row=1, column=0, sticky='W')
        self.f_info.            grid(row=2, column=0)

        # ------------------------------------------------------------------------------
        # setting commands
        self.f_success_counter.set_buttons_command(self.success)
        self.f_fail_counter.set_buttons_command(self.fail)

    def update_info(self):
        if self.success_count > 0 or self.fail_count > 0:
            info = self.f_info
            info.lb_success_rate.config(text=f'Success rate: {self.success_count} out of {self.tries}')

            percentage = round((self.success_count / self.tries) * 100, 1)
            info.lb_percentage.config(text=f'Percentage: {percentage}%')
        else:
            info = self.f_info
            info.lb_success_rate.config(text=f'Success rate: {0} out of {0}')
            info.lb_percentage.config(text=f'Percentage: {0}%')

    # ------------------------------------------------------------------------------
    # commands for consitency managing
    def success(self, number):
        self.success_count += number

        if self.success_count < 0:
            self.success_count = 0
            return

        self.tries += number

        entry = self.f_success_counter.e_entry

        entry.config(state='enabled')
        entry.delete(0, END)
        entry.insert(0, f'{self.success_count}')
        entry.config(state='disabled')

        self.update_info()

    def fail(self, number):
        self.fail_count += number

        if self.fail_count < 0:
            self.fail_count = 0
            return

        self.tries += number

        entry = self.f_fail_counter.e_entry
        entry.config(state='enabled')
        entry.delete(0, END)
        entry.insert(0, f'{self.fail_count}')
        entry.config(state='disabled')

        self.update_info()
