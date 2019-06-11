from __future__ import print_function
import PIL
import os, sys
from PIL import Image, ImageTk
from colorama import init
from termcolor import colored
from pyfiglet import Figlet
from tkinter import *
from tkinter import messagebox
init()

x="obraz.jpg"
def rotate90():
    im= PIL.Image.open(x).rotate(90) #rotate by 90 degrees
    im.show()
def rotate180():
    im= PIL.Image.open(x).rotate(180) #rotate by 180 degrees
    im.show()
def rotate270():
    im= PIL.Image.open(x).rotate(270) #roatate by 270 degrees
    im.show()
def akcja():
    messagebox.showinfo("O ile stopni chcesz obrócić obrazek?", pole_tekstowe()) #question abot rotation

w=500
h=500
glowne_okno=Tk()
glowne_okno.title("rotate")
plotno=Canvas(glowne_okno, width=w, height=h)
plotno.pack()
obraz=PIL.Image.open("obraz.jpg")
obrazTk=ImageTk.PhotoImage(obraz)
plotno.create_image(w/2,h/2, image=obrazTk)
opis_pola_tekstowego= Label(glowne_okno, text= "O ile stopni chcesz obrócić obrazek?")
opis_pola_tekstowego.pack(side=LEFT)

przycisk1=Button(glowne_okno,text="90", command= rotate90) # button to rotate by 90
przycisk1.pack(side=LEFT)
przycisk2=Button(glowne_okno, text="180", command= rotate180) #button to rotate by 180
przycisk2.pack(side=LEFT)
przycisk3=Button(glowne_okno, text="270", command= rotate270) #button to rotate by 270
przycisk3.pack(side=LEFT)
glowne_okno.mainloop()
