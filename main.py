from __future__ import annotations
import tkinter as tk
import ttk

from grips import MoveGrip, ResizeGrip
from frames import LeftFrame, RightFrame
from handler import Handler
from food import get_food
from Item import Item


class BackgroundWindow(tk.Frame):

  def __init__(self, parent):
    self.parent = parent
    self.root = parent.winfo_toplevel()

    tk.Frame.__init__(self, self.root, bg="#3b3b3b")
    #tk.Frame.__init__(self, self.root, bg="#d900ff")
    self.pack_propagate(0)

    self.move_grip = MoveGrip(self)
    #self.resize_grip = ResizeGrip(self)


  def init(self):
    
    self.move_grip.init()
    #self.resize_grip.init()

    self.pack(fill=tk.BOTH, expand=1)




class BurgNurg(tk.Tk):
  def __init__(self, *args, **kwargs):
    tk.Tk.__init__(self, *args, **kwargs)

    self.geometry("500x300")
    self.resizable(0, 0)
    self.overrideredirect(1)
    self.update()

    self.selected_item = None
    self.hovered_item = None

    self.bind("<Button-1>", self.on_left_click)

    self.background_window = BackgroundWindow(self)
    self.background_window.init()
    

    self.left_frame = LeftFrame(self.background_window)
    self.right_frame = RightFrame(self.background_window)

    test = True
    if test:
      
      self.left_frame.configure(background="#ed0000")
      self.right_frame.configure(background="#00f7ff")

    #self.left_frame.pack(side = tk.LEFT, expand=1)
    #self.right_frame.pack(side = tk.RIGHT)

    
    #jank but idc
    
    #print('test', self.winfo_width(), self.winfo_height() )
    self.left_frame.place(x=0, y=20, anchor="nw", width=self.winfo_width()//2, height=self.winfo_height()-20)
    
    self.right_frame.place(x=self.winfo_width()//2, y=20, anchor="nw", width=self.winfo_width()//2, height=self.winfo_height()-20)
    

    self.left_frame.init()
    #self.right_frame.init()
    self.right_frame.init()

    self.left_frame.place(x=0, y=20, anchor="nw", width=self.winfo_width()//2, height=self.winfo_height()-20)
    
    self.right_frame.place(x=self.winfo_width()//2, y=20, anchor="nw", width=self.winfo_width()//2, height=self.winfo_height()-20)

    '''
    self.left_frame.init()
    #self.right_frame.init()
    self.right_frame.init()

    self.left_frame.place(x=0, y=20, anchor="nw", width=self.winfo_width()//2, height=self.winfo_height()-20)
    
    self.right_frame.place(x=self.winfo_width()//2, y=20, anchor="nw", width=self.winfo_width()//2, height=self.winfo_height()-20)
'''

  def on_left_click(self, event):
    if self.hovered_item:
      self.selected_item = self.hovered_item
      assert(type(self.selected_item) == Item)
      print(f"selected item {self.selected_item.name}")
      self.right_frame.changed_items(self.selected_item)


if __name__ == "__main__":
  app = BurgNurg()
  app.mainloop()
