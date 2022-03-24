import tkinter as tk

from home import HomeScreen
from initialzeExcelDatabases import InitializeExcelDatabases

class OMAS(tk.Tk):
      def __init__(self):
            tk.Tk.__init__(self)
            self.geometry("1500x1000")
            self.title("OMAS")
            self._frame = None
            # self.frames = [
            #       ("initializeExcelWindow", InitializeExcelDatabases),
            #       ("homeScreen", HomeScreen)
            # ]
            self.switch_frame(HomeScreen)

      def switch_frame(self, frame_class):
            """Destroys current frame and replaces it with a new one."""
            new_frame = frame_class(self)
            if self._frame is not None:
                  self._frame.destroy()
            self._frame = new_frame
            self._frame.place(x=0, y=0, width = "1500", height = "1000")

if __name__ == "__main__":
    app = OMAS()
    app.mainloop()