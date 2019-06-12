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


def plik():
    messagebox.showinfo("Wybór pliku", "Możesz rozpocząć edycję swojego pliku")#pole_tekstowe.get())
    imageFile=pole_tekstowe.get()

def autorzy():
    messagebox.showinfo("Twórcy","Twórcy: \nNatalia Doczekalska\nKarolina Stefańska\nDawid Rożnowski\nMichał Gil")

def bank():
    messagebox.showinfo("Wsparcie","Jeżeli chcesz wesprzeć nasze działania, możesz przelać dowolną kwotę na poniższy numer konta bankowego: \n\nbebe bubu baba byby")

def wsparcie():
    messagebox.showinfo("Wsparcie techniczne", "Jeżeli zauważyłeś niesympatyczny błąd w działaniu naszego programu, to możesz go dla nas naprawić.")

def zapisanie():
    messagebox.showinfo("Zapis pliku", "Udało Ci się zapisać plik!")

def color():
    x=pole_tekstowe.get()
    def blacknwhite():
        img = PIL.Image.open(x).convert("L") #changes colors to black and white
        img.show()
        img.save(pole_tekstowe.get())
    def normal():
        img = PIL.Image.open(x) #changes colors to RGB
        img.show()

    w=500
    h=500
    okno_koloru=Toplevel()
    okno_koloru.title("black&white")
    plotno=Canvas(okno_koloru, width=w, height=h)
    plotno.pack()
    obraz=PIL.Image.open(x)
    obrazTk=ImageTk.PhotoImage(obraz)
    plotno.create_image(w/2,h/2, image=obrazTk)
    opis_pola_tekstowego= Label(okno_koloru, text= "Chcesz zmienić kolorystyke na czarno-białą?")
    opis_pola_tekstowego.pack(side=LEFT)


    przycisk1=Button(okno_koloru,text="Tak", command= blacknwhite, bg="green",fg="white")
    przycisk1.pack(side=LEFT)
    przycisk2=Button(okno_koloru, text="Nie",command= normal, bg="red", fg="white" )
    przycisk2.pack(side=LEFT)
    okno_koloru.mainloop()

def scale():
    x=pole_tekstowe.get()
    def scale1():
        im=PIL.Image.open(x).resize((640,480))
        im.show()
        im.save(pole_tekstowe.get())
    def scale2():
        im=PIL.Image.open(x).resize((1280,720))
        im.show()
        im.save(pole_tekstowe.get())
    def scale3():
        im=PIL.Image.open(x).resize((1080,1080))
        im.show()
        im.save(pole_tekstowe.get())
    def scale4():
        im=PIL.Image.open(x).resize((720,1280))
        im.show()
        im.save(pole_tekstowe.get())

    okno_skalowania=Toplevel()
    okno_skalowania.title("Scale")
    plotno=Canvas(okno_skalowania, width=600, height=400)
    plotno.pack()
    obraz=PIL.Image.open(x)
    obrazTk=ImageTk.PhotoImage(obraz)
    plotno.create_image(200,200,image=obrazTk)
    etykietka=Label(okno_skalowania, text="Wybierz preferowaną skale:")
    etykietka.pack(side=LEFT)

    przycisk1=Button(okno_skalowania, text="4:3", command= scale1, bg="magenta",fg="white")
    przycisk1.pack(side=LEFT)
    przycisk1=Button(okno_skalowania, text="16:9", command= scale2, bg="green",fg="white")
    przycisk1.pack(side=LEFT)
    przycisk1=Button(okno_skalowania, text="1:1", command= scale3, bg="blue",fg="white")
    przycisk1.pack(side=LEFT)
    przycisk1=Button(okno_skalowania, text="9:16", command= scale4, bg="brown",fg="white")
    przycisk1.pack(side=LEFT)
    okno_skalowania.mainloop()

