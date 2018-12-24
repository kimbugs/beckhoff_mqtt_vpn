# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(634, 231)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(310, 30, 271, 151))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.btn_disconnect_vpn = QtWidgets.QPushButton(self.groupBox)
        self.btn_disconnect_vpn.setGeometry(QtCore.QRect(140, 30, 121, 41))
        self.btn_disconnect_vpn.setObjectName("btn_disconnect_vpn")
        self.btn_restart_pms = QtWidgets.QPushButton(self.groupBox)
        self.btn_restart_pms.setGeometry(QtCore.QRect(10, 90, 121, 41))
        self.btn_restart_pms.setObjectName("btn_restart_pms")
        self.btn_connect_vpn = QtWidgets.QPushButton(self.groupBox)
        self.btn_connect_vpn.setGeometry(QtCore.QRect(10, 30, 121, 41))
        self.btn_connect_vpn.setObjectName("btn_connect_vpn")
        self.btn_add_route_pms = QtWidgets.QPushButton(self.groupBox)
        self.btn_add_route_pms.setGeometry(QtCore.QRect(140, 90, 121, 41))
        self.btn_add_route_pms.setObjectName("btn_add_route_pms")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 30, 271, 151))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(12, 20, 51, 21))
        self.label.setObjectName("label")
        self.input_site_id = QtWidgets.QTextEdit(self.groupBox_2)
        self.input_site_id.setGeometry(QtCore.QRect(69, 20, 101, 21))
        self.input_site_id.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.input_site_id.setPlaceholderText("")
        self.input_site_id.setObjectName("input_site_id")
        self.combo_vpn_id_list = QtWidgets.QComboBox(self.groupBox_2)
        self.combo_vpn_id_list.setGeometry(QtCore.QRect(70, 60, 101, 22))
        self.combo_vpn_id_list.setObjectName("combo_vpn_id_list")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(12, 59, 51, 21))
        self.label_2.setObjectName("label_2")
        self.groupBox_2.raise_()
        self.groupBox.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 634, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Pms Command"))
        self.btn_disconnect_vpn.setText(_translate("MainWindow", "Disconnect VPN"))
        self.btn_restart_pms.setText(_translate("MainWindow", "Restart Pms"))
        self.btn_connect_vpn.setText(_translate("MainWindow", "Connect VPN"))
        self.btn_add_route_pms.setText(_translate("MainWindow", "Add Route VPN"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Site Set"))
        self.label.setText(_translate("MainWindow", "SITE ID"))
        self.label_2.setText(_translate("MainWindow", "VPN ID"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

