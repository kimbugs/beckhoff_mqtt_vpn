import unittest
from mqtt_manager import MqttManager
from pms_controller import PmsController

class Test_Main(unittest.TestCase):

    def test_mqtt_publish(self):
        self.assertIs(MqttManager.write("helios/10000/PmsCommand", "test"), True)

    def test_pms_controller(self):
        pms = PmsController()

        pms.set_site_id('10000')
        
        # pms func test
        self.assertIs(pms.on_pms_restart(), True)
        self.assertIs(pms.on_connect_vpn(1), True)
        self.assertIs(pms.on_disconnect_vpn(), True)
        self.assertIs(pms.on_add_route_pms(), True)

        # ip ping test
        self.assertIs(pms.check_ping('localhost'), True)

if __name__ == "__main__":
    unittest.main()