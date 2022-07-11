from PyQt5 import QtCore, QtGui, QtWidgets
from MainWindow import *


class SearchWindow(object):





    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_open_main_window = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open_main_window.setGeometry(QtCore.QRect(10, 440, 261, 50))
        self.btn_open_main_window.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_open_main_window.setStyleSheet("background-color: rgb(115, 199, 255);\n" "font: 18pt \"Times New "
                                                "Roman\";")
        self.btn_open_main_window.setAutoDefault(False)
        self.btn_open_main_window.setObjectName("btn_open_main_window")



        self.label_main_name = QtWidgets.QLabel(self.centralwidget)
        self.label_main_name.setGeometry(QtCore.QRect(0, 0, 1000, 40))
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
        self.btn_open_candidate_profile = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open_candidate_profile.setGeometry(QtCore.QRect(590, 440, 400, 50))
        self.btn_open_candidate_profile.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_open_candidate_profile.setStyleSheet("background-color: rgb(115, 199, 255);\n"
                                                      "font: 18pt \"Times New Roman\";")
        self.btn_open_candidate_profile.setAutoDefault(False)
        self.btn_open_candidate_profile.setObjectName("btn_open_candidate_profile")
        self.btn_search = QtWidgets.QPushButton(self.centralwidget)
        self.btn_search.setGeometry(QtCore.QRect(840, 70, 150, 40))
        self.btn_search.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_search.setStyleSheet("background-color: rgb(115, 199, 255);\n"
                                      "font: 18pt \"Times New Roman\";")
        self.btn_search.setAutoDefault(False)
        self.btn_search.setObjectName("btn_search")
        self.table_all_candidate = QtWidgets.QTableWidget(self.centralwidget)
        self.table_all_candidate.setGeometry(QtCore.QRect(10, 130, 980, 300))
        self.table_all_candidate.setObjectName("table_all_candidate")
        self.table_all_candidate.setColumnCount(0)
        self.table_all_candidate.setRowCount(0)
        self.plainTextEdit_search = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_search.setGeometry(QtCore.QRect(10, 70, 820, 40))
        self.plainTextEdit_search.setObjectName("plainTextEdit_search")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_open_main_window.setText(_translate("MainWindow", "Главное меню"))
        self.label_main_name.setText(_translate("MainWindow", "ИоНова - Центр Кадрового Развития"))
        self.btn_open_candidate_profile.setText(_translate("MainWindow", "Открыть профиль кандидата"))
        self.btn_search.setText(_translate("MainWindow", "Поиск"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = SearchWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
