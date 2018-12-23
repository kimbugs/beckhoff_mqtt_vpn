# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(484, 382)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_restart_pms = QtWidgets.QPushButton(self.centralwidget)
        self.btn_restart_pms.setGeometry(QtCore.QRect(30, 80, 131, 71))
        self.btn_restart_pms.setObjectName("btn_restart_pms")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(33, 20, 60, 20))
        self.label.setObjectName("label")
        self.input_site_id = QtWidgets.QTextEdit(self.centralwidget)
        self.input_site_id.setGeometry(QtCore.QRect(80, 20, 51, 21))
        self.input_site_id.setPlaceholderText("")
        self.input_site_id.setObjectName("input_site_id")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(188, 50, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.btn_connect_vpn = QtWidgets.QPushButton(self.centralwidget)
        self.btn_connect_vpn.setGeometry(QtCore.QRect(180, 80, 131, 71))
        self.btn_connect_vpn.setObjectName("btn_connect_vpn")
        self.btn_disconnect_vpn = QtWidgets.QPushButton(self.centralwidget)
        self.btn_disconnect_vpn.setGeometry(QtCore.QRect(330, 80, 131, 71))
        self.btn_disconnect_vpn.setObjectName("btn_disconnect_vpn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 484, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_restart_pms.setText(_translate("MainWindow", "Restart Pms"))
        self.label.setText(_translate("MainWindow", "Site Id"))
        self.label_2.setText(_translate("MainWindow", "Pms Command"))
        self.btn_connect_vpn.setText(_translate("MainWindow", "Connect VPN"))
        self.btn_disconnect_vpn.setText(_translate("MainWindow", "Disconnect VPN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

