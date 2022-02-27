import tkinter as tk
from PIL import Image, ImageTk


class Item:
  def __init__(self, name, price, image, description): # price in pounds
    self.name = name
    self.price = price
    self.description = description
    self.image = image
    

  def make_button(self, *args, width=None, height=None, **kwargs):
    img = Image.open(self.image)
    img = img.resize((width,height))
    print(img.width + img.height)
    photo = ImageTk.PhotoImage(img)
    button = tk.Button(*args, image=photo, width=width, height=height, **kwargs)
    button.image = photo #stops garbage collection
    return button