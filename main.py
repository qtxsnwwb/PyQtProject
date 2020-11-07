import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *



from loading import Loading

'''
主页
'''
class Main(QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.initUI()
        self.setMenu()

    def initUI(self):
        '''
        初始化UI
        :return:
        '''
        self.resize(1000, 600)
        self.setWindowTitle("海上数据挖掘可视化分析系统")
        self.setWindowIcon(QIcon(".\\res\\boat.ico"))      # 设置窗体图标
        self.center()    # 屏幕居中显示

    def setMenu(self):
        """
        设置菜单栏
        :return:
        """
        menubar = self.menuBar()
        importMenu = menubar.addMenu(u"导入数据")
        remoteAct = QAction("遥感数据", self)
        AisAct = QAction("AIS数据", self)
        ReplayAct = QAction("数据回放", self)
        importMenu.addAction(remoteAct)
        importMenu.addAction(AisAct)
        importMenu.addAction(ReplayAct)
        # remoteAct.triggered.connect()
        # AisAct.triggered.connect()
        # ReplayAct.triggered.connect()

        preMenu = menubar.addMenu(u"预处理")
        defogAct = QAction("视觉去雾", self)
        enhanceAct = QAction("低照度增强", self)
        filterAct = QAction("AIS数据筛选", self)
        preMenu.addAction(defogAct)
        preMenu.addAction(enhanceAct)
        preMenu.addAction(filterAct)
        # defogAct.triggered.connect()
        # enhanceAct.triggered.connect()
        # filterAct.triggered.connect()

        visualMenu = menubar.addMenu(u"源数据可视化")
        trackAct = QAction("船舶轨迹可视化", self)
        densityAct = QAction("船舶密度可视化", self)
        heatAct = QAction("热力图", self)
        trafficFlowAct = QAction("船舶交通流可视化", self)
        visualMenu.addAction(trackAct)
        visualMenu.addAction(densityAct)
        visualMenu.addAction(heatAct)
        visualMenu.addAction(trafficFlowAct)
        # trackAct.triggered.connect()
        # densityAct.triggered.connect()
        # heatAct.triggered.connect()
        # trafficFlowAct.triggered.connect()

        processMenu = menubar.addMenu(u"过程可视化")
        dbscanAct = QAction("航道驱动聚类", self)
        abnAct = QAction("异常模式", self)
        freAct = QAction("频繁模式", self)
        togAct = QAction("共现模式", self)
        cycAct = QAction("周期模式", self)
        processMenu.addAction(dbscanAct)
        processMenu.addAction(abnAct)
        processMenu.addAction(freAct)
        processMenu.addAction(togAct)
        processMenu.addAction(cycAct)
        # dbscanAct.triggered.connect()
        # abnAct.triggered.connect()
        # freAct.triggered.connect()
        # togAct.triggered.connect()
        # cycAct.triggered.connect()

        resultMenu = menubar.addMenu(u"结果可视化")
        randForestAct = QAction("随机森林算法", self)
        resultMenu.addAction(randForestAct)
        # randForestAct.triggered.connect()

        aboutMenu = menubar.addMenu(u"关于")
        aboutAct = QAction("关于", self)
        aboutMenu.addAction(aboutAct)
        aboutAct.triggered.connect(self.showAbout)

    def process(self):
        self.window = Loading()
        self.window.show()

    def center(self):
        '''
        窗口在屏幕居中显示
        :return:
        '''
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    def showAbout(self):
        """
        显示关于
        :return:
        """
        QMessageBox.about(self, "关于", "海上数据挖掘可视化分析系统")

