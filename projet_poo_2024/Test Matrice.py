# =============================================================================
# Test Matrice
# =============================================================================
from matrice_led_class import *
from tkinter import *
from random import randint

fenetre = Tk()
fenetre.geometry("640x640")
led = Matrice(fenetre, 640, 640, 16, 16)
led.dessine_matrice()

led.set_pixel(4, 5, (77,236,79))
led.set_pixel(2, 8, (0,32,254))

for i in range(4,15):
    led.pause(200)
    led.deplace_pixel_bas(i, 5)
led.reset_matrice()

for i in range(16):
    led.set_pixel(i, i, (randint(15,75),randint(150,200),randint(210,255)))
    led.pause(200)

for i in range(16):
    led.set_pixel(15-i, i, (randint(150,200),randint(150,200),randint(150,200)))
    led.pause(200)

led.reset_matrice()
led.importation("trois.txt", (255,20,130))
led.pause(200)
led.importation("deux.txt", (255,0,10))
led.pause(200)
led.importation("un.txt", (24,20,130))
led.pause(200)
led.importation("zero.txt", (255,200,130))
led.pause(200)

fenetre.mainloop()
