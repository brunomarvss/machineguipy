from tkinter import *




def machcon():


    root = Tk()
    root.title("MACHINE CONTROLS")
    root.geometry("700x500")
    root.configure(background='#4E87C1')
#labels

    lbl_vacuum = Label(root, text = "VACUUM CONTROLS",fg='white',bg='#4E87C1',font='Verdana 12')
    lbl_output = Label(root, text = "OUTPUT CONTROLS",fg='white',bg='#4E87C1',font='Verdana 12')
    lbl_mc = Label(root, text = "MACHINE CONTROLS",fg='white',bg='#4E87C1',font='Verdana 15')
#buttonsdeclare
    btnvalveon1 = Button(root, text = "VALVE1 ON")
    btnvalveon2 = Button(root, text = "VALVE2 ON")
    btnvalveon3 = Button(root, text = "VALVE3 ON")
    btnvalveon4 = Button(root, text = "VALVE4 ON")
    btnvalveon5 = Button(root, text = "VALVE5 ON")
    btnvalveon6 = Button(root, text = "VALVE6 ON")
    btnvalveon7 = Button(root, text = "VALVE7 ON")
    btnvalveon8 = Button(root, text = "VALVE8 ON")
    btnvalveonall= Button(root, text = "ALL VAC ON")

    btnvalveoff1 = Button(root, text = "VALVE1 OFF")
    btnvalveoff2 = Button(root, text = "VALVE2 OFF")
    btnvalveoff3 = Button(root, text = "VALVE3 OFF")
    btnvalveoff4 = Button(root, text = "VALVE4 OFF")
    btnvalveoff5 = Button(root, text = "VALVE5 OFF")
    btnvalveoff6 = Button(root, text = "VALVE6 OFF")
    btnvalveoff7 = Button(root, text = "VALVE7 OFF")
    btnvalveoff8 = Button(root, text = "VALVE8 OFF")
    btnvalveoffall = Button(root, text = "ALL VAC OFF")

    btnvalvecycle1 = Button(root, text = "VALVE1 CYCLE")
    btnvalvecycle2 = Button(root, text = "VALVE2 CYCLE")
    btnvalvecycle3 = Button(root, text = "VALVE3 CYCLE")
    btnvalvecycle4 = Button(root, text = "VALVE4 CYCLE")
    btnvalvecycle5 = Button(root, text = "VALVE5 CYCLE")
    btnvalvecycle6 = Button(root, text = "VALVE6 CYCLE")
    btnvalvecycle7 = Button(root, text = "VALVE7 CYCLE")
    btnvalvecycle8 = Button(root, text = "VALVE8 CYCLE")
    btnvalvecycleall = Button(root, text = "ALL VAC CYCLE")

    btninteron = Button(root, text = "INTERLOCK ON")
    btninteroff = Button(root, text = "INTERLOCK OFF")

    btnbrakeon = Button(root, text = "BRAKE ON",width='12')
    btnbrakeoff = Button(root, text = "BRAKE OFF",width='12')

    btntclampon = Button(root, text = "T-CLAMP ON",width='12')
    btntclampoff = Button(root, text = "T-CLAMP OFF",width='12')

    btnthome = Button(root, text = "T-HOME",width='12')
    btntflip = Button(root, text = "T-FLIP",width='12')

    btncyclerun = Button(root, text = "CYCLE RUN",width='27')
#objectscoord
    lbl_vacuum.place(x=100,y=90)
    lbl_output.place(x=460,y=90)
    lbl_mc.place(x=255,y=40)

    btnvalveon1.place(x=50,y=150) #y step by 30
    btnvalveon2.place(x=50,y=180)
    btnvalveon3.place(x=50,y=210)
    btnvalveon4.place(x=50,y=240)
    btnvalveon5.place(x=50,y=270)
    btnvalveon6.place(x=50,y=300)
    btnvalveon7.place(x=50,y=330)
    btnvalveon8.place(x=50,y=360)
    btnvalveonall.place(x=47,y=390)

    btnvalveoff1.place(x=140,y=150) #y step by 30
    btnvalveoff2.place(x=140,y=180)
    btnvalveoff3.place(x=140,y=210)
    btnvalveoff4.place(x=140,y=240)
    btnvalveoff5.place(x=140,y=270)
    btnvalveoff6.place(x=140,y=300)
    btnvalveoff7.place(x=140,y=330)
    btnvalveoff8.place(x=140,y=360)
    btnvalveoffall.place(x=137,y=390)

    btnvalvecycle1.place(x=230,y=150) #y step by 30
    btnvalvecycle2.place(x=230,y=180)
    btnvalvecycle3.place(x=230,y=210)
    btnvalvecycle4.place(x=230,y=240)
    btnvalvecycle5.place(x=230,y=270)
    btnvalvecycle6.place(x=230,y=300)
    btnvalvecycle7.place(x=230,y=330)
    btnvalvecycle8.place(x=230,y=360)
    btnvalvecycleall.place(x=227,y=390)

    btninteron.place(x=450,y=150)
    btninteroff.place(x=550,y=150)

    btnbrakeon.place(x=450,y=200)
    btnbrakeoff.place(x=553,y=200)

    btntclampon.place(x=450,y=250)
    btntclampoff.place(x=553,y=250)

    btnthome.place(x=450,y=300)
    btntflip.place(x=553,y=300)

    btncyclerun.place(x=450,y=350)

