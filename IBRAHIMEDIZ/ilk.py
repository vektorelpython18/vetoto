import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import QtWidgets,uic
from DB import VetDB
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pencere = uic.loadUi(r"C:\Users\vektorel\Documents\GitHub\vetoto\IBRAHIMEDIZ\ilk.ui")
        self.initUI()
    
    def initUI(self):
        self.pencere.show()
        self.pencere.bt1.clicked.connect(self.tiklandi)
        self.pencere.cmb1.currentIndexChanged.connect(self.yazdir)
    def tiklandi(self):
        print(self.pencere.txtAdi.text())
        self.pencere.pBar.setMaximum(1000)
        self.pencere.pBar.setValue(1000)
        #------------------------------
        veri  = VetDB()
        self.sozluk = dict(veri.eyaletGetir())
        for item in self.sozluk:
            self.pencere.cmb1.addItem(item)
        #print(*veri.eyaletGetir(),sep="\n")
        #----------------------------------------------
    def yazdir(self):
        param = self.sozluk[self.pencere.cmb1.currentText()]
        self.pencere.cmb2.clear()
        veri = VetDB()
        self.sozluk2 = dict(veri.SecilieyaletGetir(param))
        for item in self.sozluk2:
            self.pencere.cmb2.addItem(item)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
