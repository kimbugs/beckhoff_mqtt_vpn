import paho.mqtt.client as mqtt

class MqttManagerSub:
    def __init__(self, ip, port, subId):
        self.ip = ip
        self.port = port
        self.subId = subId
        self.client = mqtt.Client()

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))

        self.client.subscribe(self.subId)

    def on_message(self, client, userdata, msg):
        print(msg.topic + " " + str(msg.payload))

    def invoke(self):
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(host=self.ip, port=self.port)
        self.client.loop_forever()