import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

'''
加载动画
'''
class Loading(QWidget):
    def __init__(self, parent=None):
        super(Loading, self).__init__(parent)
        self.setWindowOpacity(0.5)        #设置透明度
        self.label = QLabel(self)
        self.setFixedSize(1000, 800)         #设置为动图大小
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.movie = QMovie("D:/loading.gif")
        self.label.setMovie(self.movie)
        self.movie.start()
