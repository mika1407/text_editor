import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *

def changeColor():
  color = colorchooser.askcolor(title="pick a text color")
  textArea.config(fg=color[1])

def changeFont(*args):
    textArea.config(font=(font_name.get(), size_box.get()))

def newFile():
   window.title("Untitled")
   textArea.delete(1.0, END)


def saveFile():
   file = filedialog.asksaveasfilename(initialfile="untitled.txt",
                                        defaultextension='.txt',
                                        filetypes=[
                                            ("Text file","*.txt"),
                                            ("HTML file",".html"),
                                            ("All Files", ".*"),
                                        ])
   if file is None:
      return
   else:
      try:
        window.title(os.path.basename(file))
        file = open(file, "w")
        
        filetext = str(textArea.get(1.0,END))
        file.write(filetext)
      except Exception:
         print("couldn't save file")
      finally:
        file.close()

def openFile():
   file = askopenfilename(defaultextension=".txt",
                                         title="Open file",
                                         file=[("Text files","*.txt"),
                                         ("All Files","*.*")]) 
   try:
      window.title(os.path.basename(file))
      textArea.delete(1.0, END)

      file = open(file, "r")

      textArea.insert(1.0, file.read())

   except Exception:
      print("couldn't read file")
   finally:
      file.close()

def cut():
   textArea.event_generate("<<Cut>>")
def copy():
   textArea.event_generate("<<Copy>>")
def paste():
   textArea.event_generate("<<Paste>>")

def about():
   showinfo("About this program", "This is a text editor program written by Mika Tiihonen.")
def quit():
   window.destroy()

##### Window start here
window = Tk()

newImage = PhotoImage(file="files.png")
openImage = PhotoImage(file="files.png")
saveImage = PhotoImage(file="save.png")

window.title("Text editor program")
window_width = 500
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

font_name = StringVar(window)
font_name.set("Arial")

font_size = StringVar(window)
font_size.set("20")


textArea = Text(window,
            bg="light yellow",
            font=(font_name.get(), font_size.get()),
            height=12,
            width=32,
            padx=5,
            pady=5,
            fg="purple")

scroll_bar = Scrollbar(textArea)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
textArea.grid(sticky=N + E + S + W)
scroll_bar.pack(side=RIGHT, fill=Y)
textArea.config(yscrollcommand=scroll_bar.set)

frame = Frame(window)
frame.grid()

color_button = Button(frame, text="color", command=changeColor)
color_button.grid(row=0, column=0)

font_box = OptionMenu(frame, font_name, *font.families(), command=changeFont)
font_box.grid(row=0, column=1)

size_box = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=changeFont)
size_box.grid(row=0, column=2)

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar,tearoff=0,font=("MV Boli",10))
menubar.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="New", command=newFile,image=newImage,compound='left')
fileMenu.add_command(label="Open",command=openFile,image=openImage,compound='left')
fileMenu.add_command(label="Save",command=saveFile,image=saveImage,compound='left')
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quit)

editMenu = Menu(menubar,tearoff=0,font=("MV Boli",10))
menubar.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Cut",command=cut)
editMenu.add_command(label="Copy",command=copy)
editMenu.add_command(label="Paste",command=paste)

helpMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="About", command=about)

window.mainloop()

