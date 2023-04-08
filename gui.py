from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QGridLayout, QHBoxLayout, QLabel, QVBoxLayout, QGroupBox
from PyQt6.QtGui import QPixmap
# from PyQt6 import QtCore
from PyQt6.QtCore import QRunnable, Qt, QThreadPool
import os
import sys
from time import time, sleep
from PIL import Image

# class BackgroundThread(QtCore.QThread):
#     def __init__(self):
#         super().__init__()
#         self.run()

#     def run(self):
#         for i in range(0, 10):
#             sleep(0.5)
#             print("Background thread")

# global windowWidth
# global windowHeight
# windowWidth = -1
# windowHeight = -1

class BackgroundThread2(QRunnable):
    def __init__(self, mainObj):
        super().__init__()
        self.mainObj = mainObj
        self.threadPool = QThreadPool()
        self.isRunning = True
    def run(self):
        previousWidth = -1
        previousHeight = -1
        while self.isRunning:
            newWidth = self.mainObj.size().width()
            newHeight = self.mainObj.size().height()
            if (newWidth != previousWidth) or (newHeight != previousHeight):
                previousHeight = newHeight
                previousWidth = newWidth
                self.resizeImage(newWidth, newHeight)
            sleep(0.2)
    def resizeImage(self, windowWidth, windowHeight):
        print("imageLabel" in self.mainObj.__dir__())
        self.mainObj.setImage(self.mainObj.imageLabel, self.mainObj.imageInfo["filePath"])

class GUI(QWidget):
    def __init__(self):
        super().__init__()
        # thread = backgroundThread = BackgroundThread()

        self.setWindowTitle("GUI Thing")

        initWindowWidth = 400
        initWindowHeight = 300

        self.mainLayout = QHBoxLayout()
        self.setLayout(self.mainLayout)

        ## create image view window
        self.imageInfo = {
            "filePath": "",
            "imageWidth": -1,
            "imageHeight": -1,
        }
        self.imageProportionOfWindowWidth = 0.5 # Width of the winodw that the image will take up
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
        self.resize(initWindowHeight, initWindowHeight)
        ## ---  --  ---
        
        ## start background thread for updating image size when the window is resized
        self.threadpool = QThreadPool()
        self.backgroundThread = BackgroundThread2(self)
        self.threadpool.start(self.backgroundThread)

    def __del__(self):
        ## stop the background thread
        self.backgroundThread.isRunning = False

    def setImage(self, label, imagePath):
        image = Image.open(imagePath)
        self.imageInfo["imageWidth"] = image.width
        self.imageInfo["imageHeight"] = image.height
        self.imageInfo["filePath"] = imagePath
        windowWidth = self.size().width()
        desiredImageWidth = round(windowWidth * self.imageProportionOfWindowWidth)
        pixmap = QPixmap(imagePath).scaled(desiredImageWidth, desiredImageWidth, Qt.AspectRatioMode.KeepAspectRatio)
        label.setPixmap(pixmap)
    
    # def resizeEvent(self, obj):
    #     width = obj.size().width()
    #     height = obj.size().height()

    # def mouseReleaseEvent(self, obj):
    #     print("Window was clicked")

    # def loadImage(self, imagePath):
        





def launchGui():
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    # backgroundThread = BackgroundThread()
    exit(app.exec())
