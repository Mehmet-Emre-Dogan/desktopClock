try:
    with open("useLightTheme", "r", encoding="utf-8") as fil:
        from _myGuiLight import Ui_MainWindow
except:
    from _myGuiDark import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import QtCore 
from PyQt5 import QtGui 
import sys
from time import sleep
from datetime import datetime

class BGworker(QThread):
    mySignal = pyqtSignal(int)
    def run(self):
        while True:
            self.mySignal.emit(1)
            sleep(0.5)
            
class myWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(myWindow, self).__init__()
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint) #always on top
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('clock.png'))
        self.setWindowTitle("Clock")
        self.worker = BGworker()
        self.worker.mySignal.connect(self.whenSignalReceived)
        self.worker.start()

    def whenSignalReceived(self, val):
        clock = datetime.now()
        self.ui.progressBar.setValue(clock.second)
        if clock.hour < 10:
            if clock.minute < 10:
                self.ui.label.setText(f"0{clock.hour}:0{clock.minute}")
            else:
                self.ui.label.setText(f"0{clock.hour}:{clock.minute}")
        else:
            if clock.minute < 10:
                self.ui.label.setText(f"{clock.hour}:0{clock.minute}")
            else:
                self.ui.label.setText(f"{clock.hour}:{clock.minute}")
        if clock.second < 10:
            self.ui.label_2.setText(f":0{clock.second}")
        else:
            self.ui.label_2.setText(f":{clock.second}")

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myWindow()
    win.show()
    sys.exit(app.exec_())

app()
