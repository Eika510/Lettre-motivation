from turtle import *
from random import choice

speed(0)
couleur = ["pink","red","yellow","green", "IndianRed", "Salmon", "LightSalmon", "DeepPink", "DarkOrange", "Coral", "Gold", "Moccasin", "DarkKhaki", "Fuchsia", "MediumPurple", "BlueViolet", "DarkMagenta"]
couleur1 = ["blue", "cyan", "deepskyblue", "aquamarine", "DarkTurquoise", "DodgerBlue", "RoyalBlue"]

def carre(L: int, x: int, y: int):
    """Dessine un carré de longueur L au point de coordonnées (x, y) et le remplit avec la couleur donné"""
    up()
    goto(x, y)
    down()
    begin_fill()
    fillcolor(choice(couleur1))
    for i in range(4):
        forward(L)
        left(90)
    end_fill()
    
    
def oeil(taille: int, x:int, y:int):
    """Dessine un œil pour le poisson."""
    color("black")
    up()
    goto(x,y)
    down()
    begin_fill()
    circle(taille)
    end_fill()


def triangle1(L: int, x: int, y: int):
    """Dessine un triangle équilatéral de longueur de côtés L au point de coordonnées (x, y) et le remplit avec la couleur donnée."""
    up()
    goto(x, y)
    setheading(30)
    down()
    begin_fill()
    fillcolor(choice(couleur))
    for _ in range(3):
        
        forward(L)
        left(120)
    end_fill()


def triangle2(L: int, x: int, y: int):
    """Dessine un triangle équilatéral de longueur de côtés L au point de coordonnées (x, y) et le remplit avec la couleur donnée."""
    up()
    goto(x, y)
    setheading(90)
    down()
    begin_fill()
    fillcolor(choice(couleur))
    for _ in range(3):
        
        forward(L)
        left(120)
    end_fill()

#main
bgcolor
triangle1(120, -250, -120)
triangle2(30, -115, -75)
triangle1(30, -110, -75)
triangle2(35, -75, -60)
triangle2(35, -75, -97)
triangle1(30, -70, -60)
triangle1(30, -70, -97)
triangle2(35, -40, -40)
triangle2(35, -38, -82)
triangle2(35, -38, -118)
triangle1(30, -35, -37)
triangle1(30, -33, -80)
triangle1(30, -33, -116)
triangle2(35, -5, -20)
triangle2(35, -3, -60)
triangle2(35, 0, -100)
triangle2(35, -3, -139)
triangle1(165, 5, -140)
oeil(10, 40, -30)

hideturtle()
exitonclick()
