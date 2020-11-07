import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from main import Main

'''
开头加载页
'''
class Index(QWidget):
    def __init__(self, parent=None):
        super(Index, self).__init__(parent)
        self.initUI()
        QTimer.singleShot(2000, self.closeWindow)       # 定时器，定时关闭

    def initUI(self):
        '''
        初始化UI
        :return:
        '''
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.palette = QPalette()
        self.pix = QPixmap("D:/1.jpg")
        self.palette.setBrush(QPalette.Background, QBrush(self.pix))
        self.setPalette(self.palette)
        self.resize(self.pix.size())
        self.center()     # 屏幕居中显示

    def center(self):
        '''
        窗口在屏幕居中显示
        :return:
        '''
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    def closeWindow(self):
        self.close()
        self.mainWindow = Main()
        self.mainWindow.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Index()
    window.show()
    sys.exit(app.exec_())