from PyQt5 import QtCore, QtGui, QtWidgets
from NewCandidateWindow import *
from SearchWindow import *


class MainWindowClass(object):

    def openCandidateSearch(self):
        self.win = QtWidgets.QMainWindow()
        self.ui = SearchWindow()
        self.ui.setupUi(self.win)
        self.win.show()

    def openNewCandidate(self):
        self.win = QtWidgets.QMainWindow()
        self.ui = NewCandidateWindow()
        self.ui.setupUi(self.win)
        self.win.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 500)
        font = QtGui.QFont()
        font.setFamily("Sitka Heading")
        font.setPointSize(18)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_main_name = QtWidgets.QLabel(self.centralwidget)
        self.label_main_name.setGeometry(QtCore.QRect(0, 10, 1000, 40))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_main_name.setFont(font)
        self.label_main_name.setMouseTracking(False)
        self.label_main_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_main_name.setWordWrap(False)
        self.label_main_name.setObjectName("label_main_name")

        self.btn_candidate_search = QtWidgets.QPushButton(self.centralwidget)
        self.btn_candidate_search.setGeometry(QtCore.QRect(200, 125, 600, 70))
        self.btn_candidate_search.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_candidate_search.setStyleSheet("background-color: rgb(115, 199, 255);\n"
                                                "font: 18pt \"Times New Roman\";")
        self.btn_candidate_search.setAutoDefault(False)
        self.btn_candidate_search.setObjectName("btn_candidate_search")

        self.btn_candidate_search.clicked.connect(self.openCandidateSearch)

        self.btn_new_candidate = QtWidgets.QPushButton(self.centralwidget)
        self.btn_new_candidate.setGeometry(QtCore.QRect(200, 375, 600, 70))
        self.btn_new_candidate.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_new_candidate.setStyleSheet("background-color: rgb(115, 199, 255);\n"
                                             "font: 18pt \"Times New Roman\";")
        self.btn_new_candidate.setAutoDefault(False)
        self.btn_new_candidate.setObjectName("btn_new_candidate")

        self.btn_new_candidate.clicked.connect(self.openNewCandidate)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_main_name.setText(_translate("MainWindow", "ИоНова - Центр Кадрового Развития"))
        self.btn_candidate_search.setText(_translate("MainWindow", "Поиск кандидата"))
        self.btn_new_candidate.setText(_translate("MainWindow", "Новый кандидат"))




