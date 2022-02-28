from __future__ import annotations
import tkinter as tk
from food import get_food
import random

food = get_food()
random.shuffle(food)

#contains items to pick
class LeftFrame(tk.Frame):
  def __init__(self, parent, *args, **kwargs):
    self.parent = parent
    self.root = parent.winfo_toplevel()
  
    tk.Frame.__init__(self, self.parent, *args, **kwargs)

    self.config(bg = self.parent["bg"])

  
  def init(self):
    #say we want three items per row
    #count = items per row
    #button height equals width (because we want square buttons)
    #width = parent.width//count
    #we want to pack three horizontally and then go down one
    #grid_frames = []
    #for button in buttons:
    #  new_frame = tk.Frame()
    #  for _ in range(count):
    #    get_button(parent) #somehow
    #    button.pack(side=tk.RIGHT)
    #  grid_frames.append(new_frame)

    self.update()

    BUTTONS_PER_LINE = 1
    while True:

      #print(self.winfo_width())
      button_size = self.winfo_width()//(BUTTONS_PER_LINE) - 6 #-6 is dirty fix
  
      #print(f"{button_size=}")

      #print(f"{button_size * BUTTONS_PER_LINE=}")
      #print(f"{self.winfo_height()}")
      if button_size * (len(food)//BUTTONS_PER_LINE) > self.winfo_height():
        BUTTONS_PER_LINE += 1
      else:
        break

    food_gen = (item for item in food)

    self.main_grid_frame = tk.Frame(self)
    self.grid_frames = []
    finished = False
    self.temp_food_items = [] #wierd variable reference stuff
    
    while not finished:
      new_frame = tk.Frame(self.main_grid_frame)
      for _ in range(BUTTONS_PER_LINE):
        try:
          food_item = next(food_gen)

          self.temp_food_items.append(food_item)
          food_index = food.index(food_item)
          
          button = food_item.make_button(new_frame,
                                         width=button_size,
                                         height=button_size,
                                         root=self.root
                                        )
          
          #print(button["width"])
          button.pack(side=tk.RIGHT)
        except StopIteration:
          finished = True
          break

      self.grid_frames.append(new_frame)
      new_frame.pack(side=tk.TOP)

      #tried to center vertically but i'm bad ;-;
      self.main_grid_frame.grid(row=0, column=0, sticky="")
      self.main_grid_frame.grid_rowconfigure(0, weight=1)
      self.main_grid_frame.grid_columnconfigure(0, weight=1)
















      

#contains logic stuff (e.g. order sum etc)
class RightFrame(tk.Frame):
  def __init__(self, parent, *args, **kwargs):
    self.parent = parent
    self.root = parent.winfo_toplevel()
    
    tk.Frame.__init__(self, self.parent, *args, **kwargs)

    self.config(bg = self.parent["bg"])

    self.upper_right_frame = UpperRightFrame(self)

    self.lower_right_frame = LowerRightFrame(self)

    self.total = tk.StringVar(self.root)
    self.items = tk.StringVar(self.root)
    self.total_label = tk.Label(self, text = self.total)
    self.items_label = tk.Label(self, text = self.items)

    self.item_info_frame = None

    self.init()

  def init(self):

    self.upper_right_frame.place(x=0, y=0, anchor="nw", width=self.winfo_width(), height=self.winfo_height()//2)

    self.lower_right_frame.place(x=0, y=self.winfo_height()//2, anchor="nw", width=self.winfo_width(), height=self.winfo_height()//2)



  def changed_items(self, item):
    self.item_info_frame = item.make_frame(self)
    self.item_info_frame.show()

    

    



class UpperRightFrame(tk.Frame):
  def __init__(self, parent, *args, **kwargs):
    self.parent = parent
    self.root = parent.winfo_toplevel()
    
    tk.Frame.__init__(self, self.parent, *args, **kwargs)

    #self.config(bg = self.parent["bg"])
    self.config(bg = "#d900ff")

  def init(self):
    pass


class LowerRightFrame(tk.Frame):
  def __init__(self, parent, *args, **kwargs):
    self.parent = parent
    self.root = parent.winfo_toplevel()
    
    tk.Frame.__init__(self, self.parent, *args, **kwargs)

    #self.config(bg = self.parent["bg"])
    self.config(bg = "#00ff26")

  def init(self):
    pass
    