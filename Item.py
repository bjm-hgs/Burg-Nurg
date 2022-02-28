from __future__ import annotations
import tkinter as tk
from PIL import Image, ImageTk
from item_info_frame import ItemInfoFrame


class Item:
  def __init__(self, name, price, image, description): # price in pounds
    self.name = name
    self.price = price
    self.description = description
    self.image = image
    

  def make_button(self, *args, width=None, height=None, root=None, **kwargs):
    self.root=root
    img = Image.open(self.image)
    img = img.resize((width,height))
    #print(img.width + img.height)
    photo = ImageTk.PhotoImage(img)
    button = tk.Button(*args, image=photo, width=width, height=height, **kwargs)
    button.image = photo #stops garbage collection

    #jank button click stuff but was too difficult to implement normally with lambda garbage collection
    button.bind("<Enter>", self.on_enter)
    button.bind("<Leave>", self.on_leave)
    return button

  def make_frame(self, parent, *args, **kwargs):
    frame = ItemInfoFrame(parent, self, *args, **kwargs)




    return frame
  

  def on_enter(self, event):
    self.root.hovered_item = self
    #print(f"mouse entered {self.name}")
    #print(f"{self.root.hovered_item.name=}")
    #print(f"{self.root.selected_item.name=}")

  def on_leave(self, event):
    #print(f"mouse left {self.name}")
    if self.root.hovered_item == self:
      self.root.hovered_item = None
    