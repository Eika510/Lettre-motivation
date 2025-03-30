#Exo bit map

from tkinter import *

#création fenètre
root = Tk()
root.geometry("960x960")

#zone de dessin canvas
can1 = Canvas(root,height="512",width="512")
can1.place(x = 320, y = 320, anchor = "center")

#importer les images
caseA = PhotoImage(file="Chemin.gif")
caseB = PhotoImage(file="Carapateur.gif")
caseC = PhotoImage(file="Eau.gif")
caseD = PhotoImage(file="Eau nénuphare.gif")
caseE = PhotoImage(file="Nashor.gif")
caseF = PhotoImage(file="Arbre.gif")
caseG = PhotoImage(file="Bordure cote.gif")
caseH = PhotoImage(file="Bordure bas.gif")
caseI = PhotoImage(file="Bordure haut.gif")
caseJ = PhotoImage(file="Bordure cote droit.gif")
caseK = PhotoImage(file="Cote bas gauche.gif")
caseL = PhotoImage(file="Cote bas droit.gif")
caseM = PhotoImage(file="Cote haut droit.gif")
caseN = PhotoImage(file="Cote haut gauche.gif")
caseO = PhotoImage(file="Red buff.gif")
caseP = PhotoImage(file="Blue buff.gif")
viego1 = PhotoImage(file="viego.gif")
viego2 = PhotoImage(file="viego1.gif")
viego3 = PhotoImage(file="viego3.gif")
viego4 = PhotoImage(file="viego4.gif")
viego5 = PhotoImage(file="viego5.gif")
viego6 = PhotoImage(file="viego6.gif")
viego7 = PhotoImage(file="viego7.gif")
viego8 = PhotoImage(file="viego8.gif")
viego9 = PhotoImage(file="viego9.gif")
viego10 = PhotoImage(file="viego10.gif")
viego11 = PhotoImage(file="viego11.gif")
viego12 = PhotoImage(file="viego12.gif")
viego13 = PhotoImage(file="viego13.gif")
viego14 = PhotoImage(file="viego14.gif")
viego15 = PhotoImage(file="viego15.gif")
viego16 = PhotoImage(file="viego16.gif")
viego17 = PhotoImage(file="viego17.gif")
viego18 = PhotoImage(file="viego18.gif")
viego19 = PhotoImage(file="viego19.gif")
viego20 = PhotoImage(file="viego20.gif")
viego21 = PhotoImage(file="viego21.gif")
viego22 = PhotoImage(file="viego22.gif")
viego23 = PhotoImage(file="viego23.gif")
viego24 = PhotoImage(file="viego24.gif")
viego25 = PhotoImage(file="viego25.gif")
viego26 = PhotoImage(file="viego26.gif")
viego27 = PhotoImage(file="viego27.gif")
viego29 = PhotoImage(file="viego29.gif")
viego30 = PhotoImage(file="viego30.gif")
viego31 = PhotoImage(file="viego31.gif")




#creation de la matrice
L1= ["N","I","I","I","I","I","I","I","I","I","I","I","I","I","I","M"]
L2= ["G","A","A","A","A","A","A","A","A","A","A","A","A","A","A","J"]
L3= ["G","A","F","A","F","F","F","F","F","F","A","F","F","F","A","J"]
L4= ["G","A","F","A","C","B","D","C","D","D","A","F","F","F","A","J"]
L5= ["G","A","F","A","A","A","A","A","A","A","A","A","F","F","A","J"]
L6= ["G","A","F","F","F","A","O","F","F","F","F","A","A","A","A","J"]
L7= ["G","A","F","F","A","A","F","F","D","D","F","A","C","F","A","J"]
L8= ["G","A","F","C","A","F","F","F","C","D","F","A","E","F","A","J"]
L9= ["G","A","F","D","A","B","F","F","F","F","F","A","C","F","A","J"]
L10=["G","A","F","C","A","F","F","F","F","F","P","A","D","F","A","J"]
L11=["G","A","A","A","A","F","F","E","F","A","A","A","D","F","A","J"]
L12=["G","A","F","F","A","A","A","A","A","A","F","A","C","F","A","J"]
L13=["G","A","F","F","F","A","C","D","C","F","F","A","A","A","A","J"]
L14=["G","A","F","F","F","A","F","F","F","F","F","F","F","F","A","J"]
L15=["G","A","A","A","A","A","A","A","A","A","A","A","A","A","A","J"]
L16=["K","H","H","H","H","H","H","H","H","H","H","H","H","H","H","L"]
matrice = [L1,L2,L3,L4,L5,L6,L7,L8,L9,L10,L11,L12,L13,L14,L15,L16]

