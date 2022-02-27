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

      print(self.winfo_width())
      button_size = self.winfo_width()//(BUTTONS_PER_LINE) - 6 #-6 is dirty fix
  
      print(f"{button_size=}")

      print(f"{button_size * BUTTONS_PER_LINE=}")
      print(f"{self.winfo_height()}")
      if button_size * (len(food)//BUTTONS_PER_LINE) > self.winfo_height():
        BUTTONS_PER_LINE += 1
      else:
        break

    food_gen = (item for item in food)
    
    self.grid_frames = []
    finished = False
    while not finished:
      new_frame = tk.Frame(self)
      for _ in range(BUTTONS_PER_LINE):
        try:
          button = next(food_gen).make_button(new_frame, width=button_size, height=button_size)
          print(button["width"])
          button.pack(side=tk.RIGHT)
        except StopIteration:
          finished = True
          break

      self.grid_frames.append(new_frame)
      new_frame.pack(side=tk.TOP)


#contains logic stuff (e.g. order sum etc)
class RightFrame(tk.Frame):
  def __init__(self, parent, *args, **kwargs):
    self.parent = parent
    self.root = parent.winfo_toplevel()
    
    tk.Frame.__init__(self, self.parent, *args, **kwargs)

    self.config(bg = self.parent["bg"])

    self.total = tk.StringVar(self.root)
    self.items = tk.StringVar(self.root)
    self.total_label = tk.Label(self, text = self.total)
    self.items_label = tk.Label(self, text = self.items)

  def init(self):
    self.total_label.pack(side=tk.TOP)
    self.items_label.pack(side=tk.TOP)




class ItemInfoFrame(tk.Frame):
  def __init__(self, parent, *args, **kwargs):
    self.