import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
 
from Main_Dialog import Ui_MainWindow
from mqtt_manager import MqttManager
 
class MainDialog(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainDialog, self).__init__()
        self.setupUi(self)

        self.site_id = 'None'

        # btn connect
        self.btn_restart_pms.clicked.connect(self.on_pms_restart)
        self.btn_connect_vpn.clicked.connect(self.on_connect_vpn)
        self.btn_disconnect_vpn.clicked.connect(self.on_disconnect_vpn)
        self.btn_add_route_pms.clicked.connect(self.on_add_route_pms)

        # input connect
        self.input_site_id.textChanged.connect(self.set_site_id)

        # combobox connect
        self.combo_vpn_id_list.addItems(['HeliosVpn1', 'HeliosVpn2', 'HeliosVpn3', 'HeliosVpn4', 'HeliosVpn5', 'HeliosVpn6', 'HeliosVpn7', 'HeliosVpn8', 'HeliosVpn9'])

    def set_site_id(self):
        self.site_id = self.input_site_id.toPlainText()

    def on_pms_restart(self):
        self.mqtt_write_to_pms(1, 0)
        QMessageBox.about(self, "pms", "Site : " + self.site_id + " -> Restart")

    def on_connect_vpn(self):
        vpn_id = self.combo_vpn_id_list.currentIndex() + 1
        self.mqtt_write_to_pms(2, vpn_id)
        QMessageBox.about(self, "vpn", "Site : " + self.site_id + " -> Connect")

    def on_disconnect_vpn(self):
        self.mqtt_write_to_pms(3, 0)
        QMessageBox.about(self, "vpn", "Site : " + self.site_id + " -> Disconnect")

    def on_add_route_pms(self):
        self.mqtt_write_to_pms(4, 0)
        QMessageBox.about(self, "vpn", "Site : " + self.site_id + " -> Added Route")

    def mqtt_write_to_pms(self, operation, referenceValue):
        data1 = 0
        data2 = 0
        data3 = 1

        if operation == 1:
            data1 = 1
        elif operation == 2:
            data1 = 2
            data2 = referenceValue
        elif operation == 3:
            data1 = 3
        elif operation == 4:
            data1 = 4
        else:
            data1 = 0
            data2 = 0
            data3 = 0

        data1 = data1.to_bytes(2, byteorder='little', signed=True)
        data2 = data2.to_bytes(2, byteorder='little', signed=True)
        data3 = data3.to_bytes(2, byteorder='little', signed=True)

        params = data1 + data2 + data3
        MqttManager.write("helios/" + self.site_id + "/PmsCommand", params)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainDialog()
    ui.show()
    sys.exit(app.exec_())
