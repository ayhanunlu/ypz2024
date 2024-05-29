from tkinter import *
import tkinter.messagebox
pencere=Tk() #tkinter tüm foksiyonlarını pencere değişkenile yükle
pencere.geometry ("800x800+150+150")
pencere.title("Hasta Takip Programı 1.0")
def kontrol():
    try:
        with open("veri.dat","r",encoding="UTF-8") as dosya:
            kutt=dosya.readlines()
            return kutt
    except FileNotFoundError:
        kutt=[]
        return kutt

def hastasorma():
    deger=IntVar()
    deger1=IntVar()
    deger2=IntVar()
    pencere2=Frame()
    def arama():
        kutt=kontrol()
        toplamkayit=len(kutt)
        print (kutt)
        print (toplamkayit)
        aramaindex=0
        aranan=sork.get()
        while aramaindex<toplamkayit:
            kut2=kutt[aramaindex].split(",")
            #print (kut2[0])
            sonuc=aranan in kut2[0]
            #print (sonuc)
            if sonuc==True:
                adtext.delete(0,"end")
                adtext.insert(9,kut2[0])
                tctext.delete(0,"end")
                tctext.insert(9,kut2[1])
                emailtext.delete(0,"end")
                emailtext.insert(9,kut2[2])
                boytext.delete(0,"end")
                boytext.insert(9,kut2[3])
                kilotext.delete(0,"end")
                kilotext.insert(9,kut2[4])
                deger.set(int(kut2[5]))
                deger1.set(int(kut2[6]))
                deger2.set(int(kut2[7]))

                

            aramaindex+=1

        pass

    sore=Label(pencere2,text="Aranan Ad-Soyad:",font="Times 20")
    sork=Entry(pencere2,font="Times 20")
    ad=Label(pencere2,text="Ad-Soyad:",font="Times 20")
    adtext=Entry(pencere2,font="Times 20")
    tc=Label(pencere2,text="TC:",font="Times 20")
    tctext=Entry(pencere2,font="Times 20")
    email=Label(pencere2,text="E-mail:",font="Times 20")
    emailtext=Entry(pencere2,font="Times 20")
    boy=Label(pencere2,text="Boy(cm):",font="Times 20")
    boytext=Entry(pencere2,font="Times 20")
    kilo=Label(pencere2,text="Kilo(Kg):",font="Times 20")
    kilotext=Entry(pencere2,font="Times 20")
    kaydet=Button(pencere2,text="Ara",font="Times 20",command=arama)
    cik=Button(pencere2,text="Vazgeç",font="Times 20",command=pencere2.destroy)
    duzelt=Button(pencere2,text="Düzelt",font="Times 20")
    sil=Button(pencere2,text="Sil",font="Times 20")
    r1=Radiobutton(pencere2,text="Bay",font="Times 20",variable=deger,value=2)
    r2=Radiobutton(pencere2,text="Bayan",font="Times 20",variable=deger,value=1)
    c1=Checkbutton(pencere2,text="Tansiyon Hastası",font="Times 20",variable=deger1,onvalue=1,offvalue=0)
    c2=Checkbutton(pencere2,text="Şeker Hastası",font="Times 20",variable=deger2,onvalue=1,offvalue=0)



    pencere2.grid()
    sore.grid(column=0,row=0)
    sork.grid(column=1,row=0,pady=40)
    deger.set(2)
    ad.grid(column=0,row=1)
    adtext.grid(column=1,row=1)
    duzelt.grid(column=3,row=1)
    sil.grid(column=3,row=2)
    tc.grid(column=0,row=2)
    tctext.grid(column=1,row=2)
    kaydet.grid(column=2,row=0)
    cik.grid(column=3,row=0)
    email.grid(column=0,row=3)
    emailtext.grid(column=1,row=3)
    boy.grid(column=0,row=4)
    boytext.grid(column=1,row=4)
    kilo.grid(column=0,row=5)
    kilotext.grid(column=1,row=5)
    r1.grid(column=0,row=6)
    r2.grid(column=1,row=6)
    c1.grid(column=0,row=7)
    c2.grid(column=1,row=7)
    sil['state']=DISABLED
    duzelt['state']=DISABLED
    pencere2.mainloop()
    
    pass
def hastakayit():
    def verikaydet():
        
        
        try:
            with open("veri.dat","r",encoding="UTF-8") as dosya:
                kutt=dosya.readlines()
        except FileNotFoundError:
            kutt=[]

        kut=[]
        kut=adtext.get()+","+tctext.get()+","+emailtext.get()+","+boytext.get()+","+kilotext.get()+","+str(deger.get())+","+str(deger1.get())+","+str(deger2.get())+"\n"
        kutt.append(kut)
        with open("veri.dat","w",encoding="UTF-8") as dosya:
            dosya.writelines(kutt)
            dosya.close
            tkinter.messagebox.showinfo("Dikkat!","Hasta Kaydı Tamamlanmıştır!")
    deger=IntVar()
    deger1=IntVar()
    deger2=IntVar()
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
    r1=Radiobutton(pencere1,text="Bay",font="Times 20",variable=deger,value=2)
    r2=Radiobutton(pencere1,text="Bayan",font="Times 20",variable=deger,value=1)
    c1=Checkbutton(pencere1,text="Tansiyon Hastası",font="Times 20",variable=deger1,onvalue=1,offvalue=0)
    c2=Checkbutton(pencere1,text="Şeker Hastası",font="Times 20",variable=deger2,onvalue=1,offvalue=0)

    


    pencere1.grid()
    deger.set(2)
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
    r1.grid(column=0,row=5)
    r2.grid(column=1,row=5)
    c1.grid(column=0,row=6)
    c2.grid(column=1,row=6)
    
    
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
dosyamenu.add_command(label="Hasta Sorma",font="Times 20",command=hastasorma)
dosyamenu.add_command(label="Hasta Listeleme",font="Times 20")#,command=hastakayit)
dosyamenu.add_command(label="Çıkış",font="Times 20",command=pencere.destroy)
dosyamenu.add_command(label="Program Hakkında",font="Times 20",command=hakkinda)

pencere.mainloop()#sonsuz döngü