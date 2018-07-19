#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from tkinter import filedialog
from tkinter import *
import magic
import string
from to_utf8 import process as toUTF8

def main():
        def select_file():
            dev = dev_var.get()
            original = original_encoding.get()
            desktop = os.path.join(os.path.join(os.path.expanduser('~')) , 'Desktop')

            fitxategia = filedialog.askopenfilename(initialdir = desktop , title = "Aukeratu fitxategia" ,
                                                    filetypes = (
                                                        ("Guztiak" , "*.*"),
                                                        ("CSV fitxategiak" , "*.csv") ,
                                                        ("TXT fitxategiak" , "*.txt")
                                                    ))

            lblInfo.config(text = "Mota => " + magic.from_file(fitxategia))
            lblMime.config(text = "MIME => " + magic.from_file(fitxategia, mime = TRUE))

            charset, output = toUTF8 (fitxategia)

            def _removeNonAscii( s ):
                return "".join(i for i in s if ord(i) < 128)

            def filter_nonprintable( text ):
                import string
                # Get the difference of all ASCII characters from the set of printable characters
                nonprintable = set([chr(i) for i in range(128)]).difference(string.printable)
                # Use translate to remove all non-printable characters
                return text.translate({ord(character): None for character in nonprintable})
            with open(fitxategia,"r",  errors = 'ignore') as f:
                with open(output , 'w' , encoding = 'UTF-8') as fw:
                    for line in f:
                        print (line)
                        # if '\u0' in line:
                        #     print ("jojo")
                        linea = _removeNonAscii(line)
                        print (linea)
                        
                        k = filter_nonprintable(linea)
                        fw.write(k)

            # bihurtzen(fitxategia,output,charset)

            return dev_var.set(fitxategia)

        raiz = Tk()
        raiz.geometry('450x200')
        raiz.configure(bg = 'beige')
        raiz.title('Aplicación')
        dev_var = StringVar()  # The user write text
        original_encoding = StringVar()

        # Aukeratu fitxategia
        label0 = Label(raiz , text = "Aukeratu fitxategia eta egin klik bihurtu  botoian" , relief = FLAT)
        label0.pack(padx = 5 , pady = 5)

        # File_select
        frame1 = Frame(raiz , borderwidth = 2 , bg = 'old lace' , relief = RAISED)
        frame1.pack(side = TOP , padx = 5 , pady = 5)
        label1 = Label(frame1 , text = 'Fitxategia :' , bg = 'old lace').grid(row = 1 , sticky = E)
        entry1 = Entry(frame1 , textvariable = dev_var , width = 35 , exportselection = 1).grid(row = 1 , column = 2)
        btn1 = Button(frame1, text = "Aukeratu..." , relief = RAISED ,command = select_file).grid(row = 1 , column = 3)

        # File description
        frame2 = Frame(raiz , borderwidth = 2 , bg = 'old lace' , relief = RAISED)
        frame2.pack(side = TOP , padx = 5 , pady = 5)
        lblInfo = Label(raiz , text = "" , relief = RAISED, justify=LEFT)
        lblInfo.pack(padx = 5 , pady = 5, fill =BOTH)
        lblMime = Label(raiz , text = "" , relief = RAISED , justify = LEFT)
        lblMime.pack(padx = 5 , pady = 5 , fill = BOTH)

        # Bihurtu botoia

        # bouton_recup = Button(raiz , text = "Bihurtu" , relief = RAISED ,
        #                       command = bihurtzen(dev_var,'output.txt', original_encoding)
        #                       )
        # bouton_recup.pack(side = RIGHT , padx = 5 , pady = 5)

        # Irten botoia
        bouton_quit = Button(raiz , text = 'Irten' , relief = RAISED , command = raiz.quit)
        bouton_quit.pack(side = LEFT , padx = 5 , pady = 5)

        raiz.mainloop()


if __name__ == '__main__':
    main()


