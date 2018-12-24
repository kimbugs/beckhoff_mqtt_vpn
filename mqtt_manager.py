import paho.mqtt.client as mqtt

class MqttManager:
    CONFIG = {
        "ip": "localhost",
        "port": 1883,
        "keepalive": 60,
        "username": "",
        "password": ""
    }

    @classmethod
    def write(cls, key, value):
        m = mqtt.Client("python_pub")
        m.username_pw_set(username=cls.CONFIG['username'], password=cls.CONFIG['password'])
        m.connect(cls.CONFIG['ip'], cls.CONFIG['port'])

        m.publish(key, value)
