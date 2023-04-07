from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QGridLayout, QHBoxLayout, QLabel, QVBoxLayout, QGroupBox
from PyQt6.QtGui import QPixmap
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

        ## create side menu
        self.sideMenu = QGroupBox()
        self.mainLayout.addWidget(self.sideMenu)
        self.sideMenuLayout = QVBoxLayout()
        self.sideMenu.setLayout(self.sideMenuLayout)

        testButton = QPushButton(text="button")
        self.sideMenuLayout.addWidget(testButton)



def launchGui():
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    exit(app.exec())
