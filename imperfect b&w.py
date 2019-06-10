from __future__ import print_function
import PIL
import os, sys
from PIL import Image, ImageTk
from colorama import init
from termcolor import colored
from tkinter import *
from tkinter import messagebox

x="obraz.jpg"

def color(x):
    if wartosc.get()=="1":
        img = PIL.Image.open(x).convert("L") #changes colors to black and white
        print(colored("Powrót do opcji edytowania\n","red"))
    elif wartosc.get()=="2":
        img = PIL.Image.open(x) #changes colors to RGB
        print(colored("Powrót do opcji edytowania\n","red"))
        img.show()



w=500
h=500
glowne_okno=Tk()
glowne_okno.title("black&white")
plotno=Canvas(glowne_okno, width=w, height=h)
plotno.pack()
obraz=PIL.Image.open("obraz.jpg")
obrazTk=ImageTk.PhotoImage(obraz)
plotno.create_image(w/2,h/2, image=obrazTk)
opis_pola_tekstowego= Label(glowne_okno, text= "Czy chcesz czarno-białe zdjęcie??")
opis_pola_tekstowego.pack(side=LEFT)


przycisk1=Button(glowne_okno,text="tak", variable=wartosc,value=1, command= color)
przycisk1.pack(side=LEFT)
przycisk2=Button(glowne_okno, text="nie",variable=wartosc,value=2, command=color )
przycisk2.pack(side=LEFT)
glowne_okno.mainloop()