#dico qui associe lettre et image
dico = {"A" :caseA, "B" :caseB, "C" :caseC, "D" :caseD, "E" :caseE, "F" :caseF, "G" :caseG, "H" :caseH, "I" :caseI, "J" :caseJ, "K" :caseK, "L" :caseL, "M" :caseM, "N" :caseN, "O" :caseO, "P" :caseP}

#fonction
def creation_map():
    """fonction qui dessine la map"""
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            mon_image = dico[matrice[i][j]]
            can1.create_image(32*j,32*i,image=mon_image, anchor="nw")

#main
creation_map()

#placement du perso
x = 1
y = 14
perso = can1.create_image(32*x, 32*y,image=viego1, anchor ="nw")

#MAJ du perso
# =============================================================================
# question = input()
# if question == "z":
#     x = x
#     y -= 1
#     goto(x,y)
#     can1.itemconfig(perso, image = viego2)
# 
# =============================================================================
    
infini = TRUE
while infini == True:
    can1.after(500,None) #attendre 500 milisecondes
    can1.itemconfig(perso, image = viego2)
    root.update()
    can1.after(500,None) #attendre 500 milisecondes
    can1.itemconfig(perso, image = viego1)
    root.update()
    can1.after(500,None)
    can1.itemconfig(perso, image = viego3)
    root.update()
    can1.after(500,None)
    can1.itemconfig(perso, image = viego4)
    root.update()
    can1.after(500,None)
    can1.itemconfig(perso, image = viego5)
    root.update()
    can1.after(500,None)
    can1.itemconfig(perso, image = viego6)
    root.update()
    can1.after(500,None)
    can1.itemconfig(perso, image = viego7)
    root.update()
    can1.after(500,None)
    can1.itemconfig(perso, image = viego9)
    root.update()
    can1.after(500,None)
    can1.itemconfig(perso, image = viego10)
    root.update()
    can1.after(500,None)
    can1.itemconfig(perso, image = viego11)
    root.update()
    can1.after(500,None)
    can1.itemconfig(perso, image = viego12)
    root.update()
    can1.after(500,None)
    can1.itemconfig(perso, image = viego13)
    root.update()
    can1.after(500,None)
    can1.itemconfig(perso, image = viego15)
    root.update()
    can1.after(500,None)
    can1.itemconfig(perso, image = viego16)
    root.update()
    can1.after(250,None)
    can1.itemconfig(perso, image = viego17)
    root.update()
    can1.after(250,None)
    can1.itemconfig(perso, image = viego18)
    root.update()
    can1.after(250,None)
    can1.itemconfig(perso, image = viego19)
    root.update()
    can1.after(250,None)
    can1.itemconfig(perso, image = viego20)
    root.update()
    can1.after(250,None)
    can1.itemconfig(perso, image = viego21)
    root.update()
    can1.after(250,None)
    can1.itemconfig(perso, image = viego22)
    root.update()
    can1.after(250,None)
    can1.itemconfig(perso, image = viego23)
    root.update()
    can1.after(250,None)
    can1.itemconfig(perso, image = viego24)
    root.update()
    can1.after(250,None)
    can1.itemconfig(perso, image = viego25)
    root.update()
    can1.after(250,None)
    can1.itemconfig(perso, image = viego26)
    root.update()
    can1.after(250,None)
    can1.itemconfig(perso, image = viego27)
    root.update()
    can1.after(250,None)
    can1.itemconfig(perso, image = viego29)
    root.update()
    can1.after(250,None)
    can1.itemconfig(perso, image = viego30)
    root.update()
    can1.after(250,None)
    can1.itemconfig(perso, image = viego31)
    root.update()












root.mainloop()
