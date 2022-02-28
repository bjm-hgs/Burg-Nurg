import tkinter as tk



class ItemInfoFrame(tk.Frame):
  def __init__(self, parent, item, *args, **kwargs):
    self.parent = parent
    print(f"{self.parent=}")
    self.root = parent.winfo_toplevel()
    self.item = item

    tk.Frame.__init__(self, parent, *args, **kwargs)
    

  def hide(self):
    try:
      self.pack_forget()
    except: pass

    try:
      self.grid_forget()
    except: pass

    try:
      self.place_forget()
    except: pass

  def show(self):
    self.pack(fill=tk.BOTH,pady=5)
    self.lift()

  def make_widgets(self):
    self.title = tk.Label(self.parent, text=self.item.name,bg="#FFFFFF")
    self.title.pack(side=tk.TOP)