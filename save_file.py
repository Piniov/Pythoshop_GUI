def zapisanie():
    messagebox.showinfo("Zapis pliku", "Udało Ci się zapisać plik!")


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
