import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from PIL import Image, ImageTk
import matplotlib.pylab as plt
import numpy as np
import math as mt
import random as ra
from matplotlib.figure import Figure
from matplotlib.pylab import show
from tkinter import filedialog, messagebox
import pandas as pd
from tkinter.messagebox import showinfo
import webbrowser
import sqlite3
import tkcalendar as ca
from tkcalendar import DateEntry, calendar_


class CovApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)


    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.title("COVID19sim")

        self.app_width = 900
        self.app_height = 550


        self.screen_width = self.master.winfo_screenwidth()
        self.screen_height = self.master.winfo_screenheight()

        x = (self.screen_width / 2) - (self.app_width / 2)
        y = (self.screen_height / 2) - (self.app_height /2)

        self.master.geometry(f'{self.app_width}x{self.app_height}+{int(x)}+{int(y)}')

        ImgLabel = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\COVID19SIM.png')
        ImgLabel = ImageTk.PhotoImage(ImgLabel)
        Imalabelr =  Label(self, image = ImgLabel)
        Imalabelr.Image = ImgLabel

        Imgstart = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\startbutton.png')
        Imgstart = ImageTk.PhotoImage(Imgstart)
        Imastartr =  Label(self, image = Imgstart)
        Imastartr.Image = Imgstart

        Imginfo = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\infobutton.png')
        Imginfo = ImageTk.PhotoImage(Imginfo)
        Imainfor =  Label(self, image = Imginfo)
        Imainfor.Image = Imginfo

        Imgaide = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\aidebutton.png')
        Imgaide = ImageTk.PhotoImage(Imgaide)
        Imaaider =  Label(self, image = Imgaide)
        Imaaider.Image = Imgaide

        Imgclose = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\closebutton.png')
        Imgclose = ImageTk.PhotoImage(Imgclose)
        Imacloser =  Label(self, image = Imgclose)
        Imacloser.Image = Imgclose



        Imgback3 = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\corona.jpg')
        Imgback3 = ImageTk.PhotoImage(Imgback3)
        Imaback3r =  Label(self, image = Imgback3)
        Imaback3r.Image = Imgback3


        self.master.config(bg='#FFFFFF')
        self.master.iconbitmap("logo.ico")
        self.config(bg='#FFFFFF')

        self.Loginframe01 = Frame(self, width = 950, height = 450, bd = 0, bg='#FFFFFF', relief = 'flat')
        self.Loginframe01.grid(row = 0, column = 0)

        self.Loginframe0 = Frame(self.Loginframe01, width = 200, height = 500, bd = 0, bg='#FFFFFF', relief = 'flat')
        self.Loginframe0.place(rely = 0, relx = 0)



        self.Loginframe1 = Frame(self.Loginframe01, width = 300, height = 100, bd = 5, bg='#FFFFFF', relief = 'flat')
        self.Loginframe1.place(rely = 0, relx = 0.27)

        self.Loginframe2 = Frame(self.Loginframe01, width = 200, height = 515, bd = 0, bg='#FFFFFF', relief = 'flat')
        self.Loginframe2.place(rely = 0, relx = 0.75)


        self.Loginframe14 = Frame(self, width = 400, height = 200, bd = 0, bg= '#FFFFFF', relief = 'flat')
        self.Loginframe14.place(rely = 0.30, relx = 0.30)

        self.Loginframe15 = Frame(self, width = 450, height = 400, bd = 0, bg= '#FFFFFF', relief = 'flat')
        self.Loginframe15.place(rely = 0.45, relx = 0.27)

        self.btnback3 = Label(self.Loginframe15, image = Imgback3, bd = 0, bg='#FFFFFF',)
        self.btnback3.place(x=0, y=0)


        logo = Image.open('logo_cnrst_2018.png')
        logo = ImageTk.PhotoImage(logo)
        logo_label =  Label(self.Loginframe1, bd = 0, bg='#FFFFFF', image = logo)
        logo_label.Image = logo
        logo_label.grid(column=0, row=0)

        logo1 = Image.open('logo_fsdm.png')
        logo1 = ImageTk.PhotoImage(logo1)
        logo_label1 =  Label(self.Loginframe1, bd = 0, bg='#FFFFFF', image = logo1)
        logo_label1.Image = logo1
        logo_label1.grid(column=1, row=0)

        logo2 = Image.open('logo-ministère-santé-Maroc.jpg')
        logo2 = ImageTk.PhotoImage(logo2)
        logo_label2 =  Label(self.Loginframe1, bd = 0, bg='#FFFFFF', image = logo2)
        logo_label2.Image = logo2
        logo_label2.grid(column=2, row=0)




        self.LabelTitle = Label(self.Loginframe14, image = ImgLabel, bg='#FFFFFF', bd = 0)
        self.LabelTitle.place(x=0, y=0)





        self.Loginframe4 = Frame(self, width = 950, height = 100, bg='#FFFFFF', bd = 20, relief = 'flat')
        self.Loginframe4.grid(row = 1, column = 0)



        self.startbtn = tk.Button(self.Loginframe4, image = Imgstart, bd = 0, bg='#FFFFFF', command=lambda: master.switch_frame(PageOne))
        self.startbtn.place(rely = 0, relx = 0.01)

        self.btninfo = Button(self.Loginframe4, image = Imginfo, bd = 0, bg='#FFFFFF', command = self.info_window)
        self.btninfo.place(rely = 0, relx = 0.26)

        self.btnaide = Button(self.Loginframe4, image = Imgaide, bd = 0, bg='#FFFFFF', command = self.aide_window)
        self.btnaide.place(rely = 0, relx = 0.49)

        self.btnfermer = Button(self.Loginframe4, image = Imgclose, bg='#FFFFFF', bd = 0, command = self.master.quit)
        self.btnfermer.place(rely = 0, relx = 0.72)

    def info_window(self):
        self.infoWindow = Toplevel(self.master)
        self.app = Info(self.infoWindow)


    def aide_window(self):
        self.aideWindow = Toplevel(self.master)
        self.app = Aide(self.aideWindow)

class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.title("COVID19sim")

        self.app_width = 900
        self.app_height = 615


        self.screen_width = self.master.winfo_screenwidth()
        self.screen_height = self.master.winfo_screenheight()

        x = (self.screen_width / 2) - (self.app_width / 2)
        y = (self.screen_height / 2) - (self.app_height /2)

        self.master.geometry(f'{self.app_width}x{self.app_height}+{int(x)}+{int(y)}')

        self.master.config(bg='#FFFFFF')
        self.master.iconbitmap("logo.ico")


        self.config(bg = '#FFFFFF')


        ImgREhome = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\returnbuttonhome.png')
        ImgREhome = ImageTk.PhotoImage(ImgREhome)
        ImaREhomer =  Label(self, image = ImgREhome)
        ImaREhomer.Image = ImgREhome

        ImgREp = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\returnbutton.jpg')
        ImgREp = ImageTk.PhotoImage(ImgREp)
        ImaREhomer =  Label(self, image = ImgREp)
        ImaREhomer.Image = ImgREp


        ImgLabel = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\COVID19SIM.png')
        ImgLabel = ImageTk.PhotoImage(ImgLabel)
        Imalabelr =  Label(self, image = ImgLabel)
        Imalabelr.Image = ImgLabel



        ImgAnalyse = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\analysebutton.png')
        ImgAnalyse = ImageTk.PhotoImage(ImgAnalyse)
        ImaAnalyser =  Label(self, image = ImgAnalyse)
        ImaAnalyser.Image = ImgAnalyse

        ImgPredictive = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\predictivebutton.png')
        ImgPredictive = ImageTk.PhotoImage(ImgPredictive)
        ImaPredictiver =  Label(self, image = ImgPredictive)
        ImaPredictiver.Image = ImgPredictive

        Imginfo = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\infobutton.png')
        Imginfo = ImageTk.PhotoImage(Imginfo)
        Imainfor =  Label(self, image = Imginfo)
        Imainfor.Image = Imginfo

        Imgaide = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\aidebutton.png')
        Imgaide = ImageTk.PhotoImage(Imgaide)
        Imaaider =  Label(self, image = Imgaide)
        Imaaider.Image = Imgaide

        Imgback4 = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\back4.jpg')
        Imgback4 = ImageTk.PhotoImage(Imgback4)
        Imaback4r =  Label(self, image = Imgback4)
        Imaback4r.Image = Imgback4

        Imgback5 = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\back51.jpg')
        Imgback5 = ImageTk.PhotoImage(Imgback5)
        Imaback5r =  Label(self, image = Imgback5)
        Imaback5r.Image = Imgback5

        Imgback6 = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\back6.jpg')
        Imgback6 = ImageTk.PhotoImage(Imgback6)
        Imaback6r =  Label(self, image = Imgback6)
        Imaback6r.Image = Imgback6


        self.Loginframe01 = Frame(self, width = 950, height = 500, bd = 0, bg='#FFFFFF', relief = 'flat')
        self.Loginframe01.grid(row = 0, column = 0)

        self.Loginframe0 = Frame(self.Loginframe01, width = 200, height = 500, bd = 0, bg='#FFFFFF', relief = 'flat')
        self.Loginframe0.place(rely = 0, relx = 0)




        self.Loginframe1 = Frame(self.Loginframe01, width = 300, height = 400, bd = 5, bg='#FFFFFF', relief = 'flat')
        self.Loginframe1.place(rely = 0, relx = 0.27)

        self.Loginframe2 = Frame(self.Loginframe01, width = 200, height = 515, bd = 0, bg='#FFFFFF', relief = 'flat')
        self.Loginframe2.place(rely = 0, relx = 0.70)


        self.Loginframe14 = Frame(self, width = 400, height = 200, bd = 0, bg= '#FFFFFF', relief = 'flat')
        self.Loginframe14.place(rely = 0.30, relx = 0.30)

        self.Loginframe15 = Frame(self, width = 450, height = 400, bd = 0, bg= '#FFFFFF', relief = 'flat')
        self.Loginframe15.place(rely = 0.50, relx = 0.26)

        self.Loginframe30 = Frame(self.Loginframe01, width = 300, height = 500, bd = 0, bg='#FFFFFF', relief = 'flat')
        self.Loginframe30.place(rely = 0.30, relx = 0)

        self.btnback4 = Label(self.Loginframe30, image = Imgback4, bd = 0, bg='#FFFFFF',)
        self.btnback4.place(x=-0.20, y=0)

        self.Loginframe31 = Frame(self.Loginframe01, width = 300, height = 500, bd = 0, bg='#FFFFFF', relief = 'flat')
        self.Loginframe31.place(rely = 0.40, relx = 0.70)

        self.btnback5 = Label(self.Loginframe31, image = Imgback5, bd = 0, bg='#FFFFFF',)
        self.btnback5.place(x=0, y=0)



        self.Loginframe4 = Frame(self, width = 950, height = 200, bg='#FFFFFF', bd = 20, relief = 'flat')
        self.Loginframe4.grid(row = 1, column = 0)

        self.Loginframe310 = Frame(self.Loginframe01, width = 70, height = 60, bd = 0, bg='#FFFFFF', relief = 'flat')
        self.Loginframe310.place(rely = 0, relx = 0.89)

        self.btnreturnh = Button(self.Loginframe310, image = ImgREhome, bd = 0, bg='#FFFFFF', command = lambda: master.switch_frame(StartPage))
        self.btnreturnh.place(x=0, y=0)

        logo = Image.open('logo_cnrst_2018.png')
        logo = ImageTk.PhotoImage(logo)
        logo_label =  Label(self.Loginframe1, bd = 0, bg='#FFFFFF', image = logo)
        logo_label.Image = logo
        logo_label.grid(column=0, row=0)

        logo1 = Image.open('logo_fsdm.png')
        logo1 = ImageTk.PhotoImage(logo1)
        logo_label1 =  Label(self.Loginframe1, bd = 0, bg='#FFFFFF', image = logo1)
        logo_label1.Image = logo1
        logo_label1.grid(column=1, row=0)

        logo2 = Image.open('logo-ministère-santé-Maroc.jpg')
        logo2 = ImageTk.PhotoImage(logo2)
        logo_label2 =  Label(self.Loginframe1, bd = 0, bg='#FFFFFF', image = logo2)
        logo_label2.Image = logo2
        logo_label2.grid(column=2, row=0)


        self.LabelTitle = Label(self.Loginframe14, image = ImgLabel, bg='#FFFFFF', bd = 0)
        self.LabelTitle.place(x=0, y=0)



        self.btnAnalyse = Button(self.Loginframe15, image = ImgAnalyse, bd = 0, bg='#FFFFFF', command = lambda: master.switch_frame(AnalyseWindow))
        self.btnAnalyse.place(rely = 0, relx = 0.15)

        self.btnPredective = Button(self.Loginframe15, image = ImgPredictive, bd = 0, bg='#FFFFFF', command = lambda: master.switch_frame(PredictiveWindow))
        self.btnPredective.place(rely = 0.20, relx = 0.15)

        self.btninfo = Button(self.Loginframe4, image =  Imginfo , bg = '#FFFFFF', bd = 0, command = self.info_window)
        self.btninfo.place(rely = 0, relx = 0.01)

        self.btnback6 = Label(self.Loginframe4, image = Imgback6, bd = 0, bg='#FFFFFF',)
        self.btnback6.place(rely = -0.30, relx = 0.31)

        self.btnaide = Button(self.Loginframe4, image = Imgaide, bg = '#FFFFFF', bd = 0, command = self.aide_window)
        self.btnaide.place(rely = 0, relx = 0.71)




    def info_window(self):
        self.infoWindow = Toplevel(self.master)
        self.app = Info(self.infoWindow)



    def aide_window(self):
        self.aideWindow = Toplevel(self.master)
        self.app = Aide(self.aideWindow)

    def return_window(self):
       self.returnWindow = Toplevel(self.master)
       self.app = Window1(self.returnWindow)

