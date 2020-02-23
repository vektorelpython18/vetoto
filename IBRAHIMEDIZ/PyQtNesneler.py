import sys
from PyQt5.QtWidgets import QApplication,QWidget,\
QPushButton,QLineEdit,QLabel,QMessageBox
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.top = 100
        self.left = 100
        self.width = 640
        self.height = 480
        self.title = "İlk Pencere"
        self.initUI()
    
    def initUI(self):
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.setWindowTitle(self.title)
        #------------------------------
        dugme = QPushButton(self)
        dugme.setText("Tıkla")
        dugme.setToolTip("Tıklama Düğmesi")
        dugme.move(20,20)
        dugme.clicked.connect(self.tiklandi)
        self.etiket = QLabel("Aktarım Bekliyor",self)
        self.etiket.move(20,50)
        self.textBox = QLineEdit(self)
        self.textBox.move(20,70)
        #------------------------------
        self.show()

    def tiklandi(self):
        metin  = self.textBox.text()
        self.etiket.setText(metin)
        self.textBox.setText("Aktarım Yapıldı")
        self.textBox.setEnabled(False)
        el_Cevap = QMessageBox.question(self,"Bak","Python'ı Seviyor Musun?",
        QMessageBox.Yes | QMessageBox.YesAll | QMessageBox.No,\
                 QMessageBox.Yes)
        if el_Cevap == QMessageBox.Yes:
            QMessageBox.information(self,"Python","Python da seni...")
    

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
