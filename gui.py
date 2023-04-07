from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QGridLayout, QHBoxLayout, QLabel, QVBoxLayout, QGroupBox
from PyQt6.QtGui import QPixmap
# from PyQt6 import QtCore
from PyQt6.QtCore import QRunnable, Qt, QThreadPool
import os
import sys
from time import time, sleep

# class BackgroundThread(QtCore.QThread):
#     def __init__(self):
#         super().__init__()
#         self.run()

#     def run(self):
#         for i in range(0, 10):
#             sleep(0.5)
#             print("Background thread")

class BackgroundThread2(QRunnable):
    def __init__(self):
        super().__init__()
        self.threadPool = QThreadPool()
    def run(self):
        for i in range(0, 10):
            print("Thread")
            sleep(1)

class GUI(QWidget):
    def __init__(self):
        super().__init__()
        # thread = backgroundThread = BackgroundThread()
        self.threadpool = QThreadPool()
        self.backgroundThread = BackgroundThread2()
        self.threadpool.start(self.backgroundThread)

        self.setWindowTitle("GUI Thing")

        initWidth = 400
        initHeight = 400
        self.previousWidth = initWidth
        self.previousHeight = initHeight

        self.mainLayout = QHBoxLayout()
        self.setLayout(self.mainLayout)

        ## create image view window
        self.imageLabel = QLabel()
        self.mainLayout.addWidget(self.imageLabel)
        self.setImage(self.imageLabel, os.path.join(os.getcwd(),"test_image.jpg"))

        ## create side menu
        self.sideMenu = QGroupBox()
        self.mainLayout.addWidget(self.sideMenu)
        self.sideMenuLayout = QVBoxLayout()
        self.sideMenu.setLayout(self.sideMenuLayout)

        ## --- TEMP ---
        testButton = QPushButton(text="button")
        self.sideMenuLayout.addWidget(testButton)
        self.resize(initWidth, initHeight)
        ## ---  --  ---

    def setImage(self, label, imagePath):
        pixmap = QPixmap(imagePath)
        pixmap = pixmap.scaled(400, 400, Qt.AspectRatioMode.KeepAspectRatio)
        label.setPixmap(pixmap)
    
    def resizeEvent(self, obj):
        width = obj.size().width()
        height = obj.size().height()
        if self.previousWidth == width:
            print("Equal")
        else:
            print("Not equal")
        self.previousWidth = width
        # print("w="+str(width)+", h="+str(height))

    # def mouseReleaseEvent(self, obj):
    #     print("Window was clicked")



def launchGui():
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    # backgroundThread = BackgroundThread()
    exit(app.exec())
