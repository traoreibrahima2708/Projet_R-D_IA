from tkinter import *
import tkinter as tk
from PIL import Image,ImageChops,ImageOps, ImageTk
from meli import *
from detection import *
from mosaique import *
from reconnaissance import *

class Fds :

    def __init__(self,root):

        fete=tk.Toplevel(root)
        fete.title("Fete de la Science")
        fete.geometry("+%d+%d" % (fete.winfo_screenwidth() / 4, (fete.winfo_screenheight() / 2) -
                                  60))

        btn11 = tk.Button(fete, text="Mosaique", command = lambda : Mosaique(fete))
        btn11.config(height=10, width=20)
        btn11.pack(side=LEFT)
        btn12 = tk.Button(fete, text="Melimelo d'image", command = lambda : Melimelo(fete))
        btn12.config(height=10, width=20)
        btn12.pack(side=LEFT)
        btn13 = tk.Button(fete, text="Detection d'objet",command = lambda : Detection(fete))
        btn13.config(height=10, width=20)
        btn13.pack(side=LEFT)
        btn14 = tk.Button(fete, text="Reconnaissance faciale", command = lambda : Reconnaissance(fete))
        btn14.config(height=10, width=20)
        btn14.pack(side=LEFT)

        fete.resizable(width=False, height=False)
        fete.transient(root)
        fete.mainloop()