def rotate():
    x=pole_tekstowe.get()
    def rotate90():
        im= PIL.Image.open(x).rotate(90) #rotate by 90 degrees
        im.show()
        im.save(pole_tekstowe.get())
    def rotate180():
        im= PIL.Image.open(x).rotate(180) #rotate by 180 degrees
        im.show()
        im.save(pole_tekstowe.get())
    def rotate270():
        im= PIL.Image.open(x).rotate(270) #roatate by 270 degrees
        im.show()
        im.save(pole_tekstowe.get())
    def akcja():
        messagebox.showinfo("O ile stopni chcesz obrócić obrazek?", pole_tekstowe()) #question abot rotation

    w=500
    h=500
    okno_rotacji=Toplevel()
    okno_rotacji.title("Obrót obrazu")
    plotno=Canvas(okno_rotacji, width=w, height=h)
    plotno.pack()
    obraz=PIL.Image.open(x)
    obrazTk=ImageTk.PhotoImage(obraz)
    plotno.create_image(w/2,h/2, image=obrazTk)
    opis_pola_tekstowego= Label(okno_rotacji, text= "O ile stopni chcesz obrócić obrazek?")
    opis_pola_tekstowego.pack(side=LEFT)

    przycisk1=Button(okno_rotacji,text="90°", command= rotate90, bg="green",fg="white") # button to rotate by 90
    przycisk1.pack(side=LEFT)
    przycisk2=Button(okno_rotacji, text="180°", command= rotate180, bg="blue",fg="white") #button to rotate by 180
    przycisk2.pack(side=LEFT)
    przycisk3=Button(okno_rotacji, text="270°", command= rotate270, bg="red",fg="white") #button to rotate by 270
    przycisk3.pack(side=LEFT)
    okno_rotacji.mainloop()

def save_file():
    x=pole_tekstowe.get()
    def zapisywanko():
        im=PIL.Image.open(x)
        im.save(pole_zapisu.get()+".jpg")
        zapisanie()
    okno_zapisu=Toplevel()
    okno_zapisu.title("Save")
    okno_zapisu.geometry("300x70")
    opis_pola_tekstowego = Label(okno_zapisu, text="Nadaj nową nazwę swojego pliku:")
    opis_pola_tekstowego.pack(side=TOP)
    pole_zapisu = Entry (okno_zapisu)
    pole_zapisu.pack(side=TOP)
    przycisk= Button(okno_zapisu, text="Zapisz",command=zapisywanko, bg="red",fg="white")
    przycisk.pack(side=BOTTOM)
    okno_zapisu.mainloop()

glowne_okno=Tk()
glowne_okno.title("PYTHOSHOP")
glowne_okno.geometry("500x70")
opis_pola_tekstowego = Label(glowne_okno, text="Wprowadź nazwę pliku, który chcesz edytować (np. 'kochamGUIniepowiedziałniktnigdy.jpg')")
opis_pola_tekstowego.pack(side=TOP)
pole_tekstowe = Entry (glowne_okno)
pole_tekstowe.pack(side=TOP)
przycisk= Button(glowne_okno, text="Zatwierdź",command=plik,bg="orange",fg="black")
przycisk.pack(side=BOTTOM)
pasekMenu = Menu(glowne_okno)
menu_glowne=  Menu(pasekMenu, tearoff = 0)
menu_glowne.add_command(label="Zmiana kolorystyki", command=color)
menu_glowne.add_command(label="Przeskalowanie obrazu", command=scale)
menu_glowne.add_command(label="Obrót obrazu", command=rotate)
menu_glowne.add_command(label="Zapis pliku", command=save_file)
menu_glowne.add_command(label="Wyjdź",command=quit)
pasekMenu.add_cascade(label="Wyświetl opcje edytowania", menu=menu_glowne)

pomocMenu= Menu(pasekMenu, tearoff=0)
pomocMenu.add_command(label="Wyświetl listę twórców",command=autorzy)
pasekMenu.add_cascade(label="Twórcy",menu=pomocMenu)

pomocMenu2= Menu(pasekMenu, tearoff=0)
pomocMenu2.add_command(label="Numer konta bankowego", command=bank)
pomocMenu2.add_command(label="Wsparcie techniczne", command=wsparcie)
pasekMenu.add_cascade(label="Wsparcie",menu=pomocMenu2)

glowne_okno.config(menu=pasekMenu)
glowne_okno.mainloop()
