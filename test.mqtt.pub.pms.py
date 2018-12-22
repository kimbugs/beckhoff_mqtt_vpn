from mqtt_manage import MqttManage
import PyQt5

if __name__ == '__main__':    
    data1 = 2
    data2 = 0
    data3 = 1

    data1 = data1.to_bytes(2, byteorder='little', signed=True)
    data2 = data2.to_bytes(2, byteorder='little', signed=True)
    data3 = data3.to_bytes(2, byteorder='little', signed=True)

    params = data1 + data2 + data3
    MqttManage.write("helios/1/PcsCommandInfo", params)

