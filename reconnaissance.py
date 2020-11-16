from apprentissage import *
import tkinter as tk
from tkinter import *
from datasetcreator import *
from identifie import *

class Reconnaissance :

    def __init__(self,root):
        fen_rec = tk.Toplevel(root)
        fen_rec.title("Reconnaissance de personne")
        fen_rec.geometry("+%d+%d" % ((fen_rec.winfo_screenwidth() / 2) - 200, (fen_rec.winfo_screenheight() / 2) - 260))
        btn11 = tk.Button(fen_rec, text="Ajouter une personne au modele", command = Datasetcreator)
        btn11.config(height=10, width=30)
        btn11.pack(side=LEFT)
        btn12 = tk.Button(fen_rec, text="Identifier", command = Apprentissage)
        btn12.config(height=10, width=20)
        btn12.pack(side=LEFT)