from tkinter import *
from TrackerArea import TrackerArea

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
app.title("Aronimo's Consistency Tracker")
app.overrideredirect(True)
app.resizable(False, False)

mb_menu = Menu(app, bg='#65a696')

m_file = Menu(mb_menu)
mb_menu.add_cascade(label='File', menu=m_file)
m_file.add_command(label='Open')
m_file.add_command(label='Save')
m_file.add_command(label='Exit', command=on_menu_Exit)

app.config(menu=mb_menu)

main = Main(app)
main.grid(row=0, column=0)

app.mainloop()