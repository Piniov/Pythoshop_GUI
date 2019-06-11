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


def logo(tekst):
    nazwa=Figlet(font="basic").renderText(tekst)
    print(nazwa)

logo("Pythoshop")

def menu():
    while True:
        print(colored("MENU GŁÓWNE","green"))
        print("Wyświetl opcje edytowania - naciśnij 'q'\nWyłącz program - naciśnij 'r'\n")
        wybor1 = input()
        if wybor1== 'q':
            while True:
                print("Wybierz - co chcesz zrobić:")
                print (colored("1 - zmiana kolorystyki;","magenta"), colored("2 - przeskalowanie rozmiarów;","cyan"),colored("3 - obrót obrazu;","yellow"),
                colored("4 - zapis pliku;","blue"), colored("5 - wyjdź do menu głównego\n","red"))
                opcja=int(input("Odpowiedź:"))

                if opcja==1:
                    x=imageFile
                    color(x)
                elif opcja==2:
                    x=imageFile
                    scale(obrazek)
                elif opcja==3:
                    x=imageFile
                    rotate(x)
                elif opcja==4:
                    picture=imageFile
                    save_file(picture)
                elif opcja==5:
                    print(colored("\nWyjście do menu głównego\n","red"))
                    break
        elif wybor1=='r':
            print(colored("\nDziękujemy za skorzystanie z naszego programu. \nDobrego dnia! :)","green"))
            break

def color(x):
    while True:
        print("Chcesz czarno białe zdjęcie?")
        print(colored("TAK: Wciśnij: 'y'","cyan"))
        print(colored("NIE: Wciśnij 'n'","red")) #asks user if he wants b&w or colored picture
        m = input()
        if m=="y":
            im = PIL.Image.open(x).convert("L") #changes colors to black and white
        elif m=="n":
            im = PIL.Image.open(x) #changes colors to RGB
        else:
            print("Niewłaściwy klawisz! Spróbuj ponownie.\n")
            print(colored("Powrót do opcji edytowania\n","red"))
            break
        im.show()
        im.save(imageFile)
        print(colored("\nPowrót do opcji edytowania\n","red"))
        break

def scale(x):
    x=imageFile
    def scale1():
        im=PIL.Image.open(x).resize((640,480))
        im.show()
    def scale2():
        im=PIL.Image.open(x).resize((1280,720))
        im.show()
    def scale3():
        im=PIL.Image.open(x).resize((1080,1080))
        im.show()
    def scale4():
        im=PIL.Image.open(x).resize((720,1280))
        im.show()

    glowneokno=Tk()
    glowneokno.title("Scale")
    plotno=Canvas(glowneokno, width=600, height=400)
    plotno.pack()
    obraz=PIL.Image.open(x)
    obrazTk=ImageTk.PhotoImage(obraz)
    plotno.create_image(200,200,image=obrazTk)
    etykietka=Label(glowneokno, text="Wybierz skale:")
    etykietka.pack(side=LEFT)

    przycisk1=Button(glowneokno, text="4:3", command= scale1)
    przycisk1.pack(side=LEFT)
    przycisk1=Button(glowneokno, text="16:9", command= scale2)
    przycisk1.pack(side=LEFT)
    przycisk1=Button(glowneokno, text="1:1", command= scale3)
    przycisk1.pack(side=LEFT)
    przycisk1=Button(glowneokno, text="9:16", command= scale4)
    przycisk1.pack(side=LEFT)
    glowneokno.mainloop()

def rotate(x):
    x=imageFile
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
    obraz=PIL.Image.open(x)
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


def save_file(x):   #x - chosen file which user wants to save
    while True:
        im = PIL.Image.open(x)
        print ("Wpisz nazwę nowego pliku.")
        new_name = input()  #user has to name new file
        extension = '.jpg'  #extension is needed to allow Python to write a file as a picture file
        new_file = new_name + extension
        im.save(new_file)       #save() is a Pillow module function
        print ("Oto nazwa nowo utworzonego pliku:", new_file)
        print()
        print(colored("Powrót do opcji edytowania\n","red"))
        break

print(colored("Witaj w Pythoshopie!\nProgram ten umożliwia Ci zmianę kolorystyki, przeskalowanie lub obrót obrazu!\n","green"))
imageFile=input("Wpisz nazwę pliku (np. zabawny_pies.jpg):\n")
obrazek=PIL.Image.open(imageFile)
print("Oto dane dotyczące wczytanego (pierwotnego) pliku: ", obrazek.format, obrazek.size, obrazek.mode)
print()
menu()