#VALVE ON EVENT FUNC
#<INSERT EXTRA CODE> INSIDE THE FUNCTION
    def valve1on(event):
        btnvalveon1.config(bg='green',fg='white')
        btnvalveoff1.config(bg='#EFEFEF',fg='black')
    def valve2on(event):
        btnvalveon2.config(bg='green',fg='white')
        btnvalveoff2.config(bg='#EFEFEF',fg='black')
    def valve3on(event):
        btnvalveon3.config(bg='green',fg='white')
        btnvalveoff3.config(bg='#EFEFEF',fg='black')
    def valve4on(event):
        btnvalveon4.config(bg='green',fg='white')
        btnvalveoff4.config(bg='#EFEFEF',fg='black')
    def valve5on(event):
        btnvalveon5.config(bg='green',fg='white')
        btnvalveoff5.config(bg='#EFEFEF',fg='black')
    def valve6on(event):
        btnvalveon6.config(bg='green',fg='white')
        btnvalveoff6.config(bg='#EFEFEF',fg='black')
    def valve7on(event):
        btnvalveon7.config(bg='green',fg='white')
        btnvalveoff7.config(bg='#EFEFEF',fg='black')
    def valve8on(event):
        btnvalveon8.config(bg='green',fg='white')
        btnvalveoff8.config(bg='#EFEFEF',fg='black')
    def valveallon(event):
        valve1on(event)
        valve2on(event)
        valve3on(event)
        valve4on(event)
        valve5on(event)
        valve6on(event)
        valve7on(event)
        valve8on(event)


#VALVE OFF EVENT FUNC
#<INSERT EXTRA CODE> INSIDE THE FUNCTION
    def valve1off(event):
        btnvalveoff1.config(bg='red',fg='white')
        btnvalveon1.config(bg='#EFEFEF',fg='black')
    def valve2off(event):
        btnvalveoff2.config(bg='red',fg='white')
        btnvalveon2.config(bg='#EFEFEF',fg='black')
    def valve3off(event):
        btnvalveoff3.config(bg='red',fg='white')
        btnvalveon3.config(bg='#EFEFEF',fg='black')
    def valve4off(event):
        btnvalveoff4.config(bg='red',fg='white')
        btnvalveon4.config(bg='#EFEFEF',fg='black')
    def valve5off(event):
        btnvalveoff5.config(bg='red',fg='white')
        btnvalveon5.config(bg='#EFEFEF',fg='black')
    def valve6off(event):
        btnvalveoff6.config(bg='red',fg='white')
        btnvalveon6.config(bg='#EFEFEF',fg='black')
    def valve7off(event):
        btnvalveoff7.config(bg='red',fg='white')
        btnvalveon7.config(bg='#EFEFEF',fg='black')
    def valve8off(event):
        btnvalveoff8.config(bg='red',fg='white')
        btnvalveon8.config(bg='#EFEFEF',fg='black')

    def valvealloff(event):
        valve1off(event)
        valve2off(event)
        valve3off(event)
        valve4off(event)
        valve5off(event)
        valve6off(event)
        valve7off(event)
        valve8off(event)

#OUTPUT CONTROL OBJECTS EVENT FUNC
#<INSERT EXTRA CODE> INSIDE THE FUNCTION
    def interon(event):
        btninteron.config(bg='green',fg='white')
        btninteroff.config(bg='#EFEFEF',fg='black')
    def interoff(event):
        btninteroff.config(bg='red',fg='white')
        btninteron.config(bg='#EFEFEF',fg='black')
    def brakeon(event):
        btnbrakeon.config(bg='green',fg='white')
        btnbrakeoff.config(bg='#EFEFEF',fg='black')
    def brakeoff(event):
        btnbrakeoff.config(bg='red',fg='white')
        btnbrakeon.config(bg='#EFEFEF',fg='black')
    def clampon(event):
        btntclampon.config(bg='green',fg='white')
        btntclampoff.config(bg='#EFEFEF',fg='black')
    def clampoff(event):
        btntclampoff.config(bg='red',fg='white')
        btntclampon.config(bg='#EFEFEF',fg='black')
    def homeon(event):
        btnthome.config(bg='green',fg='white')
    def flipon(event):
        btntflip.config(bg='green',fg='white')




#OBJECT EVENT BIND

    btnvalveon1.bind("<Button-1>",valve1on)
    btnvalveon2.bind("<Button-1>",valve2on)
    btnvalveon3.bind("<Button-1>",valve3on)
    btnvalveon4.bind("<Button-1>",valve4on)
    btnvalveon5.bind("<Button-1>",valve5on)
    btnvalveon6.bind("<Button-1>",valve6on)
    btnvalveon7.bind("<Button-1>",valve7on)
    btnvalveon8.bind("<Button-1>",valve8on)
    btnvalveonall.bind("<Button-1>",valveallon)
    btnvalveoff1.bind("<Button-1>",valve1off)
    btnvalveoff2.bind("<Button-1>",valve2off)
    btnvalveoff3.bind("<Button-1>",valve3off)
    btnvalveoff4.bind("<Button-1>",valve4off)
    btnvalveoff5.bind("<Button-1>",valve5off)
    btnvalveoff6.bind("<Button-1>",valve6off)
    btnvalveoff7.bind("<Button-1>",valve7off)
    btnvalveoff8.bind("<Button-1>",valve8off)
    btnvalveoffall.bind("<Button-1>",valvealloff)
    btninteron.bind("<Button-1>",interon)
    btninteroff.bind("<Button-1>",interoff)
    btnbrakeon.bind("<Button-1>",brakeon)
    btnbrakeoff.bind("<Button-1>",brakeoff)
    btntclampon.bind("<Button-1>",clampon)
    btntclampoff.bind("<Button-1>",clampoff)
    btnthome.bind("<Button-1>",homeon)
    btntflip.bind("<Button-1>",flipon)

    root.mainloop()

machcon()
