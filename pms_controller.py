from PyQt5.QtWidgets import *
from mqtt_manager import MqttManager

VPN_IPs = ['10.100.10.1', '10.100.10.11', '10.100.10.12', '10.100.10.13', '10.100.10.14',
            '10.100.10.15', '10.100.10.16', '10.100.10.17', '10.100.10.18', '10.100.10.19']


class PmsController(object):
    def __init__(self):
        self.site_id = ' None'
        pass

    def set_site_id(self, site_id):
        self.site_id = site_id

    def check_vpn_id(self, vpn_index):
        result_msg = "NONE"
        if vpn_index == 0:
            result_msg = "Select VPN ID"
        else:
            # check ping
            result_msg = "HeliosVpn" + str(vpn_index) + " is used!!"

        return result_msg
            
    def on_pms_restart(self):
        self.mqtt_write_to_pms(1, 0)

        return "Site : " + self.site_id + " -> Restart"

    def on_connect_vpn(self, vpn_index):
        vpn_index = vpn_index
        self.mqtt_write_to_pms(2, vpn_index)

        return  "Site : " + self.site_id + " -> Connect"

    def on_disconnect_vpn(self):
        self.mqtt_write_to_pms(3, 0)
        
        return "Site : " + self.site_id + " -> Disconnect"

    def on_add_route_pms(self):
        self.mqtt_write_to_pms(4, 0)
        
        return "Site : " + self.site_id + " -> Added Route"

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