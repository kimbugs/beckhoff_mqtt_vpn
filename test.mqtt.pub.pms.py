from mqtt_manage import MqttManage

if __name__ == '__main__':    
    data1 = 121
    data2 = 221
    data3 = 331

    data1 = data1.to_bytes(2, byteorder='little', signed=True)
    data2 = data2.to_bytes(2, byteorder='little', signed=True)
    data3 = data3.to_bytes(2, byteorder='little', signed=True)

    params = data1 + data2 + data3

    data4 = 1
    data5 = 1
    data6 = 1

    data4 = data4.to_bytes(2, byteorder='little', signed=True)
    data5 = data5.to_bytes(2, byteorder='little', signed=True)
    data6 = data6.to_bytes(2, byteorder='little', signed=True)

    params1 = data4 + data5 + data6

    data7 = 7777
    data8 = 88
    data9 = 99

    data7 = data7.to_bytes(2, byteorder='little', signed=True)
    data8 = data8.to_bytes(2, byteorder='little', signed=True)
    data9 = data9.to_bytes(2, byteorder='little', signed=True)

    params2 = data7 + data8 + data9
    MqttManage.write("helios/1/PcsCommandInfo", params)
    #MqttManage.write("helios/1/UserConfigCommand", params1)
    #MqttManage.write("helios/1/ProtectionCommand", params2)


