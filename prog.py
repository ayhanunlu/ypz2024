from tkinter import *
pencere=Tk() #tkinter tüm foksiyonlarını pencere değişkenile yükle
pencere.geometry ("800x800+150+150")
pencere.title("Hasta Takip Programı 1.0")
def hastakayit():
    def verikaydet():
        try:
            with open("veri.dat","r",encoding="UTF-8") as dosya:
                kutt=dosya.readlines()
        except FileNotFoundError:
            kutt=[]

        kut=[]
        kut=adtext.get()+","+tctext.get()+","+emailtext.get()+","+boytext.get()+","+kilotext.get()+"\n"
        kutt.append(kut)
        with open("veri.dat","w",encoding="UTF-8") as dosya:
            dosya.writelines(kutt)
            dosya.close
        
    #pencere.title("Hasta Kayıt")
    pencere1=Frame()
    ad=Label(pencere1,text="Ad-Soyad:",font="Times 20")
    adtext=Entry(pencere1,font="Times 20")
    tc=Label(pencere1,text="TC:",font="Times 20")
    tctext=Entry(pencere1,font="Times 20")
    email=Label(pencere1,text="E-mail:",font="Times 20")
    emailtext=Entry(pencere1,font="Times 20")
    boy=Label(pencere1,text="Boy(cm):",font="Times 20")
    boytext=Entry(pencere1,font="Times 20")
    kilo=Label(pencere1,text="Kilo(Kg):",font="Times 20")
    kilotext=Entry(pencere1,font="Times 20")
    kaydet=Button(pencere1,text="Kaydet",font="Times 20",command=verikaydet)
    cik=Button(pencere1,text="Çıkış",font="Times 20",command=pencere1.destroy)

    


    pencere1.grid()
    ad.grid(column=0,row=0)
    adtext.grid(column=1,row=0)
    tc.grid(column=0,row=1)
    tctext.grid(column=1,row=1)
    kaydet.grid(column=2,row=0)
    cik.grid(column=2,row=1)
    email.grid(column=0,row=2)
    emailtext.grid(column=1,row=2)
    boy.grid(column=0,row=3)
    boytext.grid(column=1,row=3)
    kilo.grid(column=0,row=4)
    kilotext.grid(column=1,row=4)
    
    
    pencere1.mainloop()
def hakkinda():
    pencere.title("Program Hakkında")
    pencere5=Frame(pencere)
    e1=Label(pencere5,font="Times 20",text="Programlıyan Yapay Zeka Grubu\n2024\nHasta Takip 1.0")
    cik=Button(pencere5,text="Çıkış",font="Times 20",command=pencere5.destroy)


    pencere5.grid()
    e1.grid(column=0,row=0)
    cik.grid()
    pencere5.mainloop()

menu=Menu(pencere,font="Times 20")
pencere.config(menu=menu)
dosyamenu=Menu(menu,tearoff=0)
menu.add_cascade(label="Veri",menu=dosyamenu)
dosyamenu.add_command(label="Hasta Kayıt",font="Times 20",command=hastakayit)
dosyamenu.add_command(label="Hasta Sorma",font="Times 20"),#command=hastakayit)
dosyamenu.add_command(label="Hasta Listeleme",font="Times 20")#,command=hastakayit)
dosyamenu.add_command(label="Çıkış",font="Times 20",command=pencere.destroy)
dosyamenu.add_command(label="Program Hakkında",font="Times 20",command=hakkinda)

pencere.mainloop()#sonsuz döngü