class AnalyseWindow(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.title("COVID19sim")

        self.app_width = 900
        self.app_height = 615


        self.screen_width = self.master.winfo_screenwidth()
        self.screen_height = self.master.winfo_screenheight()

        x = (self.screen_width / 2) - (self.app_width / 2)
        y = (self.screen_height / 2) - (self.app_height /2)

        self.master.geometry(f'{self.app_width}x{self.app_height}+{int(x)}+{int(y)}')

        self.master.config(bg='#FFFFFF')
        self.master.iconbitmap("logo.ico")


        self.config(bg = '#FFFFFF')


        ImgREhome = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\returnbuttonhome.png')
        ImgREhome = ImageTk.PhotoImage(ImgREhome)
        ImaREhomer =  Label(self, image = ImgREhome)
        ImaREhomer.Image = ImgREhome

        ImgREp = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\returnbutton.jpg')
        ImgREp = ImageTk.PhotoImage(ImgREp)
        ImaREpr =  Label(self, image = ImgREp)
        ImaREpr.Image = ImgREp


        ImgLabel = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\COVID19SIM.png')
        ImgLabel = ImageTk.PhotoImage(ImgLabel)
        Imalabelr =  Label(self, image = ImgLabel)
        Imalabelr.Image = ImgLabel




        ImgLocale = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\localbutton.png')
        ImgLocale = ImageTk.PhotoImage(ImgLocale)
        ImaLocaler =  Label(self, image = ImgLocale)
        ImaLocaler.Image = ImgLocale

        ImgRegionale = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\regionalbutton.png')
        ImgRegionale = ImageTk.PhotoImage(ImgRegionale)
        ImaRegionaler =  Label(self, image = ImgRegionale)
        ImaRegionaler.Image = ImgRegionale

        ImgNationale = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\nationalbutton.png')
        ImgNationale = ImageTk.PhotoImage(ImgNationale)
        ImaNationaler =  Label(self, image = ImgNationale)
        ImaNationaler.Image = ImgNationale

        Imginfo = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\infobutton.png')
        Imginfo = ImageTk.PhotoImage(Imginfo)
        Imainfor =  Label(self, image = Imginfo)
        Imainfor.Image = Imginfo

        Imgaide = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\aidebutton.png')
        Imgaide = ImageTk.PhotoImage(Imgaide)
        Imaaider =  Label(self, image = Imgaide)
        Imaaider.Image = Imgaide

        Imgback4 = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\back4.jpg')
        Imgback4 = ImageTk.PhotoImage(Imgback4)
        Imaback4r =  Label(self, image = Imgback4)
        Imaback4r.Image = Imgback4

        Imgback5 = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\back51.jpg')
        Imgback5 = ImageTk.PhotoImage(Imgback5)
        Imaback5r =  Label(self, image = Imgback5)
        Imaback5r.Image = Imgback5

        Imgback6 = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\back6.jpg')
        Imgback6 = ImageTk.PhotoImage(Imgback6)
        Imaback6r =  Label(self, image = Imgback6)
        Imaback6r.Image = Imgback6


        self.Loginframe01 = Frame(self, width = 950, height = 500, bd = 0, bg='#FFFFFF', relief = 'flat')
        self.Loginframe01.grid(row = 0, column = 0)

        self.Loginframe0 = Frame(self.Loginframe01, width = 200, height = 200, bd = 0, bg='#FFFFFF', relief = 'flat')
        self.Loginframe0.place(rely = 0, relx = 0)


        self.btnreturn = Button(self.Loginframe0, image = ImgREp, bd = 0, bg='#FFFFFF', command = lambda: master.switch_frame(PageOne))
        self.btnreturn.place(x=0.20, y=0)



        self.Loginframe1 = Frame(self.Loginframe01, width = 300, height = 200, bd = 5, bg='#FFFFFF', relief = 'flat')
        self.Loginframe1.place(rely = 0, relx = 0.27)



        self.Loginframe15 = Frame(self, width = 450, height = 400, bd = 0, bg= '#FFFFFF', relief = 'flat')
        self.Loginframe15.place(rely = 0.40, relx = 0.26)

        self.Loginframe30 = Frame(self.Loginframe01, width = 300, height = 500, bd = 0, bg='#FFFFFF', relief = 'flat')
        self.Loginframe30.place(rely = 0.30, relx = 0)

        self.btnback4 = Label(self.Loginframe30, image = Imgback4, bd = 0, bg='#FFFFFF',)
        self.btnback4.place(x=-0.20, y=0)

        self.Loginframe31 = Frame(self.Loginframe01, width = 300, height = 500, bd = 0, bg='#FFFFFF', relief = 'flat')
        self.Loginframe31.place(rely = 0.40, relx = 0.70)

        self.btnback5 = Label(self.Loginframe31, image = Imgback5, bd = 0, bg='#FFFFFF',)
        self.btnback5.place(x=0, y=0)

        self.Loginframe4 = Frame(self, width = 950, height = 200, bg='#FFFFFF', bd = 20, relief = 'flat')
        self.Loginframe4.grid(row = 1, column = 0)

        self.Loginframe310 = Frame(self.Loginframe01, width = 70, height = 60, bd = 0, bg='#FFFFFF', relief = 'flat')
        self.Loginframe310.place(rely = 0, relx = 0.89)

        self.btnreturnh = Button(self.Loginframe310, image = ImgREhome, bd = 0, bg='#FFFFFF', command = lambda: master.switch_frame(StartPage))
        self.btnreturnh.place(x=0, y=0)

        logo = Image.open('logo_cnrst_2018.png')
        logo = ImageTk.PhotoImage(logo)
        logo_label =  Label(self.Loginframe1, bd = 0, bg='#FFFFFF', image = logo)
        logo_label.Image = logo
        logo_label.grid(column=0, row=0)

        logo1 = Image.open('logo_fsdm.png')
        logo1 = ImageTk.PhotoImage(logo1)
        logo_label1 =  Label(self.Loginframe1, bd = 0, bg='#FFFFFF', image = logo1)
        logo_label1.Image = logo1
        logo_label1.grid(column=1, row=0)

        logo2 = Image.open('logo-ministère-santé-Maroc.jpg')
        logo2 = ImageTk.PhotoImage(logo2)
        logo_label2 =  Label(self.Loginframe1, bd = 0, bg='#FFFFFF', image = logo2)
        logo_label2.Image = logo2
        logo_label2.grid(column=2, row=0)


        self.LabelTitle = Label(self, image = ImgLabel, bg='#FFFFFF', bd = 0)
        self.LabelTitle.place(rely = 0.28, relx = 0.30)



        self.btnLocale = Button(self.Loginframe15, image = ImgLocale, bd = 0, bg='#FFFFFF', command = lambda: master.switch_frame(localWindowA))
        self.btnLocale.place(rely = 0.06, relx = 0.18)

        self.btnRegionale = Button(self.Loginframe15, image = ImgRegionale, bd = 0, bg='#FFFFFF', command = lambda: master.switch_frame(regionalWindowA))
        self.btnRegionale.place(rely = 0.23, relx = 0.18)

        self.btnNational = Button(self.Loginframe15, image = ImgNationale, bd = 0, bg='#FFFFFF', command = lambda: master.switch_frame(nationalWindowA))
        self.btnNational.place(rely = 0.40, relx = 0.18)

        self.btninfo = Button(self.Loginframe4, image =  Imginfo , bg = '#FFFFFF', bd = 0, command = self.info_window)
        self.btninfo.place(rely = 0, relx = 0.01)

        self.btnback6 = Label(self.Loginframe4, image = Imgback6, bd = 0, bg='#FFFFFF',)
        self.btnback6.place(rely = -0.30, relx = 0.31)

        self.btnaide = Button(self.Loginframe4, image = Imgaide, bg = '#FFFFFF', bd = 0, command = self.aide_window)
        self.btnaide.place(rely = 0, relx = 0.71)


    def info_window(self):
        self.infoWindow = Toplevel(self.master)
        self.app = Info(self.infoWindow)



    def aide_window(self):
        self.aideWindow = Toplevel(self.master)
        self.app = Aide(self.aideWindow)

class PredictiveWindow(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.title("COVID19sim")

        self.app_width = 900
        self.app_height = 615


        self.screen_width = self.master.winfo_screenwidth()
        self.screen_height = self.master.winfo_screenheight()

        x = (self.screen_width / 2) - (self.app_width / 2)
        y = (self.screen_height / 2) - (self.app_height /2)

        self.master.geometry(f'{self.app_width}x{self.app_height}+{int(x)}+{int(y)}')

        self.master.config(bg='#FFFFFF')
        self.master.iconbitmap("logo.ico")


        self.config(bg = '#FFFFFF')


        ImgREhome = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\returnbuttonhome.png')
        ImgREhome = ImageTk.PhotoImage(ImgREhome)
        ImaREhomer =  Label(self, image = ImgREhome)
        ImaREhomer.Image = ImgREhome

        ImgREp = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\returnbutton.jpg')
        ImgREp = ImageTk.PhotoImage(ImgREp)
        ImaREpr =  Label(self, image = ImgREp)
        ImaREpr.Image = ImgREp


        ImgLabel = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\COVID19SIM.png')
        ImgLabel = ImageTk.PhotoImage(ImgLabel)
        Imalabelr =  Label(self, image = ImgLabel)
        Imalabelr.Image = ImgLabel




        ImgLocale = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\localbutton.png')
        ImgLocale = ImageTk.PhotoImage(ImgLocale)
        ImaLocaler =  Label(self, image = ImgLocale)
        ImaLocaler.Image = ImgLocale

        ImgRegionale = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\regionalbutton.png')
        ImgRegionale = ImageTk.PhotoImage(ImgRegionale)
        ImaRegionaler =  Label(self, image = ImgRegionale)
        ImaRegionaler.Image = ImgRegionale

        ImgNationale = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\nationalbutton.png')
        ImgNationale = ImageTk.PhotoImage(ImgNationale)
        ImaNationaler =  Label(self, image = ImgNationale)
        ImaNationaler.Image = ImgNationale

        Imginfo = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\infobutton.png')
        Imginfo = ImageTk.PhotoImage(Imginfo)
        Imainfor =  Label(self, image = Imginfo)
        Imainfor.Image = Imginfo

        Imgaide = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\aidebutton.png')
        Imgaide = ImageTk.PhotoImage(Imgaide)
        Imaaider =  Label(self, image = Imgaide)
        Imaaider.Image = Imgaide

        Imgback4 = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\back4.jpg')
        Imgback4 = ImageTk.PhotoImage(Imgback4)
        Imaback4r =  Label(self, image = Imgback4)
        Imaback4r.Image = Imgback4

        Imgback5 = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\back51.jpg')
        Imgback5 = ImageTk.PhotoImage(Imgback5)
        Imaback5r =  Label(self, image = Imgback5)
        Imaback5r.Image = Imgback5

        Imgback6 = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\back6.jpg')
        Imgback6 = ImageTk.PhotoImage(Imgback6)
        Imaback6r =  Label(self, image = Imgback6)
        Imaback6r.Image = Imgback6


        self.Loginframe01 = Frame(self, width = 950, height = 500, bd = 0, bg='#FFFFFF', relief = 'flat')
        self.Loginframe01.grid(row = 0, column = 0)

        self.Loginframe0 = Frame(self.Loginframe01, width = 200, height = 200, bd = 0, bg='#FFFFFF', relief = 'flat')
        self.Loginframe0.place(rely = 0, relx = 0)


        self.btnreturn = Button(self.Loginframe0, image = ImgREp, bd = 0, bg='#FFFFFF', command = lambda: master.switch_frame(PageOne))
        self.btnreturn.place(x=0.20, y=0)



        self.Loginframe1 = Frame(self.Loginframe01, width = 300, height = 200, bd = 5, bg='#FFFFFF', relief = 'flat')
        self.Loginframe1.place(rely = 0, relx = 0.27)



        self.Loginframe15 = Frame(self, width = 450, height = 400, bd = 0, bg= '#FFFFFF', relief = 'flat')
        self.Loginframe15.place(rely = 0.40, relx = 0.26)

        self.Loginframe30 = Frame(self.Loginframe01, width = 300, height = 500, bd = 0, bg='#FFFFFF', relief = 'flat')
        self.Loginframe30.place(rely = 0.30, relx = 0)

        self.btnback4 = Label(self.Loginframe30, image = Imgback4, bd = 0, bg='#FFFFFF',)
        self.btnback4.place(x=-0.20, y=0)

        self.Loginframe31 = Frame(self.Loginframe01, width = 300, height = 500, bd = 0, bg='#FFFFFF', relief = 'flat')
        self.Loginframe31.place(rely = 0.40, relx = 0.70)

        self.btnback5 = Label(self.Loginframe31, image = Imgback5, bd = 0, bg='#FFFFFF',)
        self.btnback5.place(x=0, y=0)

        self.Loginframe4 = Frame(self, width = 950, height = 200, bg='#FFFFFF', bd = 20, relief = 'flat')
        self.Loginframe4.grid(row = 1, column = 0)

        self.Loginframe310 = Frame(self.Loginframe01, width = 70, height = 60, bd = 0, bg='#FFFFFF', relief = 'flat')
        self.Loginframe310.place(rely = 0, relx = 0.89)

        self.btnreturnh = Button(self.Loginframe310, image = ImgREhome, bd = 0, bg='#FFFFFF', command = lambda: master.switch_frame(StartPage))
        self.btnreturnh.place(x=0, y=0)

        logo = Image.open('logo_cnrst_2018.png')
        logo = ImageTk.PhotoImage(logo)
        logo_label =  Label(self.Loginframe1, bd = 0, bg='#FFFFFF', image = logo)
        logo_label.Image = logo
        logo_label.grid(column=0, row=0)

        logo1 = Image.open('logo_fsdm.png')
        logo1 = ImageTk.PhotoImage(logo1)
        logo_label1 =  Label(self.Loginframe1, bd = 0, bg='#FFFFFF', image = logo1)
        logo_label1.Image = logo1
        logo_label1.grid(column=1, row=0)

        logo2 = Image.open('logo-ministère-santé-Maroc.jpg')
        logo2 = ImageTk.PhotoImage(logo2)
        logo_label2 =  Label(self.Loginframe1, bd = 0, bg='#FFFFFF', image = logo2)
        logo_label2.Image = logo2
        logo_label2.grid(column=2, row=0)

        self.LabelTitle = Label(self, image = ImgLabel, bg='#FFFFFF', bd = 0)
        self.LabelTitle.place(rely = 0.28, relx = 0.30)



        self.btnLocale = Button(self.Loginframe15, image = ImgLocale, bd = 0, bg='#FFFFFF', command = lambda: master.switch_frame(localWindowA))
        self.btnLocale.place(rely = 0.06, relx = 0.18)

        self.btnRegionale = Button(self.Loginframe15, image = ImgRegionale, bd = 0, bg='#FFFFFF', command = lambda: master.switch_frame(regionalWindowA))
        self.btnRegionale.place(rely = 0.23, relx = 0.18)

        self.btnNational = Button(self.Loginframe15, image = ImgNationale, bd = 0, bg='#FFFFFF', command = lambda: master.switch_frame(nationalWindowA))
        self.btnNational.place(rely = 0.40, relx = 0.18)

        self.btninfo = Button(self.Loginframe4, image =  Imginfo , bg = '#FFFFFF', bd = 0, command = self.info_window)
        self.btninfo.place(rely = 0, relx = 0.01)

        self.btnback6 = Label(self.Loginframe4, image = Imgback6, bd = 0, bg='#FFFFFF',)
        self.btnback6.place(rely = -0.30, relx = 0.31)

        self.btnaide = Button(self.Loginframe4, image = Imgaide, bg = '#FFFFFF', bd = 0, command = self.aide_window)
        self.btnaide.place(rely = 0, relx = 0.71)


    def info_window(self):
        self.infoWindow = Toplevel(self.master)
        self.app = Info(self.infoWindow)



    def aide_window(self):
        self.aideWindow = Toplevel(self.master)
        self.app = Aide(self.aideWindow)


class localWindowA(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.title("Locale analyse")

        self.app_width = 900
        self.app_height = 615


        self.screen_width = self.master.winfo_screenwidth()
        self.screen_height = self.master.winfo_screenheight()

        x = (self.screen_width / 2) - (self.app_width / 2)
        y = (self.screen_height / 2) - (self.app_height /2)

        self.master.geometry(f'{self.app_width}x{self.app_height}+{int(x)}+{int(y)}')

        self.master.iconbitmap("logo.ico")
        self.config(bg = '#FFFFFF')

        ImgREhome = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\returnbuttonhome.png')
        ImgREhome = ImageTk.PhotoImage(ImgREhome)
        ImaREhomer =  Label(self, image = ImgREhome)
        ImaREhomer.Image = ImgREhome

        ImgREp = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\returnbutton.jpg')
        ImgREp = ImageTk.PhotoImage(ImgREp)
        ImaREpr =  Label(self, image = ImgREp)
        ImaREpr.Image = ImgREp

        ImgLabel = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\LOCALE.png')
        ImgLabel = ImageTk.PhotoImage(ImgLabel)
        Imalabelr =  Label(self, image = ImgLabel)
        Imalabelr.Image = ImgLabel


        ImgSubmit = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\submitbutton.png')
        ImgSubmit = ImageTk.PhotoImage(ImgSubmit)
        ImaSubmitr =  Label(self, image = ImgSubmit)
        ImaSubmitr.Image = ImgSubmit


        ImgAdd = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\addcitybutton.png')
        ImgAdd = ImageTk.PhotoImage(ImgAdd)
        ImaAddr =  Label(self, image = ImgAdd)
        ImaAddr.Image = ImgAdd

        ImgMap = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\mapbutton.png')
        ImgMap = ImageTk.PhotoImage(ImgMap)
        ImaMapr =  Label(self, image = ImgMap)
        ImaMapr.Image = ImgMap

        ImgGraph = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\graphbutton.png')
        ImgGraph = ImageTk.PhotoImage(ImgGraph)
        ImaGraphr =  Label(self, image = ImgGraph)
        ImaGraphr.Image = ImgGraph


        Imgback7 = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\back7.jpg')
        Imgback7 = ImageTk.PhotoImage(Imgback7)
        Imaback7r =  Label(self, image = Imgback7)
        Imaback7r.Image = Imgback7

        Imgback8 = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\back8.jpg')
        Imgback8 = ImageTk.PhotoImage(Imgback8)
        Imaback8r =  Label(self, image = Imgback8)
        Imaback8r.Image = Imgback8

        Imginfo = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\infobutton.png')
        Imginfo = ImageTk.PhotoImage(Imginfo)
        Imainfor =  Label(self, image = Imginfo)
        Imainfor.Image = Imginfo

        Imgaide = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\aidebutton.png')
        Imgaide = ImageTk.PhotoImage(Imgaide)
        Imaaider =  Label(self, image = Imgaide)
        Imaaider.Image = Imgaide

        self.Loginframe01 = Frame(self, width = 950, height = 520, bd = 0, bg='#FFFFFF', relief = 'flat')
        self.Loginframe01.grid(row = 0, column = 0)

        self.Loginframe0 = Frame(self.Loginframe01, width = 200, height = 200, bd = 0, bg='#FFFFFF', relief = 'flat')
        self.Loginframe0.place(rely = 0, relx = 0)


        self.btnreturn = Button(self.Loginframe0, image = ImgREp, bd = 0, bg='#FFFFFF', command = lambda: master.switch_frame(AnalyseWindow))
        self.btnreturn.place(x=0.20, y=0)



        self.Loginframe1 = Frame(self.Loginframe01, width = 300, height = 200, bd = 5, bg='#FFFFFF', relief = 'flat')
        self.Loginframe1.place(rely = 0, relx = 0.27)


        self.Loginframe310 = Frame(self.Loginframe01, width = 70, height = 60, bd = 0, bg='#FFFFFF', relief = 'flat')
        self.Loginframe310.place(rely = 0, relx = 0.89)

        self.btnreturnh = Button(self.Loginframe310, image = ImgREhome, bd = 0, bg='#FFFFFF', command = lambda: master.switch_frame(StartPage))
        self.btnreturnh.place(x=0, y=0)


        logo = Image.open('logo_cnrst_2018.png')
        logo = ImageTk.PhotoImage(logo)
        logo_label =  Label(self.Loginframe1, bd = 0, bg='#FFFFFF', image = logo)
        logo_label.Image = logo
        logo_label.grid(column=0, row=0)

        logo1 = Image.open('logo_fsdm.png')
        logo1 = ImageTk.PhotoImage(logo1)
        logo_label1 =  Label(self.Loginframe1, bd = 0, bg='#FFFFFF', image = logo1)
        logo_label1.Image = logo1
        logo_label1.grid(column=1, row=0)

        logo2 = Image.open('logo-ministère-santé-Maroc.jpg')
        logo2 = ImageTk.PhotoImage(logo2)
        logo_label2 =  Label(self.Loginframe1, bd = 0, bg='#FFFFFF', image = logo2)
        logo_label2.Image = logo2
        logo_label2.grid(column=2, row=0)

        self.LabelTitle = Label(self, image = ImgLabel, bg='#FFFFFF', bd = 0)
        self.LabelTitle.place(rely = 0.22, relx = 0.36)

        self.lbback7 = Label(self, image = Imgback7, bd = 0, bg='#FFFFFF',)
        self.lbback7.place(rely = 0.10, relx = 0)

        self.lbback8 = Label(self, image = Imgback8, bd = 0, bg='#FFFFFF',)
        self.lbback8.place(rely = 0.10, relx = 0.75)



        # name files
        self.files = ['Fes', 'Rabat', 'Meknes', 'Tanger', 'Casablanca', 'Kenitra', 'Eljadida', 'Tetoune', 'Oujda', 'Layoune', 'Dakhla']
#---------------------------------------------------------------------------------------------------------------------------------------
        date = StringVar()
        Susceptible = StringVar()
        Exposed = StringVar()
        Symptomatic = StringVar()
        Asymptomatic = StringVar()
        Hospitalized = StringVar()
        Quarantined = StringVar()
        Recovered = StringVar()
        Dead = StringVar()
        Vaccinated = StringVar()
        population = StringVar()

        conn = sqlite3.connect("dataCovid19sim.db")
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS Cityparametres(date TEXT,Susceptible TEXT,Exposed TEXT,Symptomatic TEXT,Asymptomatic TEXT,Hospitalized TEXT,Quarantined TEXT, Recovered TEXT, Dead TEXT,Vaccinated TEXT, population TEXT)')

        # create a combobox
        self.selected_files = tk.StringVar()


        self.Loginframe2 = Frame(self, width = 30, height = 50, bd = 20, bg = '#FFFFFF' ,relief = 'flat')
        self.Loginframe2.place(rely = 0.35, relx = 0.25)

        self.files_cb = ttk.Combobox(self.Loginframe2, width = 28, textvariable = self.selected_files)
        self.files_cb['values'] = self.files
        self.files_cb['state'] = 'normal'  # normal
        self.files_cb.grid(row = 15, column = 1)
        self.files_cb.current()
        self.files_cb.bind('<<ComboboxSelected>>')



        self.btnSoumettre = Button(self, image = ImgSubmit, bd = 0, bg = '#FFFFFF', command = lambda : Load_execl_data())
        self.btnSoumettre.place(rely = 0.36, relx = 0.53)




        self.Loginframe711 = Frame(self, width = 440, height = 220, bd = 20, bg='#d1e9d3', relief = 'ridge')
        self.Loginframe711.place(rely = 0.47, relx = 0.35)


        self.frame = LabelFrame(self.Loginframe711, bg = '#d1e9d3', fg ='#1b458f',  text="Les données")
        self.frame.place(height = 180, width = 400)


        tv1 = ttk.Treeview(self.frame)
        tv1.place(relheight = 1, relwidth = 1)

        treescrolly = Scrollbar(self.frame, orient = "vertical", command = tv1.yview)
        treescrollx = Scrollbar(self.frame, orient = "horizontal", command = tv1.xview)




        tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
        treescrollx.pack(side="bottom", fill="x")
        treescrolly.pack(side="right", fill="y")

        def Load_execl_data():
            file_path = f'C:\\Users\\pcc\\Desktop\\Covid19sim\\{self.files_cb.get()}.xlsx'
            try:
                excel_filename = r"{}".format(file_path)
                df = pd.read_excel(excel_filename)
            except ValueError:
                tk.messagebox.showerror("Information", "The file you have entered is invalid")
                return None
            except FileNotFoundError:
                tk.messagebox.showerror("Information", f"No such file as {self.files_cb.get()}")
                return None

            clear_data()
            tv1["columns"] = list(df.columns)
            tv1["show"] = "headings"
            for column in tv1["columns"]:
                tv1.heading(column, text=column)
            df_rows = df.to_numpy().tolist()

            for row in df_rows:
                tv1.insert("", "end", values=row)


        def clear_data():
            tv1.delete(*tv1.get_children())



        self.btnAdd = Button(self, image = ImgAdd,  bg='#FFFFFF', bd = 0, command = lambda: master.switch_frame(connectorDB))
        self.btnAdd.place(rely = 0.44, relx = 0.03)



        self.btnMap = Button(self, image = ImgMap , bd = 0, bg='#FFFFFF', command = lambda: master.switch_frame(Map))
        self.btnMap.place(rely = 0.66, relx = 0.03)



        self.btnGraph = Button(self, image = ImgGraph, bd = 0, bg = '#FFFFFF',  command = lambda: master.switch_frame(Graph))
        self.btnGraph.place(rely = 0.55, relx = 0.03)

        self.Loginframe4 = Frame(self, width = 950, height = 150, bg='#FFFFFF', bd = 20, relief = 'flat')
        self.Loginframe4.grid(row = 1, column = 0)

        self.btninfo = Button(self.Loginframe4, image =  Imginfo , bg = '#FFFFFF', bd = 0, command = self.info_window)
        self.btninfo.place(rely = 0, relx = 0.01)


        self.btnaide = Button(self.Loginframe4, image = Imgaide, bg = '#FFFFFF', bd = 0, command = self.aide_window)
        self.btnaide.place(rely = 0, relx = 0.71)

    def info_window(self):
        self.infoWindow = Toplevel(self.master)
        self.app = Info(self.infoWindow)



    def aide_window(self):
        self.aideWindow = Toplevel(self.master)
        self.app = Aide(self.aideWindow)







class regionalWindowA(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.title("Regional analyse")

        self.app_width = 900
        self.app_height = 615


        self.screen_width = self.master.winfo_screenwidth()
        self.screen_height = self.master.winfo_screenheight()

        x = (self.screen_width / 2) - (self.app_width / 2)
        y = (self.screen_height / 2) - (self.app_height /2)

        self.master.geometry(f'{self.app_width}x{self.app_height}+{int(x)}+{int(y)}')

        self.master.iconbitmap("logo.ico")
        self.config(bg = '#FFFFFF')

        ImgREhome = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\returnbuttonhome.png')
        ImgREhome = ImageTk.PhotoImage(ImgREhome)
        ImaREhomer =  Label(self, image = ImgREhome)
        ImaREhomer.Image = ImgREhome

        ImgREp = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\returnbutton.jpg')
        ImgREp = ImageTk.PhotoImage(ImgREp)
        ImaREpr =  Label(self, image = ImgREp)
        ImaREpr.Image = ImgREp

        ImgLabel = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\REGIONAL.png')
        ImgLabel = ImageTk.PhotoImage(ImgLabel)
        Imalabelr =  Label(self, image = ImgLabel)
        Imalabelr.Image = ImgLabel


        ImgSubmit = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\submitbutton.png')
        ImgSubmit = ImageTk.PhotoImage(ImgSubmit)
        ImaSubmitr =  Label(self, image = ImgSubmit)
        ImaSubmitr.Image = ImgSubmit


        ImgAdd = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\addcitybutton.png')
        ImgAdd = ImageTk.PhotoImage(ImgAdd)
        ImaAddr =  Label(self, image = ImgAdd)
        ImaAddr.Image = ImgAdd

        ImgMap = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\mapbutton.png')
        ImgMap = ImageTk.PhotoImage(ImgMap)
        ImaMapr =  Label(self, image = ImgMap)
        ImaMapr.Image = ImgMap

        ImgGraph = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\graphbutton.png')
        ImgGraph = ImageTk.PhotoImage(ImgGraph)
        ImaGraphr =  Label(self, image = ImgGraph)
        ImaGraphr.Image = ImgGraph


        Imgback7 = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\back7.jpg')
        Imgback7 = ImageTk.PhotoImage(Imgback7)
        Imaback7r =  Label(self, image = Imgback7)
        Imaback7r.Image = Imgback7

        Imgback8 = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\back8.jpg')
        Imgback8 = ImageTk.PhotoImage(Imgback8)
        Imaback8r =  Label(self, image = Imgback8)
        Imaback8r.Image = Imgback8

        Imginfo = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\infobutton.png')
        Imginfo = ImageTk.PhotoImage(Imginfo)
        Imainfor =  Label(self, image = Imginfo)
        Imainfor.Image = Imginfo

        Imgaide = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\aidebutton.png')
        Imgaide = ImageTk.PhotoImage(Imgaide)
        Imaaider =  Label(self, image = Imgaide)
        Imaaider.Image = Imgaide

        self.Loginframe01 = Frame(self, width = 950, height = 520, bd = 0, bg='#FFFFFF', relief = 'flat')
        self.Loginframe01.grid(row = 0, column = 0)

        self.Loginframe0 = Frame(self.Loginframe01, width = 200, height = 200, bd = 0, bg='#FFFFFF', relief = 'flat')
        self.Loginframe0.place(rely = 0, relx = 0)


        self.btnreturn = Button(self.Loginframe0, image = ImgREp, bd = 0, bg='#FFFFFF', command = lambda: master.switch_frame(AnalyseWindow))
        self.btnreturn.place(x=0.20, y=0)



        self.Loginframe1 = Frame(self.Loginframe01, width = 300, height = 200, bd = 5, bg='#FFFFFF', relief = 'flat')
        self.Loginframe1.place(rely = 0, relx = 0.27)


        self.Loginframe310 = Frame(self.Loginframe01, width = 70, height = 60, bd = 0, bg='#FFFFFF', relief = 'flat')
        self.Loginframe310.place(rely = 0, relx = 0.89)

        self.btnreturnh = Button(self.Loginframe310, image = ImgREhome, bd = 0, bg='#FFFFFF', command = lambda: master.switch_frame(StartPage))
        self.btnreturnh.place(x=0, y=0)


        logo = Image.open('logo_cnrst_2018.png')
        logo = ImageTk.PhotoImage(logo)
        logo_label =  Label(self.Loginframe1, bd = 0, bg='#FFFFFF', image = logo)
        logo_label.Image = logo
        logo_label.grid(column=0, row=0)

        logo1 = Image.open('logo_fsdm.png')
        logo1 = ImageTk.PhotoImage(logo1)
        logo_label1 =  Label(self.Loginframe1, bd = 0, bg='#FFFFFF', image = logo1)
        logo_label1.Image = logo1
        logo_label1.grid(column=1, row=0)

        logo2 = Image.open('logo-ministère-santé-Maroc.jpg')
        logo2 = ImageTk.PhotoImage(logo2)
        logo_label2 =  Label(self.Loginframe1, bd = 0, bg='#FFFFFF', image = logo2)
        logo_label2.Image = logo2
        logo_label2.grid(column=2, row=0)

        self.LabelTitle = Label(self, image = ImgLabel, bg='#FFFFFF', bd = 0)
        self.LabelTitle.place(rely = 0.22, relx = 0.34)

        self.lbback7 = Label(self, image = Imgback7, bd = 0, bg='#FFFFFF',)
        self.lbback7.place(rely = 0.10, relx = 0)

        self.lbback8 = Label(self, image = Imgback8, bd = 0, bg='#FFFFFF',)
        self.lbback8.place(rely = 0.10, relx = 0.75)



        # name files
        self.files = ['Fes', 'Rabat', 'Meknes', 'Tanger', 'Casablanca', 'Kenitra', 'Eljadida', 'Tetoune', 'Oujda', 'Layoune', 'Dakhla']
#---------------------------------------------------------------------------------------------------------------------------------------
        date = StringVar()
        Susceptible = StringVar()
        Exposed = StringVar()
        Symptomatic = StringVar()
        Asymptomatic = StringVar()
        Hospitalized = StringVar()
        Quarantined = StringVar()
        Recovered = StringVar()
        Dead = StringVar()
        Vaccinated = StringVar()
        population = StringVar()

        conn = sqlite3.connect("dataCovid19sim.db")
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS Cityparametres(date TEXT,Susceptible TEXT,Exposed TEXT,Symptomatic TEXT,Asymptomatic TEXT,Hospitalized TEXT,Quarantined TEXT, Recovered TEXT, Dead TEXT,Vaccinated TEXT, population TEXT)')

        # create a combobox
        self.selected_files = tk.StringVar()


        self.Loginframe2 = Frame(self, width = 30, height = 50, bd = 20, bg = '#FFFFFF' ,relief = 'flat')
        self.Loginframe2.place(rely = 0.35, relx = 0.25)

        self.files_cb = ttk.Combobox(self.Loginframe2, width = 28, textvariable = self.selected_files)
        self.files_cb['values'] = self.files
        self.files_cb['state'] = 'normal'  # normal
        self.files_cb.grid(row = 15, column = 1)
        self.files_cb.current()
        self.files_cb.bind('<<ComboboxSelected>>')



        self.btnSoumettre = Button(self, image = ImgSubmit, bd = 0, bg = '#FFFFFF', command = lambda : Load_execl_data())
        self.btnSoumettre.place(rely = 0.36, relx = 0.53)




        self.Loginframe711 = Frame(self, width = 440, height = 220, bd = 20, bg='#d1e9d3', relief = 'ridge')
        self.Loginframe711.place(rely = 0.47, relx = 0.35)


        self.frame = LabelFrame(self.Loginframe711, bg = '#d1e9d3', fg ='#1b458f',  text="Les données")
        self.frame.place(height = 180, width = 400)


        tv1 = ttk.Treeview(self.frame)
        tv1.place(relheight = 1, relwidth = 1)

        treescrolly = Scrollbar(self.frame, orient = "vertical", command = tv1.yview)
        treescrollx = Scrollbar(self.frame, orient = "horizontal", command = tv1.xview)




        tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
        treescrollx.pack(side="bottom", fill="x")
        treescrolly.pack(side="right", fill="y")

        def Load_execl_data():
            file_path = f'C:\\Users\\pcc\\Desktop\\Covid19sim\\{self.files_cb.get()}.xlsx'
            try:
                excel_filename = r"{}".format(file_path)
                df = pd.read_excel(excel_filename)
            except ValueError:
                tk.messagebox.showerror("Information", "The file you have entered is invalid")
                return None
            except FileNotFoundError:
                tk.messagebox.showerror("Information", f"No such file as {self.files_cb.get()}")
                return None

            clear_data()
            tv1["columns"] = list(df.columns)
            tv1["show"] = "headings"
            for column in tv1["columns"]:
                tv1.heading(column, text=column)
            df_rows = df.to_numpy().tolist()

            for row in df_rows:
                tv1.insert("", "end", values=row)


        def clear_data():
            tv1.delete(*tv1.get_children())



        self.btnAdd = Button(self, image = ImgAdd,  bg='#FFFFFF', bd = 0, command = lambda: master.switch_frame(connectorDB))
        self.btnAdd.place(rely = 0.44, relx = 0.03)



        self.btnMap = Button(self, image = ImgMap , bd = 0, bg='#FFFFFF', command = lambda: master.switch_frame(Map))
        self.btnMap.place(rely = 0.66, relx = 0.03)



        self.btnGraph = Button(self, image = ImgGraph, bd = 0, bg = '#FFFFFF',  command = lambda: master.switch_frame(Graph))
        self.btnGraph.place(rely = 0.55, relx = 0.03)

        self.Loginframe4 = Frame(self, width = 950, height = 150, bg='#FFFFFF', bd = 20, relief = 'flat')
        self.Loginframe4.grid(row = 1, column = 0)

        self.btninfo = Button(self.Loginframe4, image =  Imginfo , bg = '#FFFFFF', bd = 0, command = self.info_window)
        self.btninfo.place(rely = 0, relx = 0.01)


        self.btnaide = Button(self.Loginframe4, image = Imgaide, bg = '#FFFFFF', bd = 0, command = self.aide_window)
        self.btnaide.place(rely = 0, relx = 0.71)

    def info_window(self):
        self.infoWindow = Toplevel(self.master)
        self.app = Info(self.infoWindow)



    def aide_window(self):
        self.aideWindow = Toplevel(self.master)
        self.app = Aide(self.aideWindow)

class nationalWindowA(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.title("Regional analyse")

        self.app_width = 900
        self.app_height = 615


        self.screen_width = self.master.winfo_screenwidth()
        self.screen_height = self.master.winfo_screenheight()

        x = (self.screen_width / 2) - (self.app_width / 2)
        y = (self.screen_height / 2) - (self.app_height /2)

        self.master.geometry(f'{self.app_width}x{self.app_height}+{int(x)}+{int(y)}')

        self.master.iconbitmap("logo.ico")
        self.config(bg = '#FFFFFF')

        ImgREhome = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\returnbuttonhome.png')
        ImgREhome = ImageTk.PhotoImage(ImgREhome)
        ImaREhomer =  Label(self, image = ImgREhome)
        ImaREhomer.Image = ImgREhome

        ImgREp = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\returnbutton.jpg')
        ImgREp = ImageTk.PhotoImage(ImgREp)
        ImaREpr =  Label(self, image = ImgREp)
        ImaREpr.Image = ImgREp

        ImgLabel = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\NATIONAL.png')
        ImgLabel = ImageTk.PhotoImage(ImgLabel)
        Imalabelr =  Label(self, image = ImgLabel)
        Imalabelr.Image = ImgLabel


        ImgSubmit = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\submitbutton.png')
        ImgSubmit = ImageTk.PhotoImage(ImgSubmit)
        ImaSubmitr =  Label(self, image = ImgSubmit)
        ImaSubmitr.Image = ImgSubmit


        ImgAdd = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\addcitybutton.png')
        ImgAdd = ImageTk.PhotoImage(ImgAdd)
        ImaAddr =  Label(self, image = ImgAdd)
        ImaAddr.Image = ImgAdd

        ImgMap = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\mapbutton.png')
        ImgMap = ImageTk.PhotoImage(ImgMap)
        ImaMapr =  Label(self, image = ImgMap)
        ImaMapr.Image = ImgMap

        ImgGraph = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\graphbutton.png')
        ImgGraph = ImageTk.PhotoImage(ImgGraph)
        ImaGraphr =  Label(self, image = ImgGraph)
        ImaGraphr.Image = ImgGraph


        Imgback7 = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\back7.jpg')
        Imgback7 = ImageTk.PhotoImage(Imgback7)
        Imaback7r =  Label(self, image = Imgback7)
        Imaback7r.Image = Imgback7

        Imgback8 = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\back8.jpg')
        Imgback8 = ImageTk.PhotoImage(Imgback8)
        Imaback8r =  Label(self, image = Imgback8)
        Imaback8r.Image = Imgback8

        Imginfo = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\infobutton.png')
        Imginfo = ImageTk.PhotoImage(Imginfo)
        Imainfor =  Label(self, image = Imginfo)
        Imainfor.Image = Imginfo

        Imgaide = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\aidebutton.png')
        Imgaide = ImageTk.PhotoImage(Imgaide)
        Imaaider =  Label(self, image = Imgaide)
        Imaaider.Image = Imgaide

        self.Loginframe01 = Frame(self, width = 950, height = 520, bd = 0, bg='#FFFFFF', relief = 'flat')
        self.Loginframe01.grid(row = 0, column = 0)

        self.Loginframe0 = Frame(self.Loginframe01, width = 200, height = 200, bd = 0, bg='#FFFFFF', relief = 'flat')
        self.Loginframe0.place(rely = 0, relx = 0)


        self.btnreturn = Button(self.Loginframe0, image = ImgREp, bd = 0, bg='#FFFFFF', command = lambda: master.switch_frame(AnalyseWindow))
        self.btnreturn.place(x=0.20, y=0)



        self.Loginframe1 = Frame(self.Loginframe01, width = 300, height = 200, bd = 5, bg='#FFFFFF', relief = 'flat')
        self.Loginframe1.place(rely = 0, relx = 0.27)


        self.Loginframe310 = Frame(self.Loginframe01, width = 70, height = 60, bd = 0, bg='#FFFFFF', relief = 'flat')
        self.Loginframe310.place(rely = 0, relx = 0.89)

        self.btnreturnh = Button(self.Loginframe310, image = ImgREhome, bd = 0, bg='#FFFFFF', command = lambda: master.switch_frame(StartPage))
        self.btnreturnh.place(x=0, y=0)


        logo = Image.open('logo_cnrst_2018.png')
        logo = ImageTk.PhotoImage(logo)
        logo_label =  Label(self.Loginframe1, bd = 0, bg='#FFFFFF', image = logo)
        logo_label.Image = logo
        logo_label.grid(column=0, row=0)

        logo1 = Image.open('logo_fsdm.png')
        logo1 = ImageTk.PhotoImage(logo1)
        logo_label1 =  Label(self.Loginframe1, bd = 0, bg='#FFFFFF', image = logo1)
        logo_label1.Image = logo1
        logo_label1.grid(column=1, row=0)

        logo2 = Image.open('logo-ministère-santé-Maroc.jpg')
        logo2 = ImageTk.PhotoImage(logo2)
        logo_label2 =  Label(self.Loginframe1, bd = 0, bg='#FFFFFF', image = logo2)
        logo_label2.Image = logo2
        logo_label2.grid(column=2, row=0)

        self.LabelTitle = Label(self, image = ImgLabel, bg='#FFFFFF', bd = 0)
        self.LabelTitle.place(rely = 0.22, relx = 0.34)

        self.lbback7 = Label(self, image = Imgback7, bd = 0, bg='#FFFFFF',)
        self.lbback7.place(rely = 0.10, relx = 0)

        self.lbback8 = Label(self, image = Imgback8, bd = 0, bg='#FFFFFF',)
        self.lbback8.place(rely = 0.10, relx = 0.75)



        # name files
        self.files = ['Fes', 'Rabat', 'Meknes', 'Tanger', 'Casablanca', 'Kenitra', 'Eljadida', 'Tetoune', 'Oujda', 'Layoune', 'Dakhla']
#---------------------------------------------------------------------------------------------------------------------------------------
        date = StringVar()
        Susceptible = StringVar()
        Exposed = StringVar()
        Symptomatic = StringVar()
        Asymptomatic = StringVar()
        Hospitalized = StringVar()
        Quarantined = StringVar()
        Recovered = StringVar()
        Dead = StringVar()
        Vaccinated = StringVar()
        population = StringVar()

        conn = sqlite3.connect("dataCovid19sim.db")
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS Cityparametres(date TEXT,Susceptible TEXT,Exposed TEXT,Symptomatic TEXT,Asymptomatic TEXT,Hospitalized TEXT,Quarantined TEXT, Recovered TEXT, Dead TEXT,Vaccinated TEXT, population TEXT)')

        # create a combobox
        self.selected_files = tk.StringVar()


        self.Loginframe2 = Frame(self, width = 30, height = 50, bd = 20, bg = '#FFFFFF' ,relief = 'flat')
        self.Loginframe2.place(rely = 0.35, relx = 0.25)

        self.files_cb = ttk.Combobox(self.Loginframe2, width = 28, textvariable = self.selected_files)
        self.files_cb['values'] = self.files
        self.files_cb['state'] = 'normal'  # normal
        self.files_cb.grid(row = 15, column = 1)
        self.files_cb.current()
        self.files_cb.bind('<<ComboboxSelected>>')



        self.btnSoumettre = Button(self, image = ImgSubmit, bd = 0, bg = '#FFFFFF', command = lambda : Load_execl_data())
        self.btnSoumettre.place(rely = 0.36, relx = 0.53)




        self.Loginframe711 = Frame(self, width = 440, height = 220, bd = 20, bg='#d1e9d3', relief = 'ridge')
        self.Loginframe711.place(rely = 0.47, relx = 0.35)


        self.frame = LabelFrame(self.Loginframe711, bg = '#d1e9d3', fg ='#1b458f',  text="Les données")
        self.frame.place(height = 180, width = 400)


        tv1 = ttk.Treeview(self.frame)
        tv1.place(relheight = 1, relwidth = 1)

        treescrolly = Scrollbar(self.frame, orient = "vertical", command = tv1.yview)
        treescrollx = Scrollbar(self.frame, orient = "horizontal", command = tv1.xview)




        tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
        treescrollx.pack(side="bottom", fill="x")
        treescrolly.pack(side="right", fill="y")

        def Load_execl_data():
            file_path = f'C:\\Users\\pcc\\Desktop\\Covid19sim\\{self.files_cb.get()}.xlsx'
            try:
                excel_filename = r"{}".format(file_path)
                df = pd.read_excel(excel_filename)
            except ValueError:
                tk.messagebox.showerror("Information", "The file you have entered is invalid")
                return None
            except FileNotFoundError:
                tk.messagebox.showerror("Information", f"No such file as {self.files_cb.get()}")
                return None

            clear_data()
            tv1["columns"] = list(df.columns)
            tv1["show"] = "headings"
            for column in tv1["columns"]:
                tv1.heading(column, text=column)
            df_rows = df.to_numpy().tolist()

            for row in df_rows:
                tv1.insert("", "end", values=row)


        def clear_data():
            tv1.delete(*tv1.get_children())



        self.btnAdd = Button(self, image = ImgAdd,  bg='#FFFFFF', bd = 0, command = lambda: master.switch_frame(connectorDB))
        self.btnAdd.place(rely = 0.44, relx = 0.03)



        self.btnMap = Button(self, image = ImgMap , bd = 0, bg='#FFFFFF', command = lambda: master.switch_frame(Map))
        self.btnMap.place(rely = 0.66, relx = 0.03)



        self.btnGraph = Button(self, image = ImgGraph, bd = 0, bg = '#FFFFFF',  command = lambda: master.switch_frame(Graph))
        self.btnGraph.place(rely = 0.55, relx = 0.03)

        self.Loginframe4 = Frame(self, width = 950, height = 150, bg='#FFFFFF', bd = 20, relief = 'flat')
        self.Loginframe4.grid(row = 1, column = 0)

        self.btninfo = Button(self.Loginframe4, image =  Imginfo , bg = '#FFFFFF', bd = 0, command = self.info_window)
        self.btninfo.place(rely = 0, relx = 0.01)


        self.btnaide = Button(self.Loginframe4, image = Imgaide, bg = '#FFFFFF', bd = 0, command = self.aide_window)
        self.btnaide.place(rely = 0, relx = 0.71)

    def info_window(self):
        self.infoWindow = Toplevel(self.master)
        self.app = Info(self.infoWindow)



    def aide_window(self):
        self.aideWindow = Toplevel(self.master)
        self.app = Aide(self.aideWindow)

class localWindowP(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.title("Locale analyse")

        self.app_width = 900
        self.app_height = 615


        self.screen_width = self.master.winfo_screenwidth()
        self.screen_height = self.master.winfo_screenheight()

        x = (self.screen_width / 2) - (self.app_width / 2)
        y = (self.screen_height / 2) - (self.app_height /2)

        self.master.geometry(f'{self.app_width}x{self.app_height}+{int(x)}+{int(y)}')

        self.master.iconbitmap("logo.ico")
        self.config(bg = '#FFFFFF')

        ImgREhome = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\returnbuttonhome.png')
        ImgREhome = ImageTk.PhotoImage(ImgREhome)
        ImaREhomer =  Label(self, image = ImgREhome)
        ImaREhomer.Image = ImgREhome

        ImgREp = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\returnbutton.jpg')
        ImgREp = ImageTk.PhotoImage(ImgREp)
        ImaREpr =  Label(self, image = ImgREp)
        ImaREpr.Image = ImgREp

        ImgLabel = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\LOCALE.png')
        ImgLabel = ImageTk.PhotoImage(ImgLabel)
        Imalabelr =  Label(self, image = ImgLabel)
        Imalabelr.Image = ImgLabel


        ImgSubmit = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\submitbutton.png')
        ImgSubmit = ImageTk.PhotoImage(ImgSubmit)
        ImaSubmitr =  Label(self, image = ImgSubmit)
        ImaSubmitr.Image = ImgSubmit


        ImgAdd = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\addcitybutton.png')
        ImgAdd = ImageTk.PhotoImage(ImgAdd)
        ImaAddr =  Label(self, image = ImgAdd)
        ImaAddr.Image = ImgAdd

        ImgMap = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\mapbutton.png')
        ImgMap = ImageTk.PhotoImage(ImgMap)
        ImaMapr =  Label(self, image = ImgMap)
        ImaMapr.Image = ImgMap

        ImgGraph = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\graphbutton.png')
        ImgGraph = ImageTk.PhotoImage(ImgGraph)
        ImaGraphr =  Label(self, image = ImgGraph)
        ImaGraphr.Image = ImgGraph


        Imgback7 = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\back7.jpg')
        Imgback7 = ImageTk.PhotoImage(Imgback7)
        Imaback7r =  Label(self, image = Imgback7)
        Imaback7r.Image = Imgback7

        Imgback8 = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\back8.jpg')
        Imgback8 = ImageTk.PhotoImage(Imgback8)
        Imaback8r =  Label(self, image = Imgback8)
        Imaback8r.Image = Imgback8

        Imginfo = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\infobutton.png')
        Imginfo = ImageTk.PhotoImage(Imginfo)
        Imainfor =  Label(self, image = Imginfo)
        Imainfor.Image = Imginfo

        Imgaide = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\aidebutton.png')
        Imgaide = ImageTk.PhotoImage(Imgaide)
        Imaaider =  Label(self, image = Imgaide)
        Imaaider.Image = Imgaide

        self.Loginframe01 = Frame(self, width = 950, height = 520, bd = 0, bg='#FFFFFF', relief = 'flat')
        self.Loginframe01.grid(row = 0, column = 0)

        self.Loginframe0 = Frame(self.Loginframe01, width = 200, height = 200, bd = 0, bg='#FFFFFF', relief = 'flat')
        self.Loginframe0.place(rely = 0, relx = 0)


        self.btnreturn = Button(self.Loginframe0, image = ImgREp, bd = 0, bg='#FFFFFF', command = lambda: master.switch_frame(AnalyseWindow))
        self.btnreturn.place(x=0.20, y=0)



        self.Loginframe1 = Frame(self.Loginframe01, width = 300, height = 200, bd = 5, bg='#FFFFFF', relief = 'flat')
        self.Loginframe1.place(rely = 0, relx = 0.27)


        self.Loginframe310 = Frame(self.Loginframe01, width = 70, height = 60, bd = 0, bg='#FFFFFF', relief = 'flat')
        self.Loginframe310.place(rely = 0, relx = 0.89)

        self.btnreturnh = Button(self.Loginframe310, image = ImgREhome, bd = 0, bg='#FFFFFF', command = lambda: master.switch_frame(StartPage))
        self.btnreturnh.place(x=0, y=0)


        logo = Image.open('logo_cnrst_2018.png')
        logo = ImageTk.PhotoImage(logo)
        logo_label =  Label(self.Loginframe1, bd = 0, bg='#FFFFFF', image = logo)
        logo_label.Image = logo
        logo_label.grid(column=0, row=0)

        logo1 = Image.open('logo_fsdm.png')
        logo1 = ImageTk.PhotoImage(logo1)
        logo_label1 =  Label(self.Loginframe1, bd = 0, bg='#FFFFFF', image = logo1)
        logo_label1.Image = logo1
        logo_label1.grid(column=1, row=0)

        logo2 = Image.open('logo-ministère-santé-Maroc.jpg')
        logo2 = ImageTk.PhotoImage(logo2)
        logo_label2 =  Label(self.Loginframe1, bd = 0, bg='#FFFFFF', image = logo2)
        logo_label2.Image = logo2
        logo_label2.grid(column=2, row=0)

        self.LabelTitle = Label(self, image = ImgLabel, bg='#FFFFFF', bd = 0)
        self.LabelTitle.place(rely = 0.22, relx = 0.36)

        self.lbback7 = Label(self, image = Imgback7, bd = 0, bg='#FFFFFF',)
        self.lbback7.place(rely = 0.10, relx = 0)

        self.lbback8 = Label(self, image = Imgback8, bd = 0, bg='#FFFFFF',)
        self.lbback8.place(rely = 0.10, relx = 0.75)



        # name files
        self.files = ['Fes', 'Rabat', 'Meknes', 'Tanger', 'Casablanca', 'Kenitra', 'Eljadida', 'Tetoune', 'Oujda', 'Layoune', 'Dakhla']
#---------------------------------------------------------------------------------------------------------------------------------------
        date = StringVar()
        Susceptible = StringVar()
        Exposed = StringVar()
        Symptomatic = StringVar()
        Asymptomatic = StringVar()
        Hospitalized = StringVar()
        Quarantined = StringVar()
        Recovered = StringVar()
        Dead = StringVar()
        Vaccinated = StringVar()
        population = StringVar()

        conn = sqlite3.connect("dataCovid19sim.db")
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS Cityparametres(date TEXT,Susceptible TEXT,Exposed TEXT,Symptomatic TEXT,Asymptomatic TEXT,Hospitalized TEXT,Quarantined TEXT, Recovered TEXT, Dead TEXT,Vaccinated TEXT, population TEXT)')

        # create a combobox
        self.selected_files = tk.StringVar()


        self.Loginframe2 = Frame(self, width = 30, height = 50, bd = 20, bg = '#FFFFFF' ,relief = 'flat')
        self.Loginframe2.place(rely = 0.35, relx = 0.25)

        self.files_cb = ttk.Combobox(self.Loginframe2, width = 28, textvariable = self.selected_files)
        self.files_cb['values'] = self.files
        self.files_cb['state'] = 'normal'  # normal
        self.files_cb.grid(row = 15, column = 1)
        self.files_cb.current()
        self.files_cb.bind('<<ComboboxSelected>>')



        self.btnSoumettre = Button(self, image = ImgSubmit, bd = 0, bg = '#FFFFFF', command = lambda : Load_execl_data())
        self.btnSoumettre.place(rely = 0.36, relx = 0.53)




        self.Loginframe711 = Frame(self, width = 440, height = 220, bd = 20, bg='#d1e9d3', relief = 'ridge')
        self.Loginframe711.place(rely = 0.47, relx = 0.35)


        self.frame = LabelFrame(self.Loginframe711, bg = '#d1e9d3', fg ='#1b458f',  text="Les données")
        self.frame.place(height = 180, width = 400)


        tv1 = ttk.Treeview(self.frame)
        tv1.place(relheight = 1, relwidth = 1)

        treescrolly = Scrollbar(self.frame, orient = "vertical", command = tv1.yview)
        treescrollx = Scrollbar(self.frame, orient = "horizontal", command = tv1.xview)




        tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
        treescrollx.pack(side="bottom", fill="x")
        treescrolly.pack(side="right", fill="y")

        def Load_execl_data():
            file_path = f'C:\\Users\\pcc\\Desktop\\Covid19sim\\{self.files_cb.get()}.xlsx'
            try:
                excel_filename = r"{}".format(file_path)
                df = pd.read_excel(excel_filename)
            except ValueError:
                tk.messagebox.showerror("Information", "The file you have entered is invalid")
                return None
            except FileNotFoundError:
                tk.messagebox.showerror("Information", f"No such file as {self.files_cb.get()}")
                return None

            clear_data()
            tv1["columns"] = list(df.columns)
            tv1["show"] = "headings"
            for column in tv1["columns"]:
                tv1.heading(column, text=column)
            df_rows = df.to_numpy().tolist()

            for row in df_rows:
                tv1.insert("", "end", values=row)


        def clear_data():
            tv1.delete(*tv1.get_children())



        self.btnAdd = Button(self, image = ImgAdd,  bg='#FFFFFF', bd = 0, command = lambda: master.switch_frame(connectorDB))
        self.btnAdd.place(rely = 0.44, relx = 0.03)



        self.btnMap = Button(self, image = ImgMap , bd = 0, bg='#FFFFFF', command = lambda: master.switch_frame(Map))
        self.btnMap.place(rely = 0.66, relx = 0.03)



        self.btnGraph = Button(self, image = ImgGraph, bd = 0, bg = '#FFFFFF',  command = lambda: master.switch_frame(Graph))
        self.btnGraph.place(rely = 0.55, relx = 0.03)

        self.Loginframe4 = Frame(self, width = 950, height = 150, bg='#FFFFFF', bd = 20, relief = 'flat')
        self.Loginframe4.grid(row = 1, column = 0)

        self.btninfo = Button(self.Loginframe4, image =  Imginfo , bg = '#FFFFFF', bd = 0, command = self.info_window)
        self.btninfo.place(rely = 0, relx = 0.01)


        self.btnaide = Button(self.Loginframe4, image = Imgaide, bg = '#FFFFFF', bd = 0, command = self.aide_window)
        self.btnaide.place(rely = 0, relx = 0.71)

    def info_window(self):
        self.infoWindow = Toplevel(self.master)
        self.app = Info(self.infoWindow)



    def aide_window(self):
        self.aideWindow = Toplevel(self.master)
        self.app = Aide(self.aideWindow)




class regionalWindowP(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.title("Regional analyse")

        self.app_width = 900
        self.app_height = 615


        self.screen_width = self.master.winfo_screenwidth()
        self.screen_height = self.master.winfo_screenheight()

        x = (self.screen_width / 2) - (self.app_width / 2)
        y = (self.screen_height / 2) - (self.app_height /2)

        self.master.geometry(f'{self.app_width}x{self.app_height}+{int(x)}+{int(y)}')

        self.master.iconbitmap("logo.ico")
        self.config(bg = '#FFFFFF')

        ImgREhome = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\returnbuttonhome.png')
        ImgREhome = ImageTk.PhotoImage(ImgREhome)
        ImaREhomer =  Label(self, image = ImgREhome)
        ImaREhomer.Image = ImgREhome

        ImgREp = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\returnbutton.jpg')
        ImgREp = ImageTk.PhotoImage(ImgREp)
        ImaREpr =  Label(self, image = ImgREp)
        ImaREpr.Image = ImgREp

        ImgLabel = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\REGIONAL.png')
        ImgLabel = ImageTk.PhotoImage(ImgLabel)
        Imalabelr =  Label(self, image = ImgLabel)
        Imalabelr.Image = ImgLabel


        ImgSubmit = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\submitbutton.png')
        ImgSubmit = ImageTk.PhotoImage(ImgSubmit)
        ImaSubmitr =  Label(self, image = ImgSubmit)
        ImaSubmitr.Image = ImgSubmit


        ImgAdd = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\addcitybutton.png')
        ImgAdd = ImageTk.PhotoImage(ImgAdd)
        ImaAddr =  Label(self, image = ImgAdd)
        ImaAddr.Image = ImgAdd

        ImgMap = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\mapbutton.png')
        ImgMap = ImageTk.PhotoImage(ImgMap)
        ImaMapr =  Label(self, image = ImgMap)
        ImaMapr.Image = ImgMap

        ImgGraph = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\graphbutton.png')
        ImgGraph = ImageTk.PhotoImage(ImgGraph)
        ImaGraphr =  Label(self, image = ImgGraph)
        ImaGraphr.Image = ImgGraph


        Imgback7 = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\back7.jpg')
        Imgback7 = ImageTk.PhotoImage(Imgback7)
        Imaback7r =  Label(self, image = Imgback7)
        Imaback7r.Image = Imgback7

        Imgback8 = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\back8.jpg')
        Imgback8 = ImageTk.PhotoImage(Imgback8)
        Imaback8r =  Label(self, image = Imgback8)
        Imaback8r.Image = Imgback8

        Imginfo = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\infobutton.png')
        Imginfo = ImageTk.PhotoImage(Imginfo)
        Imainfor =  Label(self, image = Imginfo)
        Imainfor.Image = Imginfo

        Imgaide = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\aidebutton.png')
        Imgaide = ImageTk.PhotoImage(Imgaide)
        Imaaider =  Label(self, image = Imgaide)
        Imaaider.Image = Imgaide

        self.Loginframe01 = Frame(self, width = 950, height = 520, bd = 0, bg='#FFFFFF', relief = 'flat')
        self.Loginframe01.grid(row = 0, column = 0)

        self.Loginframe0 = Frame(self.Loginframe01, width = 200, height = 200, bd = 0, bg='#FFFFFF', relief = 'flat')
        self.Loginframe0.place(rely = 0, relx = 0)


        self.btnreturn = Button(self.Loginframe0, image = ImgREp, bd = 0, bg='#FFFFFF', command = lambda: master.switch_frame(AnalyseWindow))
        self.btnreturn.place(x=0.20, y=0)



        self.Loginframe1 = Frame(self.Loginframe01, width = 300, height = 200, bd = 5, bg='#FFFFFF', relief = 'flat')
        self.Loginframe1.place(rely = 0, relx = 0.27)


        self.Loginframe310 = Frame(self.Loginframe01, width = 70, height = 60, bd = 0, bg='#FFFFFF', relief = 'flat')
        self.Loginframe310.place(rely = 0, relx = 0.89)

        self.btnreturnh = Button(self.Loginframe310, image = ImgREhome, bd = 0, bg='#FFFFFF', command = lambda: master.switch_frame(StartPage))
        self.btnreturnh.place(x=0, y=0)


        logo = Image.open('logo_cnrst_2018.png')
        logo = ImageTk.PhotoImage(logo)
        logo_label =  Label(self.Loginframe1, bd = 0, bg='#FFFFFF', image = logo)
        logo_label.Image = logo
        logo_label.grid(column=0, row=0)

        logo1 = Image.open('logo_fsdm.png')
        logo1 = ImageTk.PhotoImage(logo1)
        logo_label1 =  Label(self.Loginframe1, bd = 0, bg='#FFFFFF', image = logo1)
        logo_label1.Image = logo1
        logo_label1.grid(column=1, row=0)

        logo2 = Image.open('logo-ministère-santé-Maroc.jpg')
        logo2 = ImageTk.PhotoImage(logo2)
        logo_label2 =  Label(self.Loginframe1, bd = 0, bg='#FFFFFF', image = logo2)
        logo_label2.Image = logo2
        logo_label2.grid(column=2, row=0)

        self.LabelTitle = Label(self, image = ImgLabel, bg='#FFFFFF', bd = 0)
        self.LabelTitle.place(rely = 0.22, relx = 0.34)

        self.lbback7 = Label(self, image = Imgback7, bd = 0, bg='#FFFFFF',)
        self.lbback7.place(rely = 0.10, relx = 0)

        self.lbback8 = Label(self, image = Imgback8, bd = 0, bg='#FFFFFF',)
        self.lbback8.place(rely = 0.10, relx = 0.75)



        # name files
        self.files = ['Fes', 'Rabat', 'Meknes', 'Tanger', 'Casablanca', 'Kenitra', 'Eljadida', 'Tetoune', 'Oujda', 'Layoune', 'Dakhla']
#---------------------------------------------------------------------------------------------------------------------------------------
        date = StringVar()
        Susceptible = StringVar()
        Exposed = StringVar()
        Symptomatic = StringVar()
        Asymptomatic = StringVar()
        Hospitalized = StringVar()
        Quarantined = StringVar()
        Recovered = StringVar()
        Dead = StringVar()
        Vaccinated = StringVar()
        population = StringVar()

        conn = sqlite3.connect("dataCovid19sim.db")
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS Cityparametres(date TEXT,Susceptible TEXT,Exposed TEXT,Symptomatic TEXT,Asymptomatic TEXT,Hospitalized TEXT,Quarantined TEXT, Recovered TEXT, Dead TEXT,Vaccinated TEXT, population TEXT)')

        # create a combobox
        self.selected_files = tk.StringVar()


        self.Loginframe2 = Frame(self, width = 30, height = 50, bd = 20, bg = '#FFFFFF' ,relief = 'flat')
        self.Loginframe2.place(rely = 0.35, relx = 0.25)

        self.files_cb = ttk.Combobox(self.Loginframe2, width = 28, textvariable = self.selected_files)
        self.files_cb['values'] = self.files
        self.files_cb['state'] = 'normal'  # normal
        self.files_cb.grid(row = 15, column = 1)
        self.files_cb.current()
        self.files_cb.bind('<<ComboboxSelected>>')



        self.btnSoumettre = Button(self, image = ImgSubmit, bd = 0, bg = '#FFFFFF', command = lambda : Load_execl_data())
        self.btnSoumettre.place(rely = 0.36, relx = 0.53)




        self.Loginframe711 = Frame(self, width = 440, height = 220, bd = 20, bg='#d1e9d3', relief = 'ridge')
        self.Loginframe711.place(rely = 0.47, relx = 0.35)


        self.frame = LabelFrame(self.Loginframe711, bg = '#d1e9d3', fg ='#1b458f',  text="Les données")
        self.frame.place(height = 180, width = 400)


        tv1 = ttk.Treeview(self.frame)
        tv1.place(relheight = 1, relwidth = 1)

        treescrolly = Scrollbar(self.frame, orient = "vertical", command = tv1.yview)
        treescrollx = Scrollbar(self.frame, orient = "horizontal", command = tv1.xview)




        tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
        treescrollx.pack(side="bottom", fill="x")
        treescrolly.pack(side="right", fill="y")

        def Load_execl_data():
            file_path = f'C:\\Users\\pcc\\Desktop\\Covid19sim\\{self.files_cb.get()}.xlsx'
            try:
                excel_filename = r"{}".format(file_path)
                df = pd.read_excel(excel_filename)
            except ValueError:
                tk.messagebox.showerror("Information", "The file you have entered is invalid")
                return None
            except FileNotFoundError:
                tk.messagebox.showerror("Information", f"No such file as {self.files_cb.get()}")
                return None

            clear_data()
            tv1["columns"] = list(df.columns)
            tv1["show"] = "headings"
            for column in tv1["columns"]:
                tv1.heading(column, text=column)
            df_rows = df.to_numpy().tolist()

            for row in df_rows:
                tv1.insert("", "end", values=row)


        def clear_data():
            tv1.delete(*tv1.get_children())



        self.btnAdd = Button(self, image = ImgAdd,  bg='#FFFFFF', bd = 0, command = lambda: master.switch_frame(connectorDB))
        self.btnAdd.place(rely = 0.44, relx = 0.03)



        self.btnMap = Button(self, image = ImgMap , bd = 0, bg='#FFFFFF', command = lambda: master.switch_frame(Map))
        self.btnMap.place(rely = 0.66, relx = 0.03)



        self.btnGraph = Button(self, image = ImgGraph, bd = 0, bg = '#FFFFFF',  command = lambda: master.switch_frame(Graph))
        self.btnGraph.place(rely = 0.55, relx = 0.03)

        self.Loginframe4 = Frame(self, width = 950, height = 150, bg='#FFFFFF', bd = 20, relief = 'flat')
        self.Loginframe4.grid(row = 1, column = 0)

        self.btninfo = Button(self.Loginframe4, image =  Imginfo , bg = '#FFFFFF', bd = 0, command = self.info_window)
        self.btninfo.place(rely = 0, relx = 0.01)


        self.btnaide = Button(self.Loginframe4, image = Imgaide, bg = '#FFFFFF', bd = 0, command = self.aide_window)
        self.btnaide.place(rely = 0, relx = 0.71)

    def info_window(self):
        self.infoWindow = Toplevel(self.master)
        self.app = Info(self.infoWindow)



    def aide_window(self):
        self.aideWindow = Toplevel(self.master)
        self.app = Aide(self.aideWindow)

class nationalWindowP(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.title("Regional analyse")

        self.app_width = 900
        self.app_height = 615


        self.screen_width = self.master.winfo_screenwidth()
        self.screen_height = self.master.winfo_screenheight()

        x = (self.screen_width / 2) - (self.app_width / 2)
        y = (self.screen_height / 2) - (self.app_height /2)

        self.master.geometry(f'{self.app_width}x{self.app_height}+{int(x)}+{int(y)}')

        self.master.iconbitmap("logo.ico")
        self.config(bg = '#FFFFFF')

        ImgREhome = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\returnbuttonhome.png')
        ImgREhome = ImageTk.PhotoImage(ImgREhome)
        ImaREhomer =  Label(self, image = ImgREhome)
        ImaREhomer.Image = ImgREhome

        ImgREp = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\returnbutton.jpg')
        ImgREp = ImageTk.PhotoImage(ImgREp)
        ImaREpr =  Label(self, image = ImgREp)
        ImaREpr.Image = ImgREp

        ImgLabel = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\NATIONAL.png')
        ImgLabel = ImageTk.PhotoImage(ImgLabel)
        Imalabelr =  Label(self, image = ImgLabel)
        Imalabelr.Image = ImgLabel


        ImgSubmit = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\submitbutton.png')
        ImgSubmit = ImageTk.PhotoImage(ImgSubmit)
        ImaSubmitr =  Label(self, image = ImgSubmit)
        ImaSubmitr.Image = ImgSubmit


        ImgAdd = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\addcitybutton.png')
        ImgAdd = ImageTk.PhotoImage(ImgAdd)
        ImaAddr =  Label(self, image = ImgAdd)
        ImaAddr.Image = ImgAdd

        ImgMap = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\mapbutton.png')
        ImgMap = ImageTk.PhotoImage(ImgMap)
        ImaMapr =  Label(self, image = ImgMap)
        ImaMapr.Image = ImgMap

        ImgGraph = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\graphbutton.png')
        ImgGraph = ImageTk.PhotoImage(ImgGraph)
        ImaGraphr =  Label(self, image = ImgGraph)
        ImaGraphr.Image = ImgGraph


        Imgback7 = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\back7.jpg')
        Imgback7 = ImageTk.PhotoImage(Imgback7)
        Imaback7r =  Label(self, image = Imgback7)
        Imaback7r.Image = Imgback7

        Imgback8 = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\back8.jpg')
        Imgback8 = ImageTk.PhotoImage(Imgback8)
        Imaback8r =  Label(self, image = Imgback8)
        Imaback8r.Image = Imgback8

        Imginfo = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\infobutton.png')
        Imginfo = ImageTk.PhotoImage(Imginfo)
        Imainfor =  Label(self, image = Imginfo)
        Imainfor.Image = Imginfo

        Imgaide = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\aidebutton.png')
        Imgaide = ImageTk.PhotoImage(Imgaide)
        Imaaider =  Label(self, image = Imgaide)
        Imaaider.Image = Imgaide

        self.Loginframe01 = Frame(self, width = 950, height = 520, bd = 0, bg='#FFFFFF', relief = 'flat')
        self.Loginframe01.grid(row = 0, column = 0)

        self.Loginframe0 = Frame(self.Loginframe01, width = 200, height = 200, bd = 0, bg='#FFFFFF', relief = 'flat')
        self.Loginframe0.place(rely = 0, relx = 0)


        self.btnreturn = Button(self.Loginframe0, image = ImgREp, bd = 0, bg='#FFFFFF', command = lambda: master.switch_frame(AnalyseWindow))
        self.btnreturn.place(x=0.20, y=0)



        self.Loginframe1 = Frame(self.Loginframe01, width = 300, height = 200, bd = 5, bg='#FFFFFF', relief = 'flat')
        self.Loginframe1.place(rely = 0, relx = 0.27)


        self.Loginframe310 = Frame(self.Loginframe01, width = 70, height = 60, bd = 0, bg='#FFFFFF', relief = 'flat')
        self.Loginframe310.place(rely = 0, relx = 0.89)

        self.btnreturnh = Button(self.Loginframe310, image = ImgREhome, bd = 0, bg='#FFFFFF', command = lambda: master.switch_frame(StartPage))
        self.btnreturnh.place(x=0, y=0)


        logo = Image.open('logo_cnrst_2018.png')
        logo = ImageTk.PhotoImage(logo)
        logo_label =  Label(self.Loginframe1, bd = 0, bg='#FFFFFF', image = logo)
        logo_label.Image = logo
        logo_label.grid(column=0, row=0)

        logo1 = Image.open('logo_fsdm.png')
        logo1 = ImageTk.PhotoImage(logo1)
        logo_label1 =  Label(self.Loginframe1, bd = 0, bg='#FFFFFF', image = logo1)
        logo_label1.Image = logo1
        logo_label1.grid(column=1, row=0)

        logo2 = Image.open('logo-ministère-santé-Maroc.jpg')
        logo2 = ImageTk.PhotoImage(logo2)
        logo_label2 =  Label(self.Loginframe1, bd = 0, bg='#FFFFFF', image = logo2)
        logo_label2.Image = logo2
        logo_label2.grid(column=2, row=0)

        self.LabelTitle = Label(self, image = ImgLabel, bg='#FFFFFF', bd = 0)
        self.LabelTitle.place(rely = 0.22, relx = 0.34)

        self.lbback7 = Label(self, image = Imgback7, bd = 0, bg='#FFFFFF',)
        self.lbback7.place(rely = 0.10, relx = 0)

        self.lbback8 = Label(self, image = Imgback8, bd = 0, bg='#FFFFFF',)
        self.lbback8.place(rely = 0.10, relx = 0.75)



        # name files
        self.files = ['Fes', 'Rabat', 'Meknes', 'Tanger', 'Casablanca', 'Kenitra', 'Eljadida', 'Tetoune', 'Oujda', 'Layoune', 'Dakhla']
#---------------------------------------------------------------------------------------------------------------------------------------
        date = StringVar()
        Susceptible = StringVar()
        Exposed = StringVar()
        Symptomatic = StringVar()
        Asymptomatic = StringVar()
        Hospitalized = StringVar()
        Quarantined = StringVar()
        Recovered = StringVar()
        Dead = StringVar()
        Vaccinated = StringVar()
        population = StringVar()

        conn = sqlite3.connect("dataCovid19sim.db")
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS Cityparametres(date TEXT,Susceptible TEXT,Exposed TEXT,Symptomatic TEXT,Asymptomatic TEXT,Hospitalized TEXT,Quarantined TEXT, Recovered TEXT, Dead TEXT,Vaccinated TEXT, population TEXT)')

        # create a combobox
        self.selected_files = tk.StringVar()


        self.Loginframe2 = Frame(self, width = 30, height = 50, bd = 20, bg = '#FFFFFF' ,relief = 'flat')
        self.Loginframe2.place(rely = 0.35, relx = 0.25)

        self.files_cb = ttk.Combobox(self.Loginframe2, width = 28, textvariable = self.selected_files)
        self.files_cb['values'] = self.files
        self.files_cb['state'] = 'normal'  # normal
        self.files_cb.grid(row = 15, column = 1)
        self.files_cb.current()
        self.files_cb.bind('<<ComboboxSelected>>')



        self.btnSoumettre = Button(self, image = ImgSubmit, bd = 0, bg = '#FFFFFF', command = lambda : Load_execl_data())
        self.btnSoumettre.place(rely = 0.36, relx = 0.53)




        self.Loginframe711 = Frame(self, width = 440, height = 220, bd = 20, bg='#d1e9d3', relief = 'ridge')
        self.Loginframe711.place(rely = 0.47, relx = 0.35)


        self.frame = LabelFrame(self.Loginframe711, bg = '#d1e9d3', fg ='#1b458f',  text="Les données")
        self.frame.place(height = 180, width = 400)


        tv1 = ttk.Treeview(self.frame)
        tv1.place(relheight = 1, relwidth = 1)

        treescrolly = Scrollbar(self.frame, orient = "vertical", command = tv1.yview)
        treescrollx = Scrollbar(self.frame, orient = "horizontal", command = tv1.xview)




        tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
        treescrollx.pack(side="bottom", fill="x")
        treescrolly.pack(side="right", fill="y")

        def Load_execl_data():
            file_path = f'C:\\Users\\pcc\\Desktop\\Covid19sim\\{self.files_cb.get()}.xlsx'
            try:
                excel_filename = r"{}".format(file_path)
                df = pd.read_excel(excel_filename)
            except ValueError:
                tk.messagebox.showerror("Information", "The file you have entered is invalid")
                return None
            except FileNotFoundError:
                tk.messagebox.showerror("Information", f"No such file as {self.files_cb.get()}")
                return None

            clear_data()
            tv1["columns"] = list(df.columns)
            tv1["show"] = "headings"
            for column in tv1["columns"]:
                tv1.heading(column, text=column)
            df_rows = df.to_numpy().tolist()

            for row in df_rows:
                tv1.insert("", "end", values=row)


        def clear_data():
            tv1.delete(*tv1.get_children())



        self.btnAdd = Button(self, image = ImgAdd,  bg='#FFFFFF', bd = 0, command = lambda: master.switch_frame(connectorDB))
        self.btnAdd.place(rely = 0.44, relx = 0.03)



        self.btnMap = Button(self, image = ImgMap , bd = 0, bg='#FFFFFF', command = lambda: master.switch_frame(Map))
        self.btnMap.place(rely = 0.66, relx = 0.03)



        self.btnGraph = Button(self, image = ImgGraph, bd = 0, bg = '#FFFFFF',  command = lambda: master.switch_frame(Graph))
        self.btnGraph.place(rely = 0.55, relx = 0.03)

        self.Loginframe4 = Frame(self, width = 950, height = 150, bg='#FFFFFF', bd = 20, relief = 'flat')
        self.Loginframe4.grid(row = 1, column = 0)

        self.btninfo = Button(self.Loginframe4, image =  Imginfo , bg = '#FFFFFF', bd = 0, command = self.info_window)
        self.btninfo.place(rely = 0, relx = 0.01)


        self.btnaide = Button(self.Loginframe4, image = Imgaide, bg = '#FFFFFF', bd = 0, command = self.aide_window)
        self.btnaide.place(rely = 0, relx = 0.71)

    def info_window(self):
        self.infoWindow = Toplevel(self.master)
        self.app = Info(self.infoWindow)



    def aide_window(self):
        self.aideWindow = Toplevel(self.master)
        self.app = Aide(self.aideWindow)

class Map(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.title("Map")

        self.app_width = 800
        self.app_height = 615


        self.screen_width = self.master.winfo_screenwidth()
        self.screen_height = self.master.winfo_screenheight()

        x = (self.screen_width / 2) - (self.app_width / 2)
        y = (self.screen_height / 2) - (self.app_height /2)

        self.master.geometry(f'{self.app_width}x{self.app_height}+{int(x)}+{int(y)}')

        self.master.iconbitmap("logo.ico")
        self.config(bg = '#FFFFFF')


        self.Loginframe1 = Frame(self, width = 500, height = 60, bd = 20,  bg='#FFFFFF', relief = 'flat')
        self.Loginframe1.grid(row = 1, column = 0)

        logo = Image.open('logo_cnrst_2018.png')
        logo = ImageTk.PhotoImage(logo)
        logo_label =  Label(self.Loginframe1, bd = 0, bg='#FFFFFF', image = logo)
        logo_label.Image = logo
        logo_label.grid(column=0, row=0)

        logo1 = Image.open('logo_fsdm.png')
        logo1 = ImageTk.PhotoImage(logo1)
        logo_label1 =  Label(self.Loginframe1, bd = 0, bg='#FFFFFF', image = logo1)
        logo_label1.Image = logo1
        logo_label1.grid(column=1, row=0)

        logo2 = Image.open('logo-ministère-santé-Maroc.jpg')
        logo2 = ImageTk.PhotoImage(logo2)
        logo_label2 =  Label(self.Loginframe1, bd = 0, bg='#FFFFFF', image = logo2)
        logo_label2.Image = logo2
        logo_label2.grid(column=2, row=0)


        self.Loginframe1222 = Frame(self, width = 500, height = 200, bd = 20,  bg='#FFFFFF', relief = 'flat')
        self.Loginframe1222.grid(row = 2, column = 0, columnspan = 2, pady = 40)

        self.LabelTitle = Label(self.Loginframe1222, text = "Maps", font=('Verdana', 30, 'bold'),  bg='#FFFFFF', bd = 20)
        self.LabelTitle.grid(row = 0, column = 0)

        self.Loginframe1333 = Frame(self, width = 500, height = 100, bd = 20,  bg='#FFFFFF', relief = 'flat')
        self.Loginframe1333.grid(row = 3, column = 0)

        self.Loginframe1444 = Frame(self, width = 500, height = 100, bd = 20,  bg='#FFFFFF', relief = 'ridge')
        self.Loginframe1444.grid(row = 4, column = 0)

        self.btnreturn = Button(self.Loginframe1444, text = "Retour", width = 20, height = 1, command = lambda: master.switch_frame(localWindowA))
        self.btnreturn.grid(row = 0, column = 0)




        webbrowser.open('https://wego.here.com/?map=34.03313,-5.00028,4,normal')







class Graph(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.title("Graph")

        self.app_width = 900
        self.app_height = 615


        self.screen_width = self.master.winfo_screenwidth()
        self.screen_height = self.master.winfo_screenheight()

        x = (self.screen_width / 2) - (self.app_width / 2)
        y = (self.screen_height / 2) - (self.app_height /2)

        self.master.geometry(f'{self.app_width}x{self.app_height}+{int(x)}+{int(y)}')

        self.master.iconbitmap("logo.ico")
        self.config(bg = '#FFFFFF')

        ImgREhome = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\returnbuttonhome.png')
        ImgREhome = ImageTk.PhotoImage(ImgREhome)
        ImaREhomer =  Label(self, image = ImgREhome)
        ImaREhomer.Image = ImgREhome

        ImgREp = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\returnbutton.jpg')
        ImgREp = ImageTk.PhotoImage(ImgREp)
        ImaREpr =  Label(self, image = ImgREp)
        ImaREpr.Image = ImgREp

        ImgLabel = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\GRAPH.png')
        ImgLabel = ImageTk.PhotoImage(ImgLabel)
        Imalabelr =  Label(self, image = ImgLabel)
        Imalabelr.Image = ImgLabel

        Imgs = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\sbutton.png')
        Imgs = ImageTk.PhotoImage(Imgs)
        Imasr =  Label(self, image = Imgs)
        Imasr.Image = Imgs


        Imge = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\ebutton.png')
        Imge = ImageTk.PhotoImage(Imge)
        Imaer =  Label(self, image = Imge)
        Imaer.Image = Imge

        Imgy = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\ybutton.png')
        Imgy = ImageTk.PhotoImage(Imgy)
        Imayr =  Label(self, image = Imgy)
        Imayr.Image = Imgy


        Imgh = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\hbutton.png')
        Imgh = ImageTk.PhotoImage(Imgh)
        Imahr =  Label(self, image = Imgh)
        Imahr.Image = Imgh

        Imgq = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\qbutton.png')
        Imgq = ImageTk.PhotoImage(Imgq)
        Imaqr =  Label(self, image = Imgq)
        Imaqr.Image = Imgq

        Imgr = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\rbutton.png')
        Imgr = ImageTk.PhotoImage(Imgr)
        Imarr =  Label(self, image = Imgr)
        Imarr.Image = Imgr

        Imgd = Image.open('dbutton.png')
        Imgd = ImageTk.PhotoImage(Imgd)
        Imadr =  Label(self, image = Imgd)
        Imadr.Image = Imgd

        Imgv = Image.open('vbutton.png')
        Imgv = ImageTk.PhotoImage(Imgv)
        Imavr =  Label(self, image = Imgv)
        Imavr.Image = Imgv

        Imgn = Image.open('nbutton.png')
        Imgn = ImageTk.PhotoImage(Imgn)
        Imanr =  Label(self, image = Imgn)
        Imanr.Image = Imgn

        Imga = Image.open('abutton.png')
        Imga = ImageTk.PhotoImage(Imga)
        Imaar =  Label(self, image = Imga)
        Imaar.Image = Imga


        Imginfo = Image.open('infobutton.png')
        Imginfo = ImageTk.PhotoImage(Imginfo)
        Imainfor =  Label(self, image = Imginfo)
        Imainfor.Image = Imginfo

        Imgaide = Image.open('aidebutton.png')
        Imgaide = ImageTk.PhotoImage(Imgaide)
        Imaaider =  Label(self, image = Imgaide)
        Imaaider.Image = Imgaide

        Imgback9 = Image.open('back9.jpg')
        Imgback9 = ImageTk.PhotoImage(Imgback9)
        Imaback9r =  Label(self, image = Imgback9)
        Imaback9r.Image = Imgback9

        Imgback10 = Image.open('back10.jpg')
        Imgback10 = ImageTk.PhotoImage(Imgback10)
        Imaback10r =  Label(self, image = Imgback10)
        Imaback10r.Image = Imgback10


        ImgTime = Image.open('timebutton.png')
        ImgTime = ImageTk.PhotoImage(ImgTime)
        ImaTimer =  Label(self, image = ImgTime)
        ImaTimer.Image = ImgTime




        self.Loginframe01 = Frame(self, width = 950, height = 550, bd = 0, bg='#FFFFFF', relief = 'flat')
        self.Loginframe01.grid(row = 0, column = 0)

        self.Loginframe0 = Frame(self.Loginframe01, width = 200, height = 200, bd = 0, bg='#FFFFFF', relief = 'flat')
        self.Loginframe0.place(rely = 0, relx = 0)


        self.btnreturn = Button(self.Loginframe0, image = ImgREp, bd = 0, bg='#FFFFFF', command = lambda: master.switch_frame(localWindowA))
        self.btnreturn.place(x=0.20, y=0)



        self.Loginframe1 = Frame(self.Loginframe01, width = 300, height = 200, bd = 5, bg='#FFFFFF', relief = 'flat')
        self.Loginframe1.place(rely = 0, relx = 0.27)


        self.Loginframe310 = Frame(self.Loginframe01, width = 70, height = 60, bd = 0, bg='#FFFFFF', relief = 'flat')
        self.Loginframe310.place(rely = 0, relx = 0.89)

        self.btnreturnh = Button(self.Loginframe310, image = ImgREhome, bd = 0, bg='#FFFFFF', command = lambda: master.switch_frame(StartPage))
        self.btnreturnh.place(x=0, y=0)



        logo = Image.open('logo_cnrst_2018.png')
        logo = ImageTk.PhotoImage(logo)
        logo_label =  Label(self.Loginframe1, bd = 0, bg='#FFFFFF', image = logo)
        logo_label.Image = logo
        logo_label.grid(column=0, row=0)

        logo1 = Image.open('logo_fsdm.png')
        logo1 = ImageTk.PhotoImage(logo1)
        logo_label1 =  Label(self.Loginframe1, bd = 0, bg='#FFFFFF', image = logo1)
        logo_label1.Image = logo1
        logo_label1.grid(column=1, row=0)

        logo2 = Image.open('logo-ministère-santé-Maroc.jpg')
        logo2 = ImageTk.PhotoImage(logo2)
        logo_label2 =  Label(self.Loginframe1, bd = 0, bg='#FFFFFF', image = logo2)
        logo_label2.Image = logo2
        logo_label2.grid(column=2, row=0)


        self.LabelTitle = Label(self, image = ImgLabel,  bg='#FFFFFF', bd = 0)
        self.LabelTitle.place(rely = 0.24, relx = 0.37)

        self.lbback9 = Label(self, image = Imgback9, bd = 0, bg='#FFFFFF')
        self.lbback9.place(rely = 0.10, relx = 0)

        self.lbback10 = Label(self, image = Imgback10, bd = 0, bg='#FFFFFF')
        self.lbback10.place(rely = 0.10, relx = 0.75)
        self.Dated = StringVar()
        self.Datef = StringVar()
        self.Days = StringVar()

        self.lblDated = Label(self, text = 'Date depart :', font=('arial', 8, 'bold'), bd = 5, bg= '#FFFFFF', fg = 'black')
        self.lblDated.place(rely = 0.37, relx = 0)
        self.txtDated = DateEntry(self, width = 15, bg = '#D1E9D3', fg = 'black', borderwidth = 4, date_pattern = 'dd/mm/yy', textvariable= self.Dated, year = 2021)
        self.txtDated.place(rely = 0.38, relx = 0.10)


        self.lblDatef = Label(self, text = 'Date final :', font=('arial', 8, 'bold'), bd = 5, bg= '#FFFFFF', fg = 'black')
        self.lblDatef.place(rely = 0.37, relx = 0.25)
        self.txtDatef = DateEntry(self, width = 15, bg = '#D1E9D3', fg = 'black', borderwidth = 4, year = 2021, date_pattern = 'dd/mm/yy', textvariable= self.Datef)
        self.txtDatef.place(rely = 0.38, relx = 0.33)

        self.lblT = Label(self, text = 'T :', font=('arial', 8, 'bold'), bd = 5, bg= '#FFFFFF', fg = 'black')
        self.lblT.place(rely = 0.37, relx = 0.48)
        self.txtT = Entry(self, width = 18, bg = '#D1E9D3', fg = 'black', textvariable= self.Days)
        self.txtT.place(rely = 0.38, relx = 0.52)
        self.btnT = Button(self, image = ImgTime, bd = 0, bg = '#FFFFFF', command = self.calculetday)
        self.btnT.place(rely = 0.34, relx = 0.65)





        self.lblSusceptible = Label(self, text = 'Les personnes susptibles :', font=('arial', 8, 'bold'), bd = 5, bg= '#FFFFFF', fg = 'black')
        self.lblSusceptible.place(rely = 0.47, relx = 0.15)
        self.btnSusceptible = Button(self, image = Imgs, bd = 0, bg = '#FFFFFF', command = self.Susceptible_window)
        self.btnSusceptible.place(rely = 0.45, relx = 0.40)

        self.lblExposed = Label(self, text = 'Les personnes exposees :', font=('arial', 8, 'bold'), bd = 3, bg= '#FFFFFF', fg = 'black')
        self.lblExposed.place(rely = 0.47, relx = 0.50)
        self.btnExposed = Button(self, image = Imge, bg = '#FFFFFF', bd = 0, command = self.Exposed_window)
        self.btnExposed.place(rely = 0.45, relx = 0.75)


        self.lblSymptomatic = Label(self, text = 'Les personnes symptomatiques :', font=('arial', 8, 'bold'), bd = 5, bg= '#FFFFFF', fg = 'black')
        self.lblSymptomatic.place(rely = 0.56, relx = 0.15)
        self.btnSymptomatic = Button(self, image = Imgy, bd = 0, bg='#FFFFFF', command = self.Symptomatic_window)
        self.btnSymptomatic.place(rely = 0.54, relx = 0.40)


        self.lblAsymptomatic = Label(self, text = 'Les personnes asymptotiques :', font=('arial', 8, 'bold'), bd = 5, bg= '#FFFFFF', fg = 'black')
        self.lblAsymptomatic.place(rely = 0.56, relx = 0.50)
        self.btnAsymptomatic = Button(self, image = Imga, bd = 0, bg ='#FFFFFF', command = self.Asymptomatic_window)
        self.btnAsymptomatic.place(rely = 0.54, relx = 0.75)


        self.lblHospitalized = Label(self, text = 'Les personnes hospitalisees :', font=('arial', 8, 'bold'), bd = 5, bg= '#FFFFFF', fg = 'black')
        self.lblHospitalized.place(rely = 0.65, relx = 0.15)
        self.btnHospitalized = Button(self, image = Imgh, bd = 0, bg = '#FFFFFF', command = self.Hospitalized_window)
        self.btnHospitalized.place(rely = 0.63, relx = 0.40)

        self.lblQuarantined = Label(self, text = 'Les personnes mises en quarantine :', font=('arial', 8, 'bold'), bd = 5, bg= '#FFFFFF', fg = 'black')
        self.lblQuarantined.place(rely = 0.65, relx = 0.50)
        self.btnQuarantined = Button(self, image = Imgq, bd = 0, bg = '#FFFFFF', command = self.Quarantined_window)
        self.btnQuarantined.place(rely = 0.63, relx = 0.75)


        self.lblRecovered = Label(self,text = 'Les personnes recuperees :', font=('arial', 8, 'bold'), bd = 5, bg= '#FFFFFF', fg = 'black')
        self.lblRecovered.place(rely = 0.74, relx = 0.15)
        self.btnRecovered = Button(self, image = Imgr, bd = 0, bg = '#FFFFFF', command = self.Recovered_window)
        self.btnRecovered.place(rely = 0.72, relx = 0.40)


        self.lblDead = Label(self,text = 'Les personnes mortes :', font=('arial', 8, 'bold'), bd = 5, bg= '#FFFFFF', fg = 'black')
        self.lblDead.place(rely = 0.74, relx = 0.50)
        self.btnDead = Button(self, image = Imgd, bd = 0, bg = '#FFFFFF', command = self.Dead_window)
        self.btnDead.place(rely = 0.72, relx = 0.75)


        self.lblVaccinated = Label(self,text = 'Les personnes vaccinees :', font=('arial', 8, 'bold'), bd = 5,  bg= '#FFFFFF', fg = 'black')
        self.lblVaccinated.place(rely = 0.83, relx = 0.15)
        self.btnVaccinated = Button(self, image = Imgv, bd = 0, bg = '#FFFFFF', command = self.Vaccinated_window)
        self.btnVaccinated.place(rely = 0.81, relx = 0.40)


        self.lblPopulation = Label(self,text = 'La taille de la population :', font=('arial', 8, 'bold'), bd = 5, bg= '#FFFFFF', fg = 'black')
        self.lblPopulation.place(rely = 0.83, relx = 0.50)
        self.btnPopulation = Button(self, image = Imgn, bd = 0, bg  = '#FFFFFF', command = self.Population_window)
        self.btnPopulation.place(rely = 0.81, relx = 0.75)

        self.Loginframe4 = Frame(self, width = 950, height = 200, bg='#FFFFFF', bd = 20, relief = 'flat')
        self.Loginframe4.grid(row = 1, column = 0)

        self.btninfo = Button(self.Loginframe4, image =  Imginfo , bg = '#FFFFFF', bd = 0, command = self.info_window)
        self.btninfo.place(rely = -0.12, relx = 0.01)



        self.btnaide = Button(self.Loginframe4, image = Imgaide, bg = '#FFFFFF', bd = 0, command = self.aide_window)
        self.btnaide.place(rely = -0.12, relx = 0.71)

    def Susceptible_window(self):
        self.x = np.linspace(start=0,stop=int(self.Days.get()),num=6)
        self.y = np.cos(self.x)
        plt.scatter(self.x, self.y)
        plt.errorbar(self.x,self.y, linestyle="None",color='black')
        plt.xlabel('$(temps (t))$',fontsize=12)
        plt.ylabel('$(S(t))$',fontsize=12)
        plt.show()


    def Exposed_window(self):
        self.x = np.linspace(start=0,stop=int(self.Days.get()),num=6)
        self.y = np.cos(self.x)
        plt.scatter(self.x, self.y)
        plt.errorbar(self.x,self.y, linestyle="None",color='black')
        plt.xlabel('$(temps (t))$',fontsize=12)
        plt.ylabel('$(E(t))$',fontsize=12)
        plt.show()

    def Symptomatic_window(self):
        self.x = np.linspace(start=0,stop=int(self.Days.get()),num=6)
        self.y = np.cos(self.x)
        plt.scatter(self.x, self.y)
        plt.errorbar(self.x,self.y, linestyle="None",color='black')
        plt.xlabel('$(temps (t))$',fontsize=12)
        plt.ylabel('$(Y(t))$',fontsize=12)
        plt.show()

    def Asymptomatic_window(self):
        self.x = np.linspace(start=0,stop=int(self.Days.get()),num=6)
        self.y = np.cos(self.x)
        plt.scatter(self.x, self.y)
        plt.errorbar(self.x,self.y, linestyle="None",color='black')
        plt.xlabel('$(temps (t))$',fontsize=12)
        plt.ylabel('$(A(t))$',fontsize=12)
        plt.show()


    def Hospitalized_window(self):
        self.x = np.linspace(start=0,stop=int(self.Days.get()),num=6)
        self.y = np.cos(self.x)
        plt.scatter(self.x, self.y)
        plt.errorbar(self.x,self.y, linestyle="None",color='black')
        plt.xlabel('$(temps (t))$',fontsize=12)
        plt.ylabel('$(H(t))$',fontsize=12)
        plt.show()

    def Quarantined_window(self):
        self.x = np.linspace(start=0,stop=int(self.Days.get()),num=6)
        self.y = np.cos(self.x)
        plt.scatter(self.x, self.y)
        plt.errorbar(self.x,self.y, linestyle="None",color='black')
        plt.xlabel('$(temps (t))$',fontsize=12)
        plt.ylabel('$(Q(t))$',fontsize=12)
        plt.show()


    def Recovered_window(self):
        self.x = np.linspace(start=0,stop=int(self.Days.get()),num=6)
        self.y = np.cos(self.x)
        plt.scatter(self.x, self.y)
        plt.errorbar(self.x,self.y, linestyle="None",color='black')
        plt.xlabel('$(temps (t))$',fontsize=12)
        plt.ylabel('$(R(t))$',fontsize=12)
        plt.show()


    def Dead_window(self):
        self.x = np.linspace(start=0,stop=int(self.Days.get()),num=6)
        self.y = np.cos(self.x)
        plt.scatter(self.x, self.y)
        plt.errorbar(self.x,self.y, linestyle="None",color='black')
        plt.xlabel('$(temps (t))$',fontsize=12)
        plt.ylabel('$(D(t))$',fontsize=12)
        plt.show()


    def Vaccinated_window(self):
        self.x = np.linspace(start=0,stop=int(self.Days.get()),num=6)
        self.y = np.cos(self.x)
        plt.scatter(self.x, self.y)
        plt.errorbar(self.x,self.y, linestyle="None",color='black')
        plt.xlabel('$(temps (t))$',fontsize=12)
        plt.ylabel('$(V(t))$',fontsize=12)
        plt.show()


    def Population_window(self):
        self.x = np.linspace(start=0,stop=int(self.Days.get()),num=6)
        self.y = np.cos(self.x)
        plt.scatter(self.x, self.y)
        plt.errorbar(self.x,self.y, linestyle="None",color='black')
        plt.xlabel('$(temps (t))$',fontsize=12)
        plt.ylabel('$(N(t))$',fontsize=12)
        plt.show()


    def info_window(self):
        self.infoWindow = Toplevel(self.master)
        self.app = Info(self.infoWindow)



    def aide_window(self):
        self.aideWindow = Toplevel(self.master)
        self.app = Aide(self.aideWindow)

    def calculetday(self):
        self.dateDepart = (self.txtDated.get_date())
        self.dateFinal = (self.txtDatef.get_date())
        self.day = (abs ((self.dateDepart - self.dateFinal).days))
        self.Days.set(str(self.day))


class connectorDB(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.title("Database")

        self.app_width = 900
        self.app_height = 615


        self.screen_width = self.master.winfo_screenwidth()
        self.screen_height = self.master.winfo_screenheight()

        x = (self.screen_width / 2) - (self.app_width / 2)
        y = (self.screen_height / 2) - (self.app_height /2)

        self.master.geometry(f'{self.app_width}x{self.app_height}+{int(x)}+{int(y)}')

        self.master.iconbitmap("logo.ico")
        self.config(bg = '#FFFFFF')

        ImgREhome = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\returnbuttonhome.png')
        ImgREhome = ImageTk.PhotoImage(ImgREhome)
        ImaREhomer =  Label(self, image = ImgREhome)
        ImaREhomer.Image = ImgREhome

        ImgREp = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\returnbutton.jpg')
        ImgREp = ImageTk.PhotoImage(ImgREp)
        ImaREpr =  Label(self, image = ImgREp)
        ImaREpr.Image = ImgREp

        ImgLabel = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\SQLite-connections.png')
        ImgLabel = ImageTk.PhotoImage(ImgLabel)
        Imalabelr =  Label(self, image = ImgLabel)
        Imalabelr.Image = ImgLabel

        Imgadd = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\addbutton.png')
        Imgadd = ImageTk.PhotoImage(Imgadd)
        Imaaddr =  Label(self, image = Imgadd)
        Imaaddr.Image = Imgadd


        Imgdisplay = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\displaybutton.png')
        Imgdisplay = ImageTk.PhotoImage(Imgdisplay)
        Imadisplayr =  Label(self, image = Imgdisplay)
        Imadisplayr.Image = Imgdisplay

        Imgrest = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\restbutton.png')
        Imgrest = ImageTk.PhotoImage(Imgrest)
        Imarestr =  Label(self, image = Imgrest)
        Imarestr.Image = Imgrest

        Imgsup = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\supbutton.jpg')
        Imgsup = ImageTk.PhotoImage(Imgsup)
        Imasupr =  Label(self, image = Imgsup)
        Imasupr.Image = Imgsup

        Imginfo = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\infobutton1.png')
        Imginfo = ImageTk.PhotoImage(Imginfo)
        Imainfor =  Label(self, image = Imginfo)
        Imainfor.Image = Imginfo

        Imgaide = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\aidebutton1.png')
        Imgaide = ImageTk.PhotoImage(Imgaide)
        Imaaider =  Label(self, image = Imgaide)
        Imaaider.Image = Imgaide

        Imgback11 = Image.open('C:\\Users\\pcc\\Desktop\\Covid19sim\\back11.jpg')
        Imgback11 = ImageTk.PhotoImage(Imgback11)
        Imaback11r =  Label(self, image = Imgback11)
        Imaback11r.Image = Imgback11
        self.Loginframe01 = Frame(self, width = 950, height = 500, bd = 0, bg='#FFFFFF', relief = 'flat')
        self.Loginframe01.grid(row = 0, column = 0)

        self.Loginframe0 = Frame(self.Loginframe01, width = 200, height = 200, bd = 0, bg='#FFFFFF', relief = 'flat')
        self.Loginframe0.place(rely = 0, relx = 0)


        self.btnreturn = Button(self.Loginframe0, image = ImgREp, bd = 0, bg='#FFFFFF', command = lambda: master.switch_frame(localWindowA))
        self.btnreturn.place(x=0.20, y=0)



        self.Loginframe1 = Frame(self.Loginframe01, width = 300, height = 200, bd = 5, bg='#FFFFFF', relief = 'flat')
        self.Loginframe1.place(rely = 0, relx = 0.27)


        self.Loginframe310 = Frame(self.Loginframe01, width = 70, height = 60, bd = 0, bg='#FFFFFF', relief = 'flat')
        self.Loginframe310.place(rely = 0, relx = 0.89)

        self.btnreturnh = Button(self.Loginframe310, image = ImgREhome, bd = 0, bg='#FFFFFF', command = lambda: master.switch_frame(StartPage))
        self.btnreturnh.place(x=0, y=0)


        logo = Image.open('logo_cnrst_2018.png')
        logo = ImageTk.PhotoImage(logo)
        logo_label =  Label(self.Loginframe1, bd = 0, bg='#FFFFFF', image = logo)
        logo_label.Image = logo
        logo_label.grid(column=0, row=0)

        logo1 = Image.open('logo_fsdm.png')
        logo1 = ImageTk.PhotoImage(logo1)
        logo_label1 =  Label(self.Loginframe1, bd = 0, bg='#FFFFFF', image = logo1)
        logo_label1.Image = logo1
        logo_label1.grid(column=1, row=0)

        logo2 = Image.open('logo-ministère-santé-Maroc.jpg')
        logo2 = ImageTk.PhotoImage(logo2)
        logo_label2 =  Label(self.Loginframe1, bd = 0, bg='#FFFFFF', image = logo2)
        logo_label2.Image = logo2
        logo_label2.grid(column=2, row=0)




        self.LabelTitle = Label(self, image = ImgLabel,  bg='#FFFFFF', bd = 0)
        self.LabelTitle.place(rely = 0.24, relx = 0.20)

        self.lbback11 = Label(self, image = Imgback11, bd = 0, bg='#FFFFFF')
        self.lbback11.place(rely = 0.10, relx = 0)

#---------------------------------------------------------------------------
        Date = StringVar()
        NameCity = StringVar()
        Latitude = StringVar()
        Longitude = StringVar()
        Description = StringVar()
        conn = sqlite3.connect("dataCovid19sim.db")
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS Citydata(date TEXT,Nom_ville TEXT,Latitude TEXT,Longitude TEXT,Description TEXT)')
#----------------------------------------------------------------------------
        def addData():
            Date = str(self.cal.get())
            Nom_ville = str(self.txtNameCity.get())
            Latitude = str(self.txtLatitude.get())
            Longitude = str(self.txtLongitude.get())
            Description = str(self.txtDescription.get())


            conn = sqlite3.connect("dataCovid19sim.db")
            c = conn.cursor()
            c.execute('INSERT INTO Citydata(Date,Nom_ville,Latitude,Longitude,Description) VALUES(?,?,?,?,?)',(Date,Nom_ville,Latitude,Longitude,Description))
            conn.commit()
            conn.close()
            tkinter.messagebox.showinfo("SQLite connection", "Records Entry sucessifuly")


        def DisplayData():
            conn = sqlite3.connect("dataCovid19sim.db")
            c = conn.cursor()
            c.execute("SELECT * FROM Citydata")
            result = c.fetchall()
            for row in result:
                self.records.insert("", END, values=row)
            conn.commit()
            conn.close()
        def cityinfo(ev):
            viewInfo = self.records.focus()
            learnerData = self.records.item(viewInfo)
            row = learnerData['values']
            Date.set(row[0])
            Nom_ville.set(row[1])
            Latitude.set(row[2])
            Longitude.set(row[3])
            Description.set(row[4])
        def Reset():
            self.cal.delete(0,END)
            self.txtNameCity.delete(0,END)
            self.txtLatitude.delete(0,END)
            self.txtLongitude.delete(0,END)
            self.txtDescription.delete(0,END)
        def remove():

            entry_sl.delete(0,END)
            conn.commit()
        def Delete():
            conn = sqlite3.connect("dataCovid19sim.db")
            c = conn.cursor()
            c.execute("DELETE FROM Citydata WHERE Nom_ville = ?",(self.txtNameCity.get(),))

            conn.commit()
            conn.close()
            tkinter.messagebox.showinfo("SQLite connection", "Records Deleted sucessifuly")


        self.lblcal = Label(self ,text = 'Date', font=('arial', 10, 'bold'), bg= '#FFFFFF', bd = 7)
        self.lblcal.place(relx = 0, rely = 0.40)
        self.cal = DateEntry(self, width = 27, bg = '#D1E9D3', fg = 'black', borderwidth = 2, year = 2021, date_pattern = 'dd/mm/yy', textvariable= Date)
        self.cal.place(relx = 0.10, rely = 0.41)
        self.lblNameCity = Label(self ,text = 'Nom Ville', font=('arial', 10, 'bold'), bg= '#FFFFFF', bd = 7)
        self.lblNameCity.place(relx = 0, rely = 0.48)
        self.txtNameCity = Entry(self , font=('arial', 10, 'bold'), bd = 5, width = 25, bg = '#D1E9D3',textvariable= NameCity)
        self.txtNameCity.place(relx = 0.10, rely = 0.49)

        self.lblLatitude = Label(self , text = 'Latitude', font=('arial', 10, 'bold'), bg= '#FFFFFF', bd = 7)
        self.lblLatitude.place(relx = 0, rely = 0.56)
        self.txtLatitude = Entry(self , font=('arial', 10, 'bold'), bd = 5, width = 25, bg = '#D1E9D3',  textvariable= Latitude)
        self.txtLatitude.place(relx = 0.10, rely = 0.57)

        self.lblLongitude = Label(self, text = 'Longitude', font=('arial', 10, 'bold'), bg= '#FFFFFF', bd = 7)
        self.lblLongitude.place(relx = 0, rely = 0.64)
        self.txtLongitude = Entry(self , font=('arial', 10, 'bold'), bd = 5, width = 25, bg = '#D1E9D3',  textvariable= Longitude)
        self.txtLongitude.place(relx = 0.10, rely = 0.65)

        self.lblDescription = Label(self, text = 'Description', font=('arial', 10, 'bold'), bg= '#FFFFFF', bd = 7)
        self.lblDescription.place(relx = 0, rely = 0.73)
        self.txtDescription = Entry(self , font=('arial', 10, 'bold'), bd = 5, width = 25, bg = '#D1E9D3',  textvariable= Description)
        self.txtDescription.place(relx = 0.10, rely = 0.74)
        Leftframe = Frame(self, width = 700, height = 150, bd = 12, bg = '#d1e9d3', relief = 'ridge')
        Leftframe.place(relx = 0.36, rely = 0.40)

        treescrolly = Scrollbar(Leftframe, orient = "vertical")
        self.records = ttk.Treeview(Leftframe, height = 7, columns=("Date", "Nom Ville", "Latitude", "Longitude", "Description"), yscrollcommand=treescrolly.set)
        treescrolly.pack(side=RIGHT, fill=Y)
        self.records.heading("Date", text="Date")
        self.records.heading("Nom Ville", text="Nom Ville")
        self.records.heading("Latitude", text="Latitude")
        self.records.heading("Longitude", text="Longitude")
        self.records.heading("Description", text="Description")
        self.records["show"] = "headings"

        self.records.column("Date", width = 85)
        self.records.column("Nom Ville", width = 85)
        self.records.column("Latitude", width = 85)
        self.records.column("Longitude", width = 85)
        self.records.column("Description", width = 85)
        self.records.pack(fill=BOTH, expand = 1)
        self.records.bind("<ButtonRelease-1>", cityinfo)
        self.Loginframe4 = Frame(self, width = 950, height = 200, bg='#FFFFFF', bd = 20, relief = 'flat')
        self.Loginframe4.grid(row = 1, column = 0)

        self.btnnew = Button(self.Loginframe4, image = Imgadd, bd = 0, bg = '#FFFFFF', command = addData)
        self.btnnew.place(relx = 0, rely = 0.01)
        self.btndisplay = Button(self.Loginframe4, image = Imgdisplay, bd = 0, bg = '#FFFFFF', command = DisplayData)
        self.btndisplay.place(relx = 0.20, rely = 0.01)

        self.btnsup = Button(self, image = Imgsup, bd = 0, bg ='#FFFFFF', command = Delete)
        self.btnsup.place(relx = 0.90, rely = 0.40)

        self.btnReset = Button(self.Loginframe4, image = Imgrest, bd = 0, bg='#FFFFFF', command = Reset)
        self.btnReset.place(relx = 0.40, rely = 0.01)

        self.btninfo = Button(self.Loginframe4, image =  Imginfo , bg = '#FFFFFF', bd = 0, command = self.info_window)
        self.btninfo.place(relx = 0.59, rely= 0.01)


        self.btnaide = Button(self.Loginframe4, image = Imgaide, bg = '#FFFFFF', bd = 0, command = self.aide_window)
        self.btnaide.place(relx = 0.76, rely = 0.01)

    def info_window(self):
        self.infoWindow = Toplevel(self.master)
        self.app = Info(self.infoWindow)
    def aide_window(self):
        self.aideWindow = Toplevel(self.master)
        self.app = Aide(self.aideWindow)












class Info :
    def __init__(self, master):
        self.master = master
        self.master.title("info")
        self.master.geometry('')
        self.master.iconbitmap("logo.ico")
        self.frame = Frame(self.master)
        self.frame.pack()

        def open_txt():
            text_file = open("info_text.txt", 'r')
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

        my_text = Text(self.frame, width = 150, height = 20, font =("Helvetica", 10))
        my_text.pack(pady = 20)
        open_txt()







class Aide :
    def __init__(self, master):
        self.master = master
        self.master.title("aide")
        self.master.geometry('')
        self.master.iconbitmap("logo.ico")
        self.frame = Frame(self.master)
        self.frame.pack()
        def open_txt1():
            text_file = open("aide_text.txt", 'r')
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

        my_text = Text(self.frame, width = 150, height = 20, font =("Helvetica", 10))
        my_text.pack(pady = 20)
        open_txt1()


if __name__ == "__main__":
    app = CovApp()
    app.mainloop()
