from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QGridLayout, QHBoxLayout, QLabel, QVBoxLayout, QGroupBox
from PyQt6.QtGui import QPixmap
from PyQt6 import QtCore
import os
import sys

class GUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GUI Thing")

        self.mainLayout = QHBoxLayout()
        self.setLayout(self.mainLayout)

        ## create image view window
        self.imageLabel = QLabel()
        self.mainLayout.addWidget(self.imageLabel)
        self.setImage(self.imageLabel, os.path.join(os.getcwd(),"test_image.jpg"))
        # self.imageLabel.resize(200, 200)

        ## create side menu
        self.sideMenu = QGroupBox()
        self.mainLayout.addWidget(self.sideMenu)
        self.sideMenuLayout = QVBoxLayout()
        self.sideMenu.setLayout(self.sideMenuLayout)

        testButton = QPushButton(text="button")
        self.sideMenuLayout.addWidget(testButton)

        self.resize(100, 100)

    def setImage(self, label, imagePath):
        pixmap = QPixmap(imagePath)
        pixmap = pixmap.scaled(400, 400, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        label.setPixmap(pixmap)



def launchGui():
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    exit(app.exec())
