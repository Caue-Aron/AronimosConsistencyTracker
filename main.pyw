from tkinter import *
from TrackerTab import TrackerTab
from tkinter import ttk

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
        # adding menu cascade
        self.mb_menu = Menu(self)
        self.config(menu=self.mb_menu)

        self.m_file = Menu(self.mb_menu, tearoff=False)
        self.mb_menu.add_cascade(label='File', menu=self.m_file)

        self.m_file.add_command(label='Open')
        self.m_file.add_command(label='Save')
        self.m_file.add_command(label='Exit', command=self.on_menu_Exit)

        # ------------------------------------------------------------------------------
        # setting widgets
        self.tracker_tab = TrackerTab(self)

        self.tracker_tab.grid(row=0, column=0)

        # ------------------------------------------------------------------------------
        # setting commands
        self.bind("<ButtonPress-1>",    self.start_move)
        self.bind("<ButtonRelease-1>",  self.stop_move)
        self.bind("<B1-Motion>",        self.do_move)

        self.bind('<Key>', self.hot_key)

    def hot_key(self, event):

        success = self.tracker_tab.tracker_area.f_success_counter
        fail = self.tracker_tab.tracker_area.f_fail_counter

        if event.char.upper() == 'A':
            success.btn_add.invoke()

        elif event.char.upper() == 'S':
            success.btn_subtract.invoke()

        elif event.char.upper() == 'Z':
            fail.btn_add.invoke()

        elif event.char.upper() == 'X':
            fail.btn_subtract.invoke()

    # ------------------------------------------------------------------------------
    # drag and drop window
    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def stop_move(self, event):
        self.x = None
        self.y = None

    def do_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.winfo_x() + deltax
        y = self.winfo_y() + deltay
        self.geometry(f"+{x}+{y}")

    # ------------------------------------------------------------------------------
    # menu bar commands
    def on_menu_Exit(self):
        self.parent.destroy()

app = Tk()
app.title("Aronimo's Consistency Tracker")
app.lower()
app.iconify()

main = Main(app)

app.mainloop()