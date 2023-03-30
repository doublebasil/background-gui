from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QGridLayout
import sys

def buildImageWindow(root):
    widget = QWidget()
    root.addWidget(widget)
    grid = QGridLayout(widget)
    root.addLayout(grid)
    thing1 = QPushButton(grid)
    thing2 = QPushButton(grid)

def buildGui(root):
    mainGrid = QGridLayout()
    root.setLayout(mainGrid)
    buildImageWindow(mainGrid)

def main():
    app = QApplication(sys.argv)
    root = QMainWindow()
    buildGui(root)
    root.show()
    app.exec()

# if __name__ == '__main__':
#     main()

app = QApplication(sys.argv)
mainWindow = QMainWindow()
mainWidget = QWidget
QGridLayout(mainWindow)
mainWindow.setLayout(mainWindowLayout)
mainWindow.show()
app.exec()