from __future__ import print_function
import PIL
import os, sys
from PIL import Image, ImageTk
from colorama import init
from termcolor import colored
from tkinter import *
from tkinter import messagebox

def color(x):
    x=imageFile
    def blacknwhite():
        img = PIL.Image.open(x).convert("L") #changes colors to black and white
        img.show()
    def normal():
        img = PIL.Image.open(x) #changes colors to RGB
        img.show()



    w=500
    h=500
    glowne_okno=Tk()
    glowne_okno.title("black&white")
    plotno=Canvas(glowne_okno, width=w, height=h)
    plotno.pack()
    obraz=PIL.Image.open(imageFile)
    obrazTk=ImageTk.PhotoImage(obraz)
    plotno.create_image(w/2,h/2, image=obrazTk)
    opis_pola_tekstowego= Label(glowne_okno, text= "Czy chcesz czarno-białe zdjęcie??")
    opis_pola_tekstowego.pack(side=LEFT)


    przycisk1=Button(glowne_okno,text="tak", command= blacknwhite)
    przycisk1.pack(side=LEFT)
    przycisk2=Button(glowne_okno, text="nie",command=normal )
    przycisk2.pack(side=LEFT)
    glowne_okno.mainloop()
