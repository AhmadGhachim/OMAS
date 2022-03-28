import os
import tkinter as tk

from HomeScreen import HomeScreen
from frontend.InitialzeExcelDatabases import InitializeExcelDatabases

path = os.path.abspath(os.path.pardir)
path = path.replace("\\", "/", path.count("\\"))

class OMAS(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("1350x900")
        self.title("OMAS")
        self._frame = None
        if "Excel files" in os.listdir(path+"/backend"):
            self.switch_frame(HomeScreen)
        else:
            self.switch_frame(InitializeExcelDatabases)
            tk.messagebox.showinfo(title="Welcome!",message="Please start by providing details of the classes you are mentoring")
        # self.bind_all("<Button-1>", lambda event: event.widget.focus_set())

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.place(x=0, y=0, width="1350", height="900")


if __name__ == "__main__":
    app = OMAS()
    app.mainloop()
