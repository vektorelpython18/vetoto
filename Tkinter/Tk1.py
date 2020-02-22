from tkinter import *
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
pencere.geometry("300x300+100+100")
pencere.title("Kamil")
pencere.mainloop()