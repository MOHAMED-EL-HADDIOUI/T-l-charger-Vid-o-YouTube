from tkinter import *
import pytube
from tkinter import messagebox, filedialog
from tkinter.messagebox import *
from tkinter.simpledialog import *
from tkinter import messagebox
from pytube import YouTube
import tkinter as tk

#***********************************************************************************************************************

def back(R):
    R.destroy()

#***********************************************************************************************************************
def information(link):
    def Afficher():
        video = pytube.YouTube(link)
        value_titre.delete(0, END)
        value_titre.insert(0, video.title)

        value_views.delete(0, END)
        value_views.insert(0, video.views)

        value_rating.delete(0, END)
        value_rating.insert(0, video.vid_info)

        value_lenght.delete(0, END)
        value_lenght.insert(0, video.length)

    window_A = tk.Tk()
    window_A.geometry("720x480")
    window_A.resizable(width=0, height=0)
    window_A.configure(bg="#8C8F82")
    window_A.title("Information About video")
    window_A.iconbitmap("mp.ico")

    frameY = Frame(window_A, bg="#0ABD94", width=720, height=80, bd=20, relief="sunken")
    frameY.place(x=0, y=0)
    Titre_A = Label(window_A, text="  Information About video  ", fg="white", bg="#0ABD94",
                    font=("Helvatical", 18, "bold")).place(x=220, y=30)
    frameW = Frame(window_A, bg="#A2F2E0", width=720, height=380, bd=20, relief="sunken")
    frameW.place(x=0, y=90)
    Label_T = Label(window_A, text="Titre", width=8, font=("Helvatical", 18, "bold"), fg="white", bd=7,
                    bg="#0ABD94").place(x=40, y=120)
    value_titre = tk.Entry(window_A, width=35, font=("Helvatical", 18, "bold"), fg="white",
                        bg="#000000", bd=8)
    value_titre.place(x=200, y=120)
    Label_V = Label(window_A, text="Views", width=8, font=("Helvatical", 18, "bold"), fg="white", bd=7,
                    bg="#0ABD94").place(x=40, y=170)
    value_views = tk.Entry(window_A, width=35, font=("Helvatical", 18, "bold"), fg="white",
                        bg="#000000", bd=8)
    value_views.place(x=200, y=170)
    Label_R = Label(window_A, text="Rating", width=8, font=("Helvatical", 18, "bold"), fg="white", bd=7,
                    bg="#0ABD94").place(x=40, y=220)

    value_rating = tk.Entry(window_A, width=35, font=("Helvatical", 18, "bold"), fg="white",
                         bg="#000000", bd=8)
    value_rating.place(x=200, y=220)
    Label_L = Label(window_A, text="Lenght", width=8, font=("Helvatical", 18, "bold"), fg="white", bd=7,
                    bg="#0ABD94").place(x=40, y=270)
    value_lenght = tk.Entry(window_A, width=35, font=("Helvatical", 18, "bold"), fg="white",
                         bg="#000000", bd=8)
    value_lenght.place(x=200, y=270)
    Button_Z = tk.Button(frameW, width=15, text='Back', bd=8, relief="sunken", fg="white", bg="#0ABD94",command=lambda: back(window_A), font=("Arial", 12, "bold")).place(x=90, y=290)
    Button_K = tk.Button(frameW, width=15, text='Afficher', bd=8, relief="sunken", fg="white", bg="#0ABD94", command=Afficher,font=("Arial", 12, "bold")).place(x=265, y=290)
    Button_E = tk.Button(frameW, width=15, text='Quitter', bd=8, relief="sunken", fg="white", bg="#0ABD94", command=quit,font=("Arial", 12, "bold")).place(x=440, y=290)
    window_A.mainloop()
