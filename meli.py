from tkinter import *
import tkinter as tk
from pathlib import Path
from PIL import Image, ImageTk
import random
from numpy import *
from glob import *

class Melimelo :

    def __init__(self,root):

        def sol_meli():
            p1 = Label(meli, image=im1, height=250, width=250)
            p1.grid(column=1,row=0,padx=20)
            p2 = Label(meli, image=im2, height=250, width=250)
            p2.grid(column=3,row=0,padx=15)
            p3 = Label(meli, image=im3, height=250, width=250)
            p3.grid(column=2,row=1,padx=0)
            solution.destroy()

        chemin = Path('/Users/vince/Desktop/Demonstrateur/Photos/Nature')

        random_filename1 = random.choice(list(chemin.glob('*.bmp')))
        random_filename2 = random.choice(list(chemin.glob('*.bmp')))
        random_filename3 = random.choice(list(chemin.glob('*.bmp')))

        while random_filename2 == random_filename1:
            random_filename2 = random.choice(list(chemin.glob('*.bmp')));

        while random_filename3 == random_filename1 or random_filename3 == random_filename2:
            random_filename3 = random.choice(list(chemin.glob('*.bmp')));

        image1 = Image.open(random_filename1)
        new1 = image1.resize((300, 300), Image.ANTIALIAS)
        im1 = ImageTk.PhotoImage(new1)

        image2 = Image.open(random_filename2)
        new2 = image2.resize((300, 300), Image.ANTIALIAS)
        im2 = ImageTk.PhotoImage(new2)
        image3 = Image.open(random_filename3)
        new3 = image3.resize((300, 300), Image.ANTIALIAS)
        im3 = ImageTk.PhotoImage(new3)

        # récupération de la largeur et hauteur de l'image 1
        colonne1, ligne1 = image1.size
        # récupération de la largeur et hauteur de l'image 2
        colonne2, ligne2 = image2.size
        # récupération de la largeur et hauteur de l'image 2
        colonne3, ligne3 = image3.size

        # calcul des dimensions de l'image fusionnée
        colonne = min(colonne1, colonne2, colonne3)
        ligne = min(ligne1, ligne2, ligne3)

        # création d'une image de même type
        imgF = Image.new(image1.mode, (colonne, ligne))

        # boucle de traitement des pixels
        for i in range(ligne):
            for j in range(colonne):
                p1 = image1.getpixel((j, i))
                p2 = image2.getpixel((j, i))
                p3 = image3.getpixel((j, i))
                p = (p1[0], p2[1], p3[2])
                imgF.putpixel((j, i), p)


        meli=tk.Toplevel(root,bg = "gray")
        meli.title("Melimelo d'images")
        meli.resizable(width=False, height=False)
        meli.geometry("%dx%d" % (meli.winfo_screenwidth(), meli.winfo_screenheight()))
        melimelo = ImageTk.PhotoImage(imgF)
        panel = Label(meli, image=melimelo,height=512,width=512)
        panel.grid(column=0,row=0,pady=30,padx=10)
        solution = tk.Button(meli, text = "Solution",command = sol_meli)
        solution.config( height = 4, width =50)
        solution.grid(column=0,row=1,pady=20)
        meli.transient(root)
        meli.mainloop()



