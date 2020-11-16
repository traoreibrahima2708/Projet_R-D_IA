from tkinter import *
import tkinter as tk
from PIL import Image,ImageChops,ImageOps, ImageTk
from Img import *

class Trait:

    def __init__(self,root):
        filename = filedialog.askopenfilename(initialdir="/", title="Selectionnez une image",
                                                  filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

        Im = Img(filename)

        trait = tk.Toplevel(root)
        trait.title("Traitements d'images")
        trait.geometry("%dx%d" % (trait.winfo_screenwidth(), trait.winfo_screenheight()))
        ## Déclaration des éléments graphique de type menu
        menubar = Menu(trait)
        trait['menu'] = menubar
        Fichier = Menu(menubar)
        Traitement = Menu(menubar)
        Couleur = Menu(menubar)
        Texture = Menu(menubar)
        Contour = Menu(menubar)
        Aide = Menu(menubar)
        Change_palette = Menu(Couleur)
        Change_color = Menu(Couleur)

        can2 = Canvas(trait, bg="white")
        can2.pack(side=tk.TOP, fill=BOTH, expand=True)
        can2.image = Im.getImagetk()
        can2.create_image(trait.winfo_screenwidth()/4, 0, anchor=NW, image=Im.getImagetk())

        ## Ajout d'un onglet Fichier
        menubar.add_cascade(label="Fichier", menu=Fichier)
        Fichier.add_command(label="Enregistrer_sous", command=exit)
        Fichier.add_command(label="Quitter", command=exit)

        ## Ajout d'un onglet Traitement
        menubar.add_cascade(label="Traitement", menu=Traitement)
        Traitement.add_command(label="Egalisation d'histogramme", command=Im.egalisation)
        Traitement.add_command(label="Reconaissance de lettres", command=exit)
        Traitement.add_command(label="Segmentation", command=Im.segmentation)

        ## Ajout d'un onglet Couleur
        menubar.add_cascade(label="Couleur", menu=Couleur)
        Couleur.add_command(label="Negatif", command=Im.negatif)
        Couleur.add_command(label="Niveau de gris", command=Im.niveauGris)
        Couleur.add_cascade(label="Changement de palette", menu=Change_palette)
        Change_palette.add_command(label="Automne", command=Im.autumn)
        Change_palette.add_command(label="Arc en ciel", command=Im.rainbow)
        Change_palette.add_command(label="Bone", command=Im.bone)
        Change_palette.add_command(label="Cool", command=Im.cool)
        Change_palette.add_command(label="Hot", command=Im.hot)
        Change_palette.add_command(label="HSV", command=Im.hsv)
        Change_palette.add_command(label="Jet", command=Im.jet)
        Change_palette.add_command(label="Ocean", command=Im.ocean)
        Change_palette.add_command(label="Pink", command=Im.pink)
        Change_palette.add_command(label="Printemps", command=Im.spring)
        Change_palette.add_command(label="Ete", command=Im.summer)
        Change_palette.add_command(label="Hiver", command=Im.winter)

        ## Ajout d'un onglet Texture
        menubar.add_cascade(label="Texture", menu=Texture)
        Texture.add_command(label="Camouflage", command=Im.camo)

        ## Ajout d'un onglet Contours
        menubar.add_cascade(label="Contours", menu=Contour)
        Contour.add_command(label="Extraction", command=Im.extraction)
        Contour.add_command(label="Detection", command=Im.detection)

        ## Ajout d'un onglet A propos de
        menubar.add_cascade(label="?", menu=Aide)
        Aide.add_command(label="A propos de ...", command=exit)

        trait.transient(root)
        trait.mainloop()







