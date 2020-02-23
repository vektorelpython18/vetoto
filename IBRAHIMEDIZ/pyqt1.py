import sys
from PyQt5.QtWidgets import QApplication,QWidget
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.top = 100
        self.left = 100
        self.width = 100
        self.height = 100
        self.title = "İlk Pencere"
        self.initUI()
    
    def initUI(self):
        self.setGeometry(self.width,self.height,self.left,self.top)
        self.setWindowTitle(self.title)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
