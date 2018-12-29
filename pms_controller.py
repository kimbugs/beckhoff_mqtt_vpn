from mqtt_manager import MqttManager

VPN_IPs = ['10.100.0.1', '10.100.10.11', '10.100.10.12', '10.100.10.13', '10.100.10.14',
            '10.100.10.15', '10.100.10.16', '10.100.10.17', '10.100.10.18', '10.100.10.19']

import subprocess

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
            result = self.check_ping(VPN_IPs[vpn_index])
            if result:
                result_msg = "HeliosVpn" + str(vpn_index) + " is used, select another id"
            else:
                result_msg = "HeliosVpn" + str(vpn_index) + " is available"
            
        return result_msg
            
    def on_pms_restart(self):
        result = self.mqtt_write_to_pms(1, 0)
        
        if result:
            return "Site : " + self.site_id + " -> Restart"
        else:
            return "Site : " + self.site_id + " -> Fail"
        
    def on_connect_vpn(self, vpn_index):
        vpn_index = vpn_index
        result = self.mqtt_write_to_pms(2, vpn_index)
        
        if result:
            return  True
        else:
            return  False
        
    def on_disconnect_vpn(self):
        result = self.mqtt_write_to_pms(3, 0)

        if result:
            return "Site : " + self.site_id + " -> Disconnect"
        else:
            return "Site : " + self.site_id + " -> Fail"
        
    def on_add_route_pms(self):
        result = self.mqtt_write_to_pms(4, 0)
        
        if result:
            return "Site : " + self.site_id + " -> Added Route"
        else:
            return "Site : " + self.site_id + " -> Fail"
        
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
        result = MqttManager.write("helios/" + self.site_id + "/PmsCommand", params)

        if result:
            return True
        else:
            return False

    def check_ping(self, host_ip):
        hostname = host_ip
        sub_p = subprocess.Popen(["ping", "-W", "500", "-c", "1", hostname], stdout=subprocess.PIPE)
        sub_p.wait()
        response = sub_p.poll()
        # and then check the response...
        if response == 0 :
            return True
        else:
            return False

