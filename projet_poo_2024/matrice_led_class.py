# -*- coding: utf-8 -*-

from tkinter import *
# =============================================================================
# classe pixel
# =============================================================================

class Pixel :
    
    def __init__(self,ligne,colonne,r,v,b):
        """cree un pixel avec ses 3 couleurs r,v,b des entiers
        sa ligne et sa colonne : ligne et colonne des entiers commençant à 0
        """
        self.l = ligne
        self.c = colonne
        self.r = r
        self.v = v
        self.b = b

    def couleur_hexa(self):
        """donne la couleur (r,v,b) en hexadécimal"""
        if self.r<=15 :
            self.couleur = "#"+"0"+hex(self.r)[2:]
        else : 
            self.couleur = "#"+hex(self.r)[2:]
        if self.v<=15 :
            self.couleur += "0"+hex(self.v)[2:]
        else : 
            self.couleur += hex(self.v)[2:]
        if self.b<=15 :
            self.couleur += "0"+hex(self.b)[2:]
        else : 
            self.couleur += hex(self.b)[2:]   
                
    def change_couleur(self,new):
        """change la couleur du pixel
        new tuple du type (r,v,b)"""
        self.r,self.v,self.b = new
        self.couleur_hexa()
                
    def get_couleur(self):
        """renvoie la couleur du pixel"""
        return (self.r,self.v,self.b)
    
    def dessine_pixel(self,can,taille_c,taille_l):
        """dessine le pixel dans le canvas can choisi
        taille_c : taille en largeur
        taille_l : taille ne hauteur"""
        self.couleur_hexa()
        self.pix = can.create_rectangle(self.c*taille_c,self.l*taille_l,(self.c+1)*taille_c,(self.l+1)*taille_l,fill=self.couleur,outline = "white",width=1)
        
    def change_pixel(self,can):
        """change la couleur d'un pixel et met de la même couleur son contour"""
        self.couleur_hexa()
        can.itemconfig(self.pix,fill=self.couleur,outline=self.couleur)
    

# =============================================================================
# classe matrice
# =============================================================================

     
class Matrice :
    
    def __init__(self,f,largeur,hauteur,nc,nl):
        """crée une matrice rectangle de pixel 
        nl = nbre de lignes 
        nc = nbre de colonnes
        f fenetre tkinter de taille largeur x hauteur """
        self.nl = nl
        self.nc = nc
        self.f = f
        self.liste_pixels = [[Pixel(i,j,0,0,0) for j in range(self.nc)] for i in range(self.nl)] #tous noirs
        self.width = largeur #largeur de la fenetre
        self.height = hauteur #hauteur de la fenetre
        self.can = Canvas(self.f,width=self.width,height=self.height,bg ="black")   #creation du canvas
        
    def get_pixel(self,i,j):
        """recupere le pixel ligne i colonne j"""
        return self.liste_pixels[i][j]
    
    def set_pixel(self,i,j,new):
        """change la couleur du pixel ligne i colonne j"""
        self.liste_pixels[i][j].change_couleur(new)
        self.liste_pixels[i][j].change_pixel(self.can)
        self.f.update()
        
    def dessine_matrice(self) :
        """dessine la matrice dans une dans une fenetre tkinter"""
        self.can.place(x=0,y=0)
        self.taille_l = self.height//self.nl #taille ligne
        self.taille_c = self.width//self.nc #taille colonne
        for i in range(self.nl) :   #on dessine la premiere matrice
            for j in range(self.nc):
                self.liste_pixels[i][j].dessine_pixel(self.can,self.taille_c,self.taille_l)
              
    def mise_a_jour(self,temps)  :
        """met à jour la matrice après temps millisecondes"""
        self.can.after(temps,None)  #pause de temps millisecondes
        for i in range(self.nl) :   
            for j in range(self.nc):
                self.liste_pixels[i][j].dessine_pixel(self.can,self.taille_c,self.taille_l)
                        
    def pause(self,temps):
        """fait une pause de temps millisecondes"""
        self.can.after(temps,None)
        
    def importation(self,fichier,couleur):
        """importe un fichier texte composé de 0 et de 1
        les 0 donne des pixels noirs
        les 1 donne des pixels dans la couleur (r,v,b) proposée
        chaque ligne du fichier a un longueur égal à self.largeur
        il y a en tout self.hauteur lignes
        Après avoir été importé le fichier devient une matrice de pixel"""
        with open(fichier,'r') as fichier_import :
            lignes = fichier_import.readlines()
        assert len(lignes[0])-1==self.nc,"largeur du fichier importée incompatible"
        assert len(lignes)==self.nl,"hauteur du fichier importée incompatible"
        for i in range(self.nl) :  
            for j in range(self.nc):
                if lignes[i][j]!="0" :
                    self.set_pixel(i,j,couleur)
                else :
                    self.set_pixel(i,j,(0,0,0))
                    
    def reset_matrice(self):
        """réinitilise la matrice pixel noir bordures blanches"""
        self.liste_pixels = [[Pixel(i,j,0,0,0) for j in range(self.nc)] for i in range(self.nl)] #tous noirs    
        self.mise_a_jour(100)       
            
    def deplace_pixel_gauche(self,i,j):
        """le pixel à la place (i,j) est effacé et il remplace celui à la place (i,j-1)"""
        if j-1>=0 :
            c = self.get_pixel(i,j).get_couleur()
            self.set_pixel(i,j,(0,0,0))      
            self.set_pixel(i,j-1,c)      
            
    def deplace_pixel_droite(self,i,j):
        """le pixel à la place (i,j) est effacé et il remplace celui à la place (i,j+1)"""
        if j+1<=self.nc-1 :
            c = self.get_pixel(i,j).get_couleur()
            self.set_pixel(i,j,(0,0,0))      
            self.set_pixel(i,j+1,c)      
            
    def deplace_pixel_bas(self,i,j):
        """le pixel à la place (i,j) est effacé et il remplace celui à la place (i+1,j)"""
        if i+1<=self.nl-1 :
            c = self.get_pixel(i,j).get_couleur()
            self.set_pixel(i,j,(0,0,0))      
            self.set_pixel(i+1,j,c)      
            
    def deplace_pixel_haut(self,i,j):
        """le pixel à la place (i,j) est effacé et il remplace celui à la place (i-1,j)"""
        if i-1>=0 :
            c = self.get_pixel(i,j).get_couleur()
            self.set_pixel(i,j,(0,0,0))      
            self.set_pixel(i-1,j,c)      
            
                
    
