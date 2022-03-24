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

#-----------------------------------------------------------------------------------------------
    Date = StringVar()
    NameCity = StringVar()
    Latitude = StringVar()
    Longitude = StringVar()
    Description = StringVar()
#------------------------------------------------------------------------------------------------
    conn = sqlite3.connect("dataCovid19sim.db")
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS Citydata(date TEXT,Nom_ville TEXT,Latitude TEXT,Longitude TEXT,Description TEXT)')
#-----------------------------------------------------------------------------------------------------------------------------
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


#-------------------------------------------------------------------------------------------------------------------------------------------

    self.lblcal = Label(self ,text = 'Date', font=('arial', 10, 'bold'), bg= '#FFFFFF', bd = 7)
    self.lblcal.place(relx = 0, rely = 0.40)
    self.cal = DateEntry(self, width = 27, bg = '#D1E9D3', fg = 'black', borderwidth = 2, year = 2021, date_pattern = 'dd/mm/yy', textvariable= Date)
    self.cal.place(relx = 0.10, rely = 0.41)

    self.lblNameCity = Label(self ,text = 'Nom Ville', font=('arial', 10, 'bold'), bg= '#FFFFFF', bd = 7)
    self.lblNameCity.place(relx = 0, rely = 0.48)
    self.txtNameCity = Entry(self , font=('arial', 10, 'bold'), bd = 5, width = 25, bg = '#D1E9D3', justify = 'left', textvariable= NameCity)
    self.txtNameCity.place(relx = 0.10, rely = 0.49)

    self.lblLatitude = Label(self , text = 'Latitude', font=('arial', 10, 'bold'), bg= '#FFFFFF', bd = 7)
    self.lblLatitude.place(relx = 0, rely = 0.56)
    self.txtLatitude = Entry(self , font=('arial', 10, 'bold'), bd = 5, width = 25, bg = '#D1E9D3', justify = 'left',  textvariable= Latitude)
    self.txtLatitude.place(relx = 0.10, rely = 0.57)

    self.lblLongitude = Label(self, text = 'Longitude', font=('arial', 10, 'bold'), bg= '#FFFFFF', bd = 7)
    self.lblLongitude.place(relx = 0, rely = 0.64)
    self.txtLongitude = Entry(self , font=('arial', 10, 'bold'), bd = 5, width = 25, bg = '#D1E9D3', justify = 'left',  textvariable= Longitude)
    self.txtLongitude.place(relx = 0.10, rely = 0.65)

    self.lblDescription = Label(self, text = 'Description', font=('arial', 10, 'bold'), bg= '#FFFFFF', bd = 7)
    self.lblDescription.place(relx = 0, rely = 0.73)
    self.txtDescription = Entry(self , font=('arial', 10, 'bold'), bd = 5, width = 25, bg = '#D1E9D3', justify = 'left',  textvariable= Description)
    self.txtDescription.place(relx = 0.10, rely = 0.74)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

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

#------------------------------------------------------------------------------------------------------------------------------------
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
    self.lblcal = Label(self ,text = 'Date', font=('arial', 10, 'bold'), bg= '#FFFFFF', bd = 7)
    self.lblcal.place(relx = 0, rely = 0.40)
    self.cal = DateEntry(self, width = 27, bg = '#D1E9D3', fg = 'black', borderwidth = 2, year = 2021, date_pattern = 'dd/mm/yy', textvariable= Date)
    self.cal.place(relx = 0.10, rely = 0.41)
    #--------------------------------------------------------------------------------------------------------------------------------------------------------
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
            def calculetday(self):
                self.dateDepart = (self.txtDated.get_date())
                self.dateFinal = (self.txtDatef.get_date())
                self.day = (abs ((self.dateDepart - self.dateFinal).days))
                self.Days.set(str(self.day))
