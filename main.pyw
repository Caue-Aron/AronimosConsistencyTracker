from tkinter import *
from tkinter import ttk
from TrackerTab import TrackerTab
from RightClickMenu import RightClickMenu
from Config import hot_keys

# pyinstaller --onefile main.pyw

# ------------------------------------------------------------------------------
# main window
class Main(Toplevel):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # ------------------------------------------------------------------------------
        # window properties
        self.overrideredirect(True)
        self.attributes('-topmost', 1)
        self.grab_set()
        self.parent = parent

        # ------------------------------------------------------------------------------
        # used to drag and drop the window
        self.x = 0
        self.y = 0

        # ------------------------------------------------------------------------------
        # setting widgets
        self.tracker_tab = TrackerTab(self)
        self.m_menu = RightClickMenu(self)

        self.tracker_tab.grid(row=0, column=0)

        # ------------------------------------------------------------------------------
        # setting commands
        self.bind("<ButtonPress-1>",    self.start_move)
        self.bind("<ButtonRelease-1>",  self.stop_move)
        self.bind("<B1-Motion>",        self.move)
        self.bind("<Button-3>",         self.popup)
        self.bind('<Key>',              self.hot_key)
        self.bind('<Escape>',           self.close)

        self.focus_force()

    def hot_key(self, event):

        success = self.tracker_tab.tracker_area.f_success_counter
        fail = self.tracker_tab.tracker_area.f_fail_counter

        if event.char.upper() == hot_keys['add_success']:
            success.btn_add.invoke()

        elif event.char.upper() == hot_keys['subtract_success']:
            success.btn_subtract.invoke()

        elif event.char.upper() == hot_keys['add_fail']:
            fail.btn_add.invoke()

        elif event.char.upper() == hot_keys['subtract_fail']:
            fail.btn_subtract.invoke()

    # ------------------------------------------------------------------------------
    # drag and drop window
    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def stop_move(self, event):
        self.x = None
        self.y = None

    def move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.winfo_x() + deltax
        y = self.winfo_y() + deltay
        self.geometry(f"+{x}+{y}")

    def popup(self, event):
        try:
            self.m_menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.m_menu.grab_release()

    def close(self, event):
        self.parent.destroy()

app = Tk()
app.title("Aronimo's Consistency Tracker")
app.lower()
app.iconify()

main = Main(app)

app.mainloop()