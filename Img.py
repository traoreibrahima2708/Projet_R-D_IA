from tkinter import *
import tkinter as tk
from PIL import *
from PIL import Image,ImageChops,ImageOps, ImageTk
import cv2
import matplotlib.pyplot as plt
from pathlib import Path
import random
import numpy as np
from numpy import *
import os
from os import *
from glob import *
import pytesseract

class Img:

    def __init__(self,nom):
        self.nom_fic = nom
        self.image = Image.open(nom)
        self.image = self.image.resize((700, 700), Image.ANTIALIAS)
        self.imagetk = ImageTk.PhotoImage(self.image)
        self.imagecv = cv2.imread(self.nom_fic, 0)
        self.imagecv = cv2.resize(self.imagecv, (1000, 1000))
        self.im_gray = cv2.imread(self.nom_fic, cv2.IMREAD_GRAYSCALE)


    def getImage(self):
        return self.image

    def getImagetk(self):
        return self.imagetk


    def egalisation(self):

        # img = chargez_image_from_PIL('myImage.jpg', resize=(500,400))
        equ = cv2.equalizeHist(self.imagecv)  # appel à la fonction equalisation du opencv

        ##Affichage de l'image d'origine et de l'image traitée
        plt.imshow(equ, cmap = 'gray')
        plt.title(' Image égalisée'), plt.xticks([]), plt.yticks([])
        plt.show()

    ###### Segmentation

    def segmentation(self):
        bords = cv2.Canny(self.imagecv, 250, 250)
        ##Affichage de l'image d'origine et de l'image traitée
        plt.imshow(bords, cmap = 'gray')
        plt.title(' Image segmentée'), plt.xticks([]), plt.yticks([])
        plt.show()


    def negatif(self):

        # récupération de la largeur et hauteur de l'image
        colonne, ligne = self.image.size

        # création d'une image de même type
        imgF = Image.new(self.image.mode, self.image.size)

        # boucle de traitement des pixels
        for i in range(ligne):
            for j in range(colonne):
                pixel = self.image.getpixel((j, i))
                # on calcule le complement à MAX pour chaque composante - effet négatif
                p = (255 - pixel[0], 255 - pixel[1], 255 - pixel[2])
                # composition de la nouvelle image
                imgF.putpixel((j, i), p)

        # la fonction de PIL qui fait la même chose
        # imgF = ImageChops.invert(img)

        # affichage de l'image
        plt.imshow(imgF)
        plt.show()


    def niveauGris(self):
        # affichage de l'image
        plt.imshow(self.im_gray)
        plt.colorbar()
        plt.show()


    def autumn(self):
        ## Recoloration de l'image en niveau de gris
        im_color = cv2.applyColorMap(self.imagecv, cv2.COLORMAP_AUTUMN)
        ##Affichage de l'image d'origine et de l'image traitée
        plt.imshow(im_color, cmap = 'gray')
        plt.show()

    def rainbow(self):
        ## Recoloration de l'image en niveau de gris
        im_color = cv2.applyColorMap(self.imagecv, cv2.COLORMAP_RAINBOW)
        ##Affichage de l'image d'origine et de l'image traitée
        plt.imshow(im_color)
        plt.show()

    def bone(self):
        ## Recoloration de l'image en niveau de gris
        im_color = cv2.applyColorMap(self.imagecv, cv2.COLORMAP_BONE)
        ##Affichage de l'image d'origine et de l'image traitée
        plt.imshow(im_color)
        plt.show()

    def cool(self):
        ## Recoloration de l'image en niveau de gris
        im_color = cv2.applyColorMap(self.imagecv, cv2.COLORMAP_COOL)
        ##Affichage de l'image d'origine et de l'image traitée
        plt.imshow(im_color)
        plt.show()

    def hot(self):
        ## Recoloration de l'image en niveau de gris
        im_color = cv2.applyColorMap(self.imagecv, cv2.COLORMAP_HOT)
        ##Affichage de l'image d'origine et de l'image traitée
        plt.imshow(im_color)
        plt.show()

    def hsv(self):
        ## Recoloration de l'image en niveau de gris
        im_color = cv2.applyColorMap(self.imagecv, cv2.COLORMAP_HSV)
        ##Affichage de l'image d'origine et de l'image traitée
        plt.imshow(im_color)
        plt.show()

    def jet(self):
        ## Recoloration de l'image en niveau de gris
        im_color = cv2.applyColorMap(self.imagecv, cv2.COLORMAP_JET)
        ##Affichage de l'image d'origine et de l'image traitée
        plt.imshow(im_color)
        plt.show()

    def ocean(self):
        ## Recoloration de l'image en niveau de gris
        im_color = cv2.applyColorMap(self.imagecv, cv2.COLORMAP_OCEAN)
        ##Affichage de l'image d'origine et de l'image traitée
        plt.imshow(im_color)
        plt.show()

    def pink(self):
        ## Recoloration de l'image en niveau de gris
        im_color = cv2.applyColorMap(self.imagecv, cv2.COLORMAP_PINK)
        ##Affichage de l'image d'origine et de l'image traitée
        plt.imshow(im_color)
        plt.show()

    def spring(self):
        ## Recoloration de l'image en niveau de gris
        im_color = cv2.applyColorMap(self.imagecv, cv2.COLORMAP_SPRING)
        ##Affichage de l'image d'origine et de l'image traitée
        plt.imshow(im_color)
        plt.show()

    def summer(self):
        ## Recoloration de l'image en niveau de gris
        im_color = cv2.applyColorMap(self.imagecv, cv2.COLORMAP_SUMMER)
        ##Affichage de l'image d'origine et de l'image traitée
        plt.imshow(im_color)
        plt.show()

    def winter(self):
        ## Recoloration de l'image en niveau de gris
        im_color = cv2.applyColorMap(self.imagecv, cv2.COLORMAP_WINTER)
        ##Affichage de l'image d'origine et de l'image traitée
        plt.imshow(im_color)
        plt.show()

    def camo(self):
        ## Chemins des répertoire contenant les images de silouhettes et textures
        path1 = Path('/Users/vince/Desktop/Demonstrateur/Photos/Silhouettes')
        path2 = Path('/Users/vince/Desktop/Demonstrateur/Photos/Textures')
        ## Choix aléatoire d'une silouhette et de deux textures
        random_filename1 = random.choice(list(path1.glob('*.bmp')))
        random_filename2 = random.choice(list(path2.glob('*.bmp')))
        random_filename3 = random.choice(list(path2.glob('*.bmp')))

        while random_filename2 == random_filename3:
            random_filename2 = random.choice(list(path.glob('*.bmp')));

        image1 = Image.open(random_filename1)
        image2 = Image.open(random_filename2)
        image3 = Image.open(random_filename3)

        # récupération de la largeur et hauteur de l'image 1
        colonne1, ligne1 = image1.size
        # récupération de la largeur et hauteur de l'image 2
        colonne2, ligne2 = image2.size
        # récupération de la largeur et hauteur de l'image 3
        colonne3, ligne3 = image3.size

        # calcul des dimensions de l'image fusionnée
        colonne = min(colonne1, colonne2, colonne3)
        ligne = min(ligne1, ligne2, ligne3)

        # création d'une image de même type
        img1 = Image.new(image1.mode, (colonne, ligne))
        img2 = Image.new(image1.mode, (colonne, ligne))
        imgF = Image.new(image1.mode, (colonne, ligne))

        # boucle de traitement des pixels
        for i in range(ligne):
            for j in range(colonne):
                S = image1.getpixel((j, i))
                T1 = image2.getpixel((j, i))
                T2 = image3.getpixel((j, i))
                Si1 = (S[0] + T1[0], S[1] + T1[1], S[2] + T1[2])
                Si2 = ((255 - S[0]) + T2[0], (255 - S[1]) + T2[1], (255 - S[2]) + T2[2])
                img1.putpixel((j, i), Si1)
                img2.putpixel((j, i), Si2)

        for i in range(ligne):
            for j in range(colonne):
                Z1 = img1.getpixel((j, i))
                Z2 = img2.getpixel((j, i))

                if Z1 == (255, 255, 255):
                    Z1 = (0, 0, 0)

                if Z2 == (255, 255, 255):
                    Z2 = (0, 0, 0)

                # l'image Finale

                SF = (Z1[0] + Z2[0], Z1[1] + Z2[1], Z1[2] + Z2[2])
                imgF.putpixel((j, i), SF)

        plt.subplot(221), plt.imshow(imgF)
        plt.title(' Image traitée'), plt.xticks([]), plt.yticks([])
        plt.subplot(222), plt.imshow(image1)
        plt.title(' Image 1'), plt.xticks([]), plt.yticks([])
        plt.subplot(223), plt.imshow(image2)
        plt.title(' Image 2'), plt.xticks([]), plt.yticks([])
        plt.subplot(224), plt.imshow(image3)
        plt.title(' Image 3'), plt.xticks([]), plt.yticks([])
        plt.show()

    def extraction(self):
        def Norme(p1, p2, p3, p4):
            n = sqrt((p1[0] - p3[0]) * (p1[0] - p3[0]) + (p2[0] - p4[0]) * (p2[0] - p4[0]))
            return n

        colonne, ligne = self.image.size
        contour = Image.new(self.image.mode, self.image.size)

        # extraction des contours en niveau de gris
        seuil = 15
        for i in range(1, ligne - 1):
            for j in range(1, colonne - 1):
                p1 = self.image.getpixel((j - 1, i))
                p2 = self.image.getpixel((j, i - 1))
                p3 = self.image.getpixel((j + 1, i))
                p4 = self.image.getpixel((j, i + 1))
                n = Norme(p1, p2, p3, p4)
                if n < seuil:
                    p = (255, 255, 255)
                else:
                    p = (0, 0, 0)

                contour.putpixel((j - 1, i - 1), p)

        # la fonction de PIL qui fait la même chose
        # imgC = img.filter(ImageFilter.CONTOUR)

        # affichage de l'image
        plt.imshow(contour)
        plt.show()

    ###### Détection des contours
    def detection(self):

        # detection de contours:
        ret, thresh = cv2.threshold(self.im_gray, 127, 255, 0)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        len(contours)  # Comptage du nombre de contours fermés
        contour = cv2.drawContours(self.imagecv, contours, -1, (0, 255, 0), 3)
        # .....................................................................
        # Affichage:
        plt.imshow(contour)
        plt.show()





