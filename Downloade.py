from tkinter import *
import pytube
from tkinter import messagebox, filedialog
from tkinter.messagebox import *
from tkinter.simpledialog import *
from tkinter import messagebox
from pytube import YouTube
from tkinter import ttk

from information import *
#***********************************************************************************************************************
def quitter(root):
	reponse = askyesno("Terminer le jeu","Voulez-vous réellement quitter ? \n Cliquer « Oui » pour finir")
	if reponse :
		root.destroy()
#***********************************************************************************************************************
def back(R):
    R.destroy()
#***********************************************************************************************************************
def browse():
    download_Directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH")
    download_Path.set(download_Directory)
#***********************************************************************************************************************
def download():
    lien = lien_var.get()

    if nmbr1_name.get()=="MP4":
        youtube = pytube.YouTube(lien)
        video = youtube.streams.get_highest_resolution()
        folder = download_Path.get()
        video.download(folder)
        lien_var.set("")
        messagebox.showinfo(title='Download', message='Done')
    elif nmbr1_name.get()=="MP3":
        youtube1 = pytube.YouTube(lien)
        video1 = youtube1.streams.filter(mime_type="audio/mp4",abr="128kbps",type = "audio")
        folder = download_Path.get()
        video1.download(folder)
        lien_var.set("")
        messagebox.showinfo(title='Download', message='Done')

#***********************************************************************************************************************
window = Tk()
window.geometry("720x480")
window.resizable(width=0, height=0)
window.configure(bg="#8C8F82")
window.title("YouTube Downloader")
window.iconbitmap("mp.ico")
frame1 = Frame(window, bg="#0ABD94", width=720, height=80, bd=20, relief="sunken")
frame1.place(x=0, y=0)
Titre = Label(window, text="  YouTube Downloader  ", fg="white", bg="#0ABD94", font=("Helvatical", 18, "bold")).place(x=220, y=30)
frame2 = Frame(window, bg="#A2F2E0", width=720, height=380, bd=20, relief="sunken")
frame2.place(x=0, y=90)
Label_A = Label(frame2, text="Choose a location for your video", width=35, font=("Helvatical", 14, "bold"),fg="white", bg="#0ABD94", bd=10, relief="sunken").place(x=110, y=40)
download_Path = StringVar()
download_path = Entry(frame2, width=35, textvariable=download_Path, bd=10, fg="#0ABD94", bg="white",relief="sunken", font=("Helvatical", 12, "bold")).place(x=170, y=90)
choose_folder = Button(frame2, text="Browse", bd=8, relief="sunken", fg="white", bg="#0ABD94", command=browse,font=("Helvatical", 12, "bold")).place(x=560, y=40)
link_here = Label(frame2, text="Tape Your link video", width=35, font=("Helvatical", 14, "bold"), fg="white",bg="#0ABD94", bd=10, relief="sunken").place(x=110, y=140)
lien_var = StringVar()
entry = Entry(frame2, width=35, textvariable=lien_var, bd=10, fg="#0ABD94", bg="white", relief="sunken",font=("Arial", 12, "bold")).place(x=170, y=190)
Button_1 = Button(frame2, width=15, text='Download', bd=8, relief="sunken", fg="white", bg="#0ABD94",command=download, font=("Arial", 12, "bold")).place(x=245, y=240)
Button_2 = Button(frame2, width=15, text='Information', bd=8, relief="sunken", fg="white", bg="#0ABD94",command=lambda :information(lien_var.get()), font=("Arial", 12, "bold")).place(x=110, y=290)
Button_3 = Button(frame2, width=15, text='Quitter', bd=8, relief="sunken", fg="white", bg="#0ABD94", command=lambda :quitter(window),font=("Arial", 12, "bold")).place(x=380, y=290)
nmbr1_name = StringVar()
nmbr1_name.set("MP4")
cmb1 = ttk.Combobox(frame2,justify="center" ,width=10,textvariable=nmbr1_name, font=('Helvatical', 12, 'bold'))
cmb1['values'] = ('MP4', 'MP3')
cmb1.place(x=560, y=140)
cmb1.current()
combostyle = ttk.Style()

combostyle.theme_create('combostyle', parent='alt',
                         settings = {'TCombobox':
                                     {'configure':
                                      {'selectbackground': '#A2F2E0',
                                       'fieldbackground': '#A2F2E0',
                                       'background': '#0ABD94'
                                       }}})
combostyle.theme_use('combostyle')
window.mainloop()


