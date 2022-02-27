import tkinter as tk
import ttk



#i'm not bad code, stop staring at me baka!! >.<

#https://stackoverflow.com/questions/53641648/tkinter-python-3-moving-a-borderless-window
class MoveGrip:
  ''' Makes a window dragable. '''
  def __init__(self, real_parent, disable=None, releasecmd=None):
    self.top_Frame = tk.Frame(real_parent, bg="#1a1a1a", width=real_parent.winfo_toplevel().winfo_width(),height=20)

    self.parent = self.top_Frame
    self.root = self.parent.winfo_toplevel()

    self.disable = disable
    if type(disable) == 'str':
        self.disable = disable.lower()

    self.releaseCMD = releasecmd

    self.parent.bind('<Button-1>', self.relative_position)
    self.parent.bind('<ButtonRelease-1>', self.drag_unbind)
    
    self.ext_but = tk.Button(self.top_Frame, text="X", bg="#363636", fg="#a3a3a3", command=lambda: self.root.destroy())

    self.min_but = tk.Button(self.top_Frame, text="-", bg="#363636", fg="#a3a3a3", command=lambda: self.minimize())

    self.root.bind('<Map>', self.overrideredirect_if_mapped)
    

  def init(self):
    #self.top_Frame.place(x=0, y=0, anchor="nw", width=self.root.winfo_width(), height=20)
    self.top_Frame.pack(side=tk.TOP, anchor="nw")
    
    self.ext_but.place(x=self.root.winfo_width()-30, y=0, anchor="nw", width=30, height=20)

    self.min_but.place(x=self.root.winfo_width()-60, y=0, anchor="nw", width=30, height=20)
  

  def relative_position (self, event) :
      cx, cy = self.parent.winfo_pointerxy()
      geo = self.root.geometry().split("+")
      print(geo)
      self.oriX, self.oriY = int(geo[1]), int(geo[2])
      self.relX = cx - self.oriX
      self.relY = cy - self.oriY

      self.parent.bind('<Motion>', self.drag_wid)

  def drag_wid (self, event) :
      cx, cy = self.parent.winfo_pointerxy()
      d = self.disable
      x = cx - self.relX
      y = cy - self.relY
      if d == 'x' :
          x = self.oriX
      elif d == 'y' :
          y = self.oriY
      self.root.geometry('+%i+%i' % (x, y))

  def drag_unbind (self, event) :
      self.parent.unbind('<Motion>')
      if self.releaseCMD != None :
          self.releaseCMD()

  #https://stackoverflow.com/questions/29186327/tclerror-cant-iconify-override-redirect-flag-is-set
  def minimize(self):
    self.root.overrideredirect(False)
    self.root.iconify()
    
  def overrideredirect_if_mapped(self, event):
    #happens when window goes back into focus after being minimized
    #print(f"mapped. root state is {self.root.wm_state()}")
    if self.root.wm_state() == "normal":
      #remove border again (iconify needs to remove overrideredirect to work)
      self.root.overrideredirect(True)




#https://stackoverflow.com/questions/22421888/tkinter-windows-without-title-bar-but-resizable
class ResizeGrip:
  ''' Makes a window dragable. '''
  def __init__ (self, parent, disable=None, releasecmd=None) :
    self.parent = parent
    self.root = parent.winfo_toplevel()

    self.grip = ttk.Sizegrip(self.root)

  def init(self):
    self.grip.place(relx=1.0, rely=1.0, anchor="se")
    self.grip.lift()
    self.grip.bind("<B1-Motion>", self.OnMotion)

  def OnMotion(self, event):
    x1 = self.root.winfo_pointerx()
    y1 = self.root.winfo_pointery()
    x0 = self.root.winfo_rootx()
    y0 = self.root.winfo_rooty()
    self.root.geometry("%sx%s" % ((x1-x0),(y1-y0)))