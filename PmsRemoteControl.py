import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
 
from functools import partial

from Main_Dialog import Ui_MainWindow
from pms_controller import PmsController

VPN_IDs = ['None', 'HeliosVpn1', 'HeliosVpn2', 'HeliosVpn3', 'HeliosVpn4', 'HeliosVpn5', 
            'HeliosVpn6', 'HeliosVpn7', 'HeliosVpn8', 'HeliosVpn9']

class MainDialog(QMainWindow, Ui_MainWindow, PmsController):
    def __init__(self):
        super(MainDialog, self).__init__()
        self.setupUi(self)

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

    def slot_site_id(self):
        site_id = self.input_site_id.toPlainText()
        self.set_site_id(site_id)

    def slot_vpn_id(self):
        vpn_index = self.combo_vpn_id_list.currentIndex()
        result_msg = self.check_vpn_id(vpn_index)

        QMessageBox.about(self, "vpn", result_msg)

    def slot_connect_vpn(self):
        vpn_index = self.combo_vpn_id_list.currentIndex()
        result_msg = self.on_connect_vpn(vpn_index)

        QMessageBox.about(self, "vpn", result_msg)

    def slot_disconnect_vpn(self):
        result_msg = self.on_disconnect_vpn()

        QMessageBox.about(self, "vpn", result_msg)

    def slot_pms_restart(self):
        result_msg = self.on_pms_restart()

        QMessageBox.about(self, "pms", result_msg)

    def slot_add_route_pms(self):
        result_msg = self.on_add_route_pms()

        QMessageBox.about(self, "vpn", result_msg)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainDialog()
    ui.show()
    sys.exit(app.exec_())
