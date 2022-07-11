from PyQt5 import *
from MainWindow import *
from CandidateInfoWindow import *
from NewCandidateWindow import *
from SearchWindow import *

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindowClass()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
