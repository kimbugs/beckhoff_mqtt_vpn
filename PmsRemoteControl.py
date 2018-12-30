import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from PyQt5.QtCore import QTimer, QThread, pyqtSignal
from PyQt5 import QtTest
 
#from functools import partial
from time import sleep

from Main_Dialog import Ui_MainWindow
from pms_controller import PmsController

VPN_IDs = ['None', 'HeliosVpn1', 'HeliosVpn2', 'HeliosVpn3', 'HeliosVpn4', 'HeliosVpn5', 
            'HeliosVpn6', 'HeliosVpn7', 'HeliosVpn8', 'HeliosVpn9']

VPN_IPs = ['10.100.0.1', '10.100.10.11', '10.100.10.12', '10.100.10.13', '10.100.10.14',
            '10.100.10.15', '10.100.10.16', '10.100.10.17', '10.100.10.18', '10.100.10.19']

class VpnStatusCheck(QThread):
    threadEvent = QtCore.pyqtSignal(int)

    def run(self):
        

class MainDialog(QMainWindow, Ui_MainWindow, PmsController):
    def __init__(self):
        super(MainDialog, self).__init__()
        self.setupUi(self)
        self.site_id = 'None'

        # Qtimer
        self.timer_vpn_status = QTimer(self)
        self.timer_vpn_status.timeout.connect(self.check_vpn_status)
        self.timer_vpn_status.start(2000)

        # btn connect
        self.btn_restart_pms.clicked.connect(self.slot_pms_restart)
        self.btn_connect_vpn.clicked.connect(self.slot_connect_vpn)
        self.btn_disconnect_vpn.clicked.connect(self.slot_disconnect_vpn)
        self.btn_add_route_pms.clicked.connect(self.slot_add_route_pms)

        # input connect
        self.input_site_id.textChanged.connect(self.slot_site_id)

        # combobox connect
        self.combo_vpn_id_list.addItems(VPN_IDs)
        self.combo_vpn_id_list.currentTextChanged.connect(self.slot_vpn_id)

    def check_vpn_status(self):
        print('vpn server : True')
        print('vpn clinet(10.100.10.11) : True')

    def slot_site_id(self):
        self.site_id = self.input_site_id.toPlainText()
        self.set_site_id(self.site_id)

    def slot_vpn_id(self):
        vpn_index = self.combo_vpn_id_list.currentIndex()

        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Loding...")
        msg_box.setText("Please wait....")
        msg_box.open()
        result = self.check_ping(VPN_IPs[vpn_index])
        QtTest.QTest.qWait(1000)
        msg_box.close()
        
        if result:
            result_msg = "HeliosVpn" + str(vpn_index) + " is used, select another id"
        else:
            result_msg = "HeliosVpn" + str(vpn_index) + " is available"

        QMessageBox.about(self, "vpn", result_msg)

    def slot_connect_vpn(self):
        vpn_index = self.combo_vpn_id_list.currentIndex()
        self.on_connect_vpn(vpn_index)
        
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Loding...")
        msg_box.setText("Please wait 10s....")
        msg_box.open()
        QtTest.QTest.qWait(10000)
        result = self.check_ping(VPN_IPs[vpn_index])
        msg_box.close()

        if result:
            result_msg = "Site : " + self.site_id + " -> Connected"
        else:
            result_msg = "Site : " + self.site_id + " -> Fail"

        QMessageBox.about(self, "vpn", result_msg)
        
    def slot_disconnect_vpn(self):
        vpn_index = self.combo_vpn_id_list.currentIndex()
        result_msg = self.on_disconnect_vpn()

        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Loding...")
        msg_box.setText("Please wait 10s....")
        msg_box.open()
        QtTest.QTest.qWait(10000)
        result = self.check_ping(VPN_IPs[vpn_index])
        msg_box.close()

        if not result:
            result_msg = "Site : " + self.site_id + " -> Disconnected"
        else:
            result_msg = "Site : " + self.site_id + " -> Fail"

        QMessageBox.about(self, "vpn", result_msg)

    def slot_pms_restart(self):
        result = self.on_pms_restart()

        if result:
            result_msg = "Site : " + self.site_id + " -> Restart"
        else:
            result_msg = "Site : " + self.site_id + " -> Fail"

        QMessageBox.about(self, "pms", result_msg)

    def slot_add_route_pms(self):
        result = self.on_add_route_pms()

        if result:
            result_msg = "Site : " + self.site_id + " -> Added Route"
        else:
            result_msg = "Site : " + self.site_id + " -> Fail"

        QMessageBox.about(self, "vpn", result_msg)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainDialog()
    ui.show()
    sys.exit(app.exec_())
