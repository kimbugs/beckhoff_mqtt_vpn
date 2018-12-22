from mqtt_manage import MqttManage

MAP = {"test_data": [("data", "H")]}
DEVICE_COUNT = 3

def device_interface():
    interface = []
    for device_index in range(1, DEVICE_COUNT + 1):
        interface.append(('test_data{}'.format(device_index), MAP["test_data"]))
    return interface

if __name__ == '__main__':
    interface = device_interface()
    mqttmanage = MqttManage("helios/1/PcsCommandInfo", interface)

    mqttmanage.loop()



