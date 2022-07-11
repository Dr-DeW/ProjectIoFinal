from PyQt5 import QtCore, QtGui, QtWidgets


class CandidateInfoWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_fio = QtWidgets.QLabel(self.centralwidget)
        self.label_fio.setGeometry(QtCore.QRect(390, 100, 600, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_fio.setFont(font)
        self.label_fio.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_fio.setObjectName("label_fio")
        self.text_all_info_candidate = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_all_info_candidate.setGeometry(QtCore.QRect(390, 160, 600, 330))
        self.text_all_info_candidate.setObjectName("text_all_info_candidate")
        self.graphics_foto = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphics_foto.setGeometry(QtCore.QRect(40, 100, 250, 250))
        self.graphics_foto.setObjectName("graphics_foto")
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
        self.label_final_score = QtWidgets.QLabel(self.centralwidget)
        self.label_final_score.setGeometry(QtCore.QRect(40, 360, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_final_score.setFont(font)
        self.label_final_score.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_final_score.setObjectName("label_final_score")
        self.btn_open_main_window = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open_main_window.setGeometry(QtCore.QRect(40, 440, 261, 50))
        self.btn_open_main_window.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_open_main_window.setStyleSheet("background-color: rgb(115, 199, 255);\n"
                                                "font: 18pt \"Times New Roman\";")
        self.btn_open_main_window.setAutoDefault(False)
        self.btn_open_main_window.setObjectName("btn_open_main_window")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_fio.setText(_translate("MainWindow", "ФИО: "))
        self.label_main_name.setText(_translate("MainWindow", "ИоНова - Центр Кадрового Развития"))
        self.label_final_score.setText(_translate("MainWindow", "Итоговый балл:"))
        self.btn_open_main_window.setText(_translate("MainWindow", "Главное меню"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = CandidateInfoWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
