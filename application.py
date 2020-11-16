from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image,ImageChops,ImageOps, ImageTk
from fds import *
from trait import *

class Application:

    def __init__(self):

        ##### Programme principal #####

        ## Création de la fenêtre principale avec son titre et ses dimensions
        self.root = tk.Tk()
        self.root.title("Demonstrateur de traitements d'image")
        self.root.geometry("%dx%d" % (self.root.winfo_screenwidth(), self.root.winfo_screenheight()))

        ## Ajout de l'image de fonc
        self.can = Canvas(self.root, bg="white")
        self.can.pack(side=TOP, fill=BOTH, expand=True)
        imageFile = Image.open("PosterTEX_V1.jpg")
        imageFile = imageFile.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.ANTIALIAS)
        imageFile = ImageTk.PhotoImage(imageFile)
        self.can.image = imageFile
        self.can.create_image(self.root.winfo_width() / 2, self.root.winfo_height() / 2, anchor=NW, image=imageFile)

        im_fete = Image.open("/Users/vince/Downloads/fete-de-la-science_titre.jpg")
        im_fete = im_fete.resize((300, 200), Image.ANTIALIAS)
        im_fete = ImageTk.PhotoImage(im_fete)
        ## Ajout des boutons permettant d'ouvrir les fenêtres secondaires
        bt1 = Button(self.root, image=im_fete, bg='gray', command=lambda: Fds(self.root))
        # bt1.config(height=10, width=30)
        bt1_w = self.can.create_window(self.root.winfo_screenheight() / 2 - 130, self.root.winfo_screenheight() / 2,
                                       window=bt1)

        bt2 = Button(self.root, text="Autres traitements", bg='gray', command=lambda: Trait(self.root))
        bt2.config(height=10, width=30)
        bt2_w = self.can.create_window(self.root.winfo_screenheight() + 230, self.root.winfo_screenheight() / 2,
                                       window=bt2)
        self.root.resizable(width=False, height=False)
        self.root.mainloop()
