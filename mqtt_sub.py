from mqtt_manager_sub import MqttManagerSub

if __name__ == "__main__":
    mqtt_sub = MqttManagerSub("localhost",1883,"helios/1/pmsCommand")
    mqtt_sub.invoke()

