from tkinter import *
import tkinter.messagebox
import sqlite3
pencere=Tk() #tkinter tüm foksiyonlarını pencere değişkenile yükle
pencere.geometry ("800x800+150+150")
pencere.title("Hasta Takip Programı 1.0")
global aramaindex
aramaindex=0

con=sqlite3.connect("veri.db")
cursor=con.cursor()
global tablo
global silno
tablo="CREATE TABLE IF NOT EXISTS veri(id INTEGER PRIMARY KEY,ad TEXT,tc TEXT,email TEXT,boy TEXT,kilo TEXT,deger TEXT,deger1 TEXT,deger2 TEXT)"

def islem(ifade):
    cursor.execute(ifade)
    con.commit()
    
islem(tablo)
def kontrol():
    try:
        with open("veri.dat","r",encoding="UTF-8") as dosya:
            kutt=dosya.readlines()
            dosya.close()
            return kutt
    except FileNotFoundError:
        kutt=[]
        return kutt

def yaz(kutt):
        with open("veri.dat","w",encoding="UTF-8") as dosya:
            dosya.writelines(kutt)
            dosya.close     
def hastalistele():
    def listeduzelt():
        kutt=kontrol()
        adet=len(entries)
        toplamkayit=len(kutt)
        #print (adet)
        aramaindex=0
        index=0
        kut2=[]
        kut=[]
        kut4=[]
        while aramaindex<toplamkayit:
            kut2=kutt[aramaindex].split(",")
            kut=entries[index].get()+","+entries[index+1].get()+","+entries[index+2].get()+","+kut2[3]+","+kut2[4]+","+kut2[5]+","+kut2[6]+","+kut2[7]
            kut4.append(kut)
            index+=3
            aramaindex+=1
        yaz(kut4)
        tkinter.messagebox.showinfo("Veri Düzeltildi","İlgili veri düzeltildi!!!")
            
            

        


        pass

    kutt=kontrol()
    variables=[]
    entries=[]
    kont=0
    index=-1
    toplamkayit=len(kutt)
    print (toplamkayit)
    pencere3=Frame()
    for k in range(toplamkayit):
        for i in range(3):
            va=StringVar()
            en=Entry(pencere3,font="Times 15",textvariable=va)
            en.grid(row=k,column=i)
            variables.append(va)
            entries.append(en)
    geri=Button(pencere3,text="Geri Dön",font="Times 15",command=pencere3.destroy)  
    duzelt=Button(pencere3,text="Duzelt",font="Times 15",command=listeduzelt)
    while kont<toplamkayit:
        bol=kutt[kont].split(",")
        index+=1
        entries[index].insert(0,bol[0])
        index+=1
        entries[index].insert(0,bol[1])
        index+=1
        entries[index].insert(0,bol[2])
        kont+=1

    pencere3.grid()
    geri.grid(column=4,row=0)
    duzelt.grid(column=4,row=1)


    pencere3.mainloop()

def hastasorma():
    global aramaindex
    deger=IntVar()
    deger1=IntVar()
    deger2=IntVar()
    pencere2=Frame()
    
    def silme():
        global silno
        global aramaindex
        
        
        #print(aramaindex)
        #silinecek=aramaindex-1
        """if silinecek<0:
            tkinter.messagebox.INFO("Silinemiyor","Silinecek Veri Yok")
            
        else:"""
        sonuc=tkinter.messagebox.askyesno("Silinecek!","Eminmisinz?")
            #print (sonuc)
        if sonuc==True:
                """kutt=kontrol()
                kutt.pop(silinecek)
                yaz(kutt)"""
                r=f"DELETE FROM veri WHERE id={silno}"
                islem(r)
                sil['state']=DISABLED
                duzelt['state']=DISABLED
                tkinter.messagebox.showinfo("Silindi!!!","İlgili veri silindi!!!")
                aramaindex=0
                pencere2.destroy()
                    
       
    def duzelt():
        global aramaindex
        duzeltilecek=aramaindex-1

        kutt=kontrol()
        if duzeltilecek<0:
            tkinter.messagebox.showinfo("Düzeltilemiyor!","Düzeltilecek Veri Bulunamadı!")
            pencere2.destroy()
        else:
            kut=adtext.get()+","+tctext.get()+","+emailtext.get()+","+boytext.get()+","+kilotext.get()+","+str(deger.get())+","+str(deger1.get())+","+str(deger2.get())+"\n"
            kutt.pop(duzeltilecek)
            kutt.insert(duzeltilecek,kut)
            yaz(kutt)
            tkinter.messagebox.showinfo("Düzeltildi","İlgili veri düzeltildi!!!")



        
        

        
    def arama():
        global tablo
        global aramaindex
        global silno
        islem(tablo)
        ara="SELECT * FROM veri"
        islem(ara)
        kutt=list(cursor.fetchall())
    

        #kutt=kontrol()
        toplamkayit=len(kutt)
        print (kutt)
        
        #print (toplamkayit)
        #aramaindex=0
        if aramaindex>=toplamkayit:
            #print("büyük")
            aramaindex=0
        aranan=sork.get()
        #print ("Ayhan")
        #print (type(kutt))
        #print (kutt[4][1])
        while aramaindex<toplamkayit:
            
            kut2=kutt[aramaindex][1]
            #print (kut2[0])
            sonuc=aranan in kut2
            #print (sonuc)
            if sonuc==True:
                silno=kutt[aramaindex][0]
                adtext.delete(0,"end")
                adtext.insert(0,kutt[aramaindex][1])
                tctext.delete(0,"end")
                tctext.insert(0,kutt[aramaindex][2])
                emailtext.delete(0,"end")
                emailtext.insert(0,kutt[aramaindex][3])
                boytext.delete(0,"end")
                boytext.insert(0,kutt[aramaindex][4])
                kilotext.delete(0,"end")
                kilotext.insert(0,kutt[aramaindex][5])
                deger.set(int(kutt[aramaindex][6]))
                deger1.set(int(kutt[aramaindex][7]))
                deger2.set(int(kutt[aramaindex][8]))
                #print(aramaindex)
                #print(toplamkayit)
                aramaindex+=1
                sil['state']=NORMAL
                duzelt['state']=NORMAL

                break

                

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
    duzelt=Button(pencere2,text="Düzelt",font="Times 20",command=duzelt)
    sil=Button(pencere2,text="Sil",font="Times 20",command=silme)
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
    global tablo
    def verikaydet():
        global tablo
         
        kut=[]
        kut.append(adtext.get())
        kut.append(tctext.get())
        kut.append(emailtext.get())
        kut.append(boytext.get())
        kut.append(kilotext.get())
        kut.append(str(deger.get()))
        kut.append(str(deger1.get()))
        kut.append(str(deger2.get()))
        
        
        cursor.execute(tablo)
        con.commit()
        kaydet="INSERT INTO veri(ad,tc,email,boy,kilo,deger,deger1,deger2) VALUES (?,?,?,?,?,?,?,?)"
        cursor.execute(kaydet,kut)
        con.commit()
        #con.close()
        tkinter.messagebox.showinfo("Dikkat!","Hasta Kaydı Tamamlanmıştır!")
        pencere1.destroy()
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
dosyamenu.add_command(label="Hasta Listeleme",font="Times 20",command=hastalistele)
dosyamenu.add_command(label="Çıkış",font="Times 20",command=pencere.destroy)
dosyamenu.add_command(label="Program Hakkında",font="Times 20",command=hakkinda)

pencere.mainloop()#sonsuz döngü