import unittest
from mqtt_manager import MqttManager
from pms_controller import PmsController

class Test_Main(unittest.TestCase):

    def test_mqtt_publish(self):
        self.assertIs(MqttManager.write("helios/10000/PmsCommand", "test"), True)

    def test_pms_controller(self):
        pms = PmsController()

        pms.check_vpn_id('10000')
        
        # pms func test
        self.assertIn("Site",pms.on_pms_restart())
        self.assertIn("Site",pms.on_connect_vpn(1))
        self.assertIn("Site",pms.on_disconnect_vpn())
        self.assertIn("Site",pms.on_add_route_pms())

        # ip ping test
        self.assertIs(pms.check_ping('localhost'), True)

if __name__ == "__main__":
    unittest.main()