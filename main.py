from tkinter import *
from PIL import Image, ImageTk
import random

N = [str(random.randint(0,2)) for __ in range(4)]
def is_valid(newval):
    global N
    if len(newval) == 4:
        if newval == ''.join(N):
            N = [str(random.randint(0, 2)) for __ in range(4)]
            img2 = ImageTk.PhotoImage(Image.open('cards/' + ''.join(N) + '.png'))
            lbl.configure(image=img2)
            lbl.image = img2
    return True


window = Tk()

check = (window.register(is_valid), "%P")

image_file = Image.open('cards/' + ''.join(N) + '.png')
vp_image = ImageTk.PhotoImage(image_file)
lbl = Label(image=vp_image)
lbl.grid(row=0, column=0)

ntr = Entry(justify=CENTER, validate="all", validatecommand=check)
ntr.grid(row=1, column=0)

mainloop()

while True:
    print(ntr.get())
