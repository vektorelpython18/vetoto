from tkinter import *
from tkinter import messagebox,filedialog
pencere = Tk()
#-------------------
etiket = Label(text="Adı:")
etiket.grid(column=0,row=0)
#--------------------
textBox = Entry()
textBox.grid(column=1,row=0)
#-------------------
def tiklandi():
    print(textBox.get())
    print(rdb.getboolean(varRdb))
    print(varRdb)
dugme = Button(text="Aktarım",command=tiklandi)
dugme.grid(column=2,row=0)
#--------------------
varRdb = BooleanVar()
varRdb = False
rdb = Radiobutton(text="deneme",value=varRdb,command=tiklandi)
rdb.grid(column=3,row=0)
#--------------------
def mesaj():
    mesaj = "Merhaba Kamil"
    # mesajBox = messagebox.showwarning("Yazılım",mesaj)
    mesaj = messagebox.askyesno("Yazılım","Açmak istiyor musun")
    if mesaj:
        dosya = filedialog.askopenfile(initialdir="/",
        title="Dosya Aç",
        filetypes=(("Resim Dosyaları","*.jpg"),("Bütün Dosyalar","*.*")))
menu = Menu(pencere)
pencere.config(menu=menu)
dosyaMenu = Menu(menu)
menu.add_cascade(label="Dosya",menu=dosyaMenu)
dosyaMenu.add_command(label="Yeni",command=mesaj)
dosyaMenu.add_command(label="Çıkış",command=pencere.quit)
pencere.geometry("300x300+100+100")
pencere.title("Kamil")
pencere.mainloop()