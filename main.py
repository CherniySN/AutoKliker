import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QThread
import time
import keyboard


class RefreshWindow(QThread):

    def __init__(self):
        QThread.__init__(self)

    def run(self):
        while True:
            try:
                if keyboard.is_pressed('Enter'):
                    print('You pressed enter for the second time!')
                    break
                start = time.time()
                while time.time() - start < 5:
                    keyboard.press('F1')
                    time.sleep(0.02)
                    if keyboard.is_pressed('Enter'):
                        print('You pressed enter for the first time!')
                        break
                time.sleep(0.5)
                print(str(time.ctime()) + ' зажата клавиша F1 на 4 секунд;')

            except:
                print('Исключение')


class App(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.refwind = RefreshWindow()
        self.set()

    def set(self):
        self.w_root = uic.loadUi('window.ui')
        self.w_root.openButton.cliked.connect(self.setClick)
        self.w_root.show()

    def setClick(self):
        self.refwind.start() # начало потока


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()
