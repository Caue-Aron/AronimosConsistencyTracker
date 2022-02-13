from tkinter import *
from TrackerArea import TrackerArea
from ctypes import windll

# pyinstaller --onefile main.pyw

# Some WindowsOS styles, required for task bar integration
GWL_EXSTYLE = -20
WS_EX_APPWINDOW = 0x00040000
WS_EX_TOOLWINDOW = 0x00000080

def set_appwindow(mainWindow):
    # Honestly forgot what most of this stuff does. I think it's so that you can see
    # the program in the task bar while using overridedirect. Most of it is taken
    # from a post I found on stackoverflow.
    hwnd = windll.user32.GetParent(mainWindow.winfo_id())
    stylew = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    stylew = stylew & ~WS_EX_TOOLWINDOW
    stylew = stylew | WS_EX_APPWINDOW
    res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, stylew)
    # re-assert the new window style
    mainWindow.wm_withdraw()
    mainWindow.after(10, lambda: mainWindow.wm_deiconify())

def on_menu_Exit():
    app.destroy()

class Main(Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.x = 0
        self.y = 0

        self.lbf_title = LabelFrame(self, relief='ridge')
        self.lb_title = Label(self.lbf_title, text="Aronimo's Consistency Tracker")
        self.tracker_area = TrackerArea(self)

        self.lbf_title.grid(row=0, column=0, pady=(15, 15))
        self.lb_title.grid(row=0, column=0)
        self.tracker_area.grid(row=1, column=0)

        self.parent.bind("<ButtonPress-1>", self.start_move)
        self.parent.bind("<ButtonRelease-1>", self.stop_move)
        self.parent.bind("<B1-Motion>", self.do_move)

        self.parent.bind('<Key>', self.hot_key)

    def hot_key(self, event):
        if event.char.upper() == 'A':
            self.tracker_area.f_success_counter.btn_add.invoke()

        elif event.char.upper() == 'S':
            self.tracker_area.f_success_counter.btn_subtract.invoke()

        elif event.char.upper() == 'Z':
            self.tracker_area.f_fail_counter.btn_add.invoke()

        elif event.char.upper() == 'X':
            self.tracker_area.f_fail_counter.btn_subtract.invoke()

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def stop_move(self, event):
        self.x = None
        self.y = None

    def do_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.parent.winfo_x() + deltax
        y = self.parent.winfo_y() + deltay
        self.parent.geometry(f"+{x}+{y}")

app = Tk()
app.after(10, lambda: set_appwindow(app))
app.title("Aronimo's Consistency Tracker")
# app.overrideredirect(True)
app.resizable(False, False)

mb_menu = Menu(app)

m_file = Menu(mb_menu)
mb_menu.add_cascade(label='File', menu=m_file)
m_file.add_command(label='Open')
m_file.add_command(label='Save')
m_file.add_command(label='Exit', command=on_menu_Exit)

app.config(menu=mb_menu)

main = Main(app)
main.grid(row=0, column=0)

app.mainloop